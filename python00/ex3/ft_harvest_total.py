# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 19:06:51 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:38:17 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total_harvest = day1 + day2 + day3
    print(f"Total harvest : {total_harvest}")
