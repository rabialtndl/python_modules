# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_into.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 16:16:03 by raltunda           #+#    #+#             #
#   Updated: 2026/04/28 18:18:54 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print(" ")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
