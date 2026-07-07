# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 19:39:26 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:43:35 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive(n=None, day=1):
    if (n is None):
        n = int(input("Days until harvest: "))

    if (day > n):
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(n, day + 1)
