class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


def water_plant(name: str) -> None:
    if name != name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{name}'")
    else:
        print(f"Watering {name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce", "carrots"]
    try:
        for i in valid_plants:
            water_plant(i)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
        print("")
        print("Testing WaterError...")
    finally:
        print("Closing watering system")
        print("")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for i in invalid_plants:
            water_plant(i)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
