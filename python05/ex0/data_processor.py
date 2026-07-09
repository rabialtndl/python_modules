import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("Storage is empty.")

        first = self._storage[0]
        self._storage = self._storage[1:]
        return first


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            for item in data:
                if (
                    not isinstance(item, (int, float))
                    or isinstance(item, bool)
                ):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]

        for item in items:
            packet = (self._rank, str(item))
            self._storage = self._storage + [packet]
            self._rank = self._rank + 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]

        for item in items:
            packet = (self._rank, str(item))
            self._storage = self._storage + [packet]
            self._rank = self._rank + 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False

                for key, value in item.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]

        for item in items:
            log_str = (
                f"{item.get('log_level', '')}: "
                f"{item.get('log_message', '')}"
            )
            packet = (self._rank, log_str)
            self._storage = self._storage + [packet]
            self._rank = self._rank + 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric_process = NumericProcessor()
    print(f" Trying to validate input '42': {numeric_process.validate(42)}")
    print(f" Trying to validate input 'Hello':"
          f"{numeric_process.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")

    try:
        numeric_process.ingest("foo")
    except ValueError as ex:
        print(f" Got exception : {ex}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")

    numeric_process.ingest(num_data)
    print(" Extracting 3 values...")

    for x in range(0, 3):
        rank, value = numeric_process.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_process = TextProcessor()
    print(f" Trying to validate input '42': {text_process.validate(42)}")
    test_data = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {test_data}")

    text_process.ingest(test_data)
    print(" Extracting 1 value...")
    rank, value = text_process.output()
    print(f" Text value {rank} : {value}")

    print("\nTesting Log Processor...")
    log_process = LogProcessor()
    print(
         f" Trying to validate input 'Hello': "
         f" {log_process.validate('Hello')}")
    log_data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]

    log_process.ingest(log_data)
    print(f" Processing data: {log_data}")
    print(" Extracting 2 values...")
    for _ in range(0, 2):
        rank, value = log_process.output()
        print(
              f" Log entry {rank}:"
              f" {value}"
              )


if __name__ == "__main__":
    main()
