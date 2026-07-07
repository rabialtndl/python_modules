# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 20:35:44 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:43:45 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{name} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{name} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{name} seeds: {quantity} square meters")
    else:
        print("Unknown unit type")
