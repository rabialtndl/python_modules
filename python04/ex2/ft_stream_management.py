import sys
import typing


def stream_man(file_path: str) -> None:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{file_path}'\n")

    file_obj: typing.IO[str] | None = None
    content: str = ""

    try:
        file_obj = open(file_path, "r")
        content = file_obj.read()
        print("---")
        print()
        sys.stdout.write(content)
        print()
        print("---")
    except Exception as ex:
        sys.stderr.write(f"[STDERR] Error opening file '{file_path}': {ex}\n")
        return

    if file_obj is not None:
        file_obj.close()
        sys.stdout.write(f"File '{file_path}' closed.\n")

    sys.stdout.write("\nTransform data:\n")
    transformed_content: str = ""
    print("---")
    print()
    if content:
        raw_lines: list[str] = content.splitlines()
        for line in raw_lines:
            transformed_line: str = f"{line}#"
            sys.stdout.write(f"{transformed_line}\n")
            transformed_content += transformed_line + "\n"
    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_file: str = sys.stdin.readline()
    new_file = new_file.rstrip("\r\n")

    if not new_file:
        sys.stdout.write("Not saving data.\n")
        return

    print(f"Saving data to '{new_file}'")
    write_obj: typing.IO[str] | None = None
    try:
        write_obj = open(new_file, "w")
        write_obj.write(transformed_content)
        sys.stdout.write(f"Data saved in file '{new_file}'.\n")
    except Exception as ex:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {ex}\n")
        sys.stdout.write("Data not saved.\n")
    finally:
        if write_obj is not None:
            write_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
        return
    stream_man(sys.argv[1])


if __name__ == "__main__":
    main()
