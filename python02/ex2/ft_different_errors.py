def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        "garden" + 0
    return 4


def test_error_types() -> None:
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as ex:
            print(f"Caught ValueError: {ex}")
        except ZeroDivisionError as ex:
            print(f"Caught ZeroDivisionError: {ex}")
        except FileNotFoundError as ex:
            print(f"Caught FileNotFoundError: {ex}")
        except TypeError as ex:
            print(f"Caught TypeError: {ex}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully!")
