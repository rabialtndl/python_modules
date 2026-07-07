import sys


def command_quest() -> None:
    total_len = len(sys.argv)
    print(f"Program name : {sys.argv[0]}")
    if (total_len == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_len -1}")
        for i in range(1, total_len):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total_len}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
    print()
