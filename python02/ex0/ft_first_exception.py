def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp_inputs = ["25", "abc"]

    for data in temp_inputs:
        print(f"Input data is '{data}'")

        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print("")
        except Exception as ex:
            print(f"Caught input_temperature error: {ex}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
    print(" ")
    print("All tests completed - program didn't crash!")
