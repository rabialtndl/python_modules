def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    temp_inputs = ["25", "abc", "100", "-50"]

    for data in temp_inputs:
        print(f"Input data is '{data}'")

        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print("")
        except Exception as ex:
            print(f"Caught input_temperature error: {ex}")
            print("")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature()
    print("All tests completed - program didn't crash!")
