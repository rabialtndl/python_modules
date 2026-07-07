# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_age.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 19:10:18 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:40:16 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    plant_age = int(input("Enter plant age in days : "))
    if (plant_age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
