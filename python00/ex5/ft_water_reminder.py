# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 19:15:42 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:42:01 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    water = int(input("Days since last watering: "))
    if (water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
