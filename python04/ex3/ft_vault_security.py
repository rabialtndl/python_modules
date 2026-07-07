def secure_archive(file_name: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(file_name, "r") as file_obj:
                data: str = file_obj.read()
                return True, data
        elif mode == "w":
            with open(file_name, "w") as file_obj:
                file_obj.write(content)
                return True, "Content successfully written to file"
        else:
            return False, f"Unsupported mode: {mode}"
    except Exception as ex:
        return False, str(ex)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    example1 = secure_archive("/not/existing/file", "r")
    print(example1)

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    example2 = secure_archive("/etc/master.passwd", "r")
    print(example2)

    print()
    ancient_fragment_data = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        " [FRAGMENT 002] Knowledge must survive the entropy wars\n"
        " [FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    ancient_fragment_file = "ancient_fragment.txt"
    secure_archive(ancient_fragment_file, "w", ancient_fragment_data)
    example3 = secure_archive(ancient_fragment_file, "r")
    print("Using 'secure_archive' to read from a regular file:")
    print(example3)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    example4 = secure_archive("new_file.txt", "w", ancient_fragment_data)
    print(example4)


if __name__ == "__main__":
    main()
