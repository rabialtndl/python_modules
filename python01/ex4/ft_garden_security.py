# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 19:30:37 by raltunda           #+#    #+#             #
#   Updated: 2026/04/28 22:44:39 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0

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

    def show(self) -> None:
        print(
            f"Current state: {self.name}: "
            f"{round(self._height, 1)}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.name}: 15.0cm, 10 days old")
    print("")

    rose.set_height(25.0)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    print("")

    rose.set_height(-5.0)
    rose.set_age(-1)

    print("")
    rose.show()


if __name__ == "__main__":
    main()
