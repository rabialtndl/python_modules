# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_data.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 16:16:58 by raltunda           #+#    #+#             #
#   Updated: 2026/04/28 18:41:59 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.show()

    sunflower = Plant("Sunflower", 80, 45)
    sunflower.show()

    cactus = Plant("Cactus", 15, 120)
    cactus.show()


if __name__ == "__main__":
    main()
