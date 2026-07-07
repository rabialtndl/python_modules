import sys
import typing


def archive_creation(file_path: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")

    file_obj: typing.IO[str] | None = None
    content: str = ""

    try:
        file_obj = open(file_path, "r")
        content = file_obj.read()
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

    print("\nTransform data:")
    transformed_content: str = ""
    print("---")
    print()
    if content:
        raw_lines: list[str] = content.splitlines()
        for line in raw_lines:
            transformed_line: str = f"{line}#"
            print(transformed_line)
            transformed_content += transformed_line + "\n"
    print()
    print("---")
    new_file: str = input("Enter new file name (or empty): ")
    if not new_file:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    write_obj: typing.IO[str] | None = None
    try:
        write_obj = open(new_file, "w")
        write_obj.write(transformed_content)
        print(f"Data saved in file '{new_file}'.")
    except Exception as ex:
        print(f"Error saving file '{new_file}': {ex}")
    finally:
        if write_obj is not None:
            write_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    archive_creation(sys.argv[1])


if __name__ == "__main__":
    main()
