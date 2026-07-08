import typing
import abc


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [text for rank, text in data]
        csv_string = ",".join(values)
        print("CSV Output:")
        print(csv_string)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_parts = []
        for rank, text in data:
            part = f'"item_{rank}": "{text}"'
            json_parts.append(part)

        json_string = "{" + ", ".join(json_parts) + "}"
        
        print("JSON Output:")
        print(json_string)
        


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0
        self._total_processed: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("Storage is empty.")

        first = self._storage[0]
        self._storage = self._storage[1:]
        return first

    def get_stats(self) -> tuple[int, int]:
        return self._total_processed, len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.typing.Any) -> bool:
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
            raise ValueError(" Got exception: Improper numeric data")

        if isinstance(data, list):
            for item in data:
                packet = (self._rank, str(item))
                self._storage.append(packet)
                self._rank += 1
                self._total_processed += 1
        else:
            packet = (self._rank, str(data))
            self._storage.append(packet)
            self._rank += 1
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.typing.Any) -> bool:
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
            raise ValueError(" Got exception: Improper text data")
        if isinstance(data, list):
            for item in data:
                packet = (self._rank, str(item))
                self._storage.append(packet)
                self._rank += 1
                self._total_processed += 1
        else:
            packet = (self._rank, str(data))
            self._storage.append(packet)
            self._rank += 1
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.typing.Any) -> bool:
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
            raise ValueError(" Got exception: Improper log data")

        if isinstance(data, list):
            for item in data:
                log_str = str(item)
                packet = (self._rank, log_str)
                self._storage.append(packet)
                self._rank += 1
                self._total_processed += 1
        else:
            log_str = str(data)
            packet = (self._rank, log_str)
            self._storage.append(packet)
            self._rank += 1
            self._total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[typing.typing.Any]) -> None:
        for element in stream:
            processor_founded = False
            for processor in self._processor:
                if processor.validate(element):
                    processor.ingest(element)
                    processor_founded = True
                    break
            if not processor_founded:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self._processor:
            print("No processor found, no data")
            return

        for process in self._processor:
            total, remaining = process.get_stats()
            if process.__class__.__name__ == "NumericProcessor":
                print(f"Numeric Processor: total {total} items processed,"
                      f" remaining {remaining} on processor")
            elif process.__class__.__name__ == "TextProcessor":
                print(f"Text Processor: total {total} items processed, "
                      f" remaining {remaining} on processor")
            elif process.__class__.__name__ == "LogProcessor":
                print(f"Log Processor: total {total} items processed,"
                      f" remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processor:
            data = []
            for _ in range(nb):
                if not processor._data:
                    break
                item = processor.output()
                data.append(item)
            if data:
                plugin.process_output(data)

    
def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n Initialize Data Stream... \n == DataStream statistics ==")
    numeric_process = NumericProcessor()

    

if __name__ == "__main__":
    main()
