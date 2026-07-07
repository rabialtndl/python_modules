class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def check_water(water: float) -> None:
    if water <= 10:
        raise WaterError


def check_plant(name: str, plant_list: list) -> None:
    if name not in plant_list:
        raise PlantError(f"The {name} plant is wilting!")


def test_error_types() -> None:
    garden_plants = ["rose"]
    print("Testing PlantError...")
    try:
        check_plant("tomato", garden_plants)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
        print("")
    print("Testing WaterError...")
    try:
        check_water(2)
    except WaterError as ex:
        print(f"Caught WaterError: {ex}")
        print("")
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", garden_plants)
    except GardenError as ex:
        print(f"Caught GardenError: {ex}")
    try:
        check_water(4)
    except GardenError as ex:
        print(f"Caught GardenError: {ex}")
        print("")
    finally:
        print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print("")
    test_error_types()
