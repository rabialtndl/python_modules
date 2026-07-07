import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        set_of_coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z':"
            )
        parts = [part.strip() for part in set_of_coordinates.split(',')]
        total_len = len(parts)
        if (total_len != 3):
            print("Invalid syntax")
            continue
        try:
            float_parts = [float(part) for part in parts]
            x, y, z = float_parts
            return (x, y, z)
        except ValueError as e:
            error_val = str(e).split(':')[-1].strip()
            print(f"Error on parameter {error_val}: {e}")


def main() -> None:
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist1:.4f}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist2 = math.sqrt((pos2[0] - pos1[0]) ** 2 +
                      (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {dist2:.4f}")


if __name__ == "__main__":
    print("Get a first set of coordinates")
    print()
    main()
