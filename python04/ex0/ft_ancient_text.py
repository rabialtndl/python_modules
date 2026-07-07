import sys
import typing


def ancient_text(file_path: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")
    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(file_path, "r")
        content: str = file_obj.read()
        print("---")
        print()
        print(content, end="")
        print()
        print("---")

    except Exception as ex:
        print(f"Error opening file '{file_path}': {ex}")
        return

    if file_obj is not None:
        file_obj.close()
        print(f"File '{file_path}' closed.")


def main() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
