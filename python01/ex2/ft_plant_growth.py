# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 18:21:01 by raltunda           #+#    #+#             #
#   Updated: 2026/04/28 19:10:20 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.ages = self.ages + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    rose.show()
    first_height = rose.height

    for i in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {i} ===")
        rose.show()

    growth_this_week = round(rose.height - first_height, 1)
    print(f"Growth this week: {growth_this_week}cm")


if __name__ == "__main__":
    main()
