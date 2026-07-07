# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/05/01 20:55:38 by raltunda           #+#    #+#             #
#   Updated: 2026/05/03 16:44:46 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count = self._grow_count + 1

        def record_age(self) -> None:
            self._age_count = self._age_count + 1

        def record_show(self) -> None:
            self._show_count = self._show_count + 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, amount: float) -> None:
        self.set_height(self._height + amount)
        self._stats.record_grow()

    def age(self, days: int) -> None:
        self.set_age(self._age + days)
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(plnt) -> 'Plant':
        return plnt("Unknown", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self._stats: Tree.Stats = self.Stats()
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose.name}]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.name}]")
    display_statistics(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.name}]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    display_statistics(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower.name}]")
    display_statistics(sunflower)
    print("")
    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    print(f"[statistics for {anon.name} plant]")
    display_statistics(anon)


if __name__ == "__main__":
    main()
