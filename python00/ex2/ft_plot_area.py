# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plot_area.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: raltunda <raltunda@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 19:01:27 by raltunda           #+#    #+#             #
#   Updated: 2026/04/27 21:38:13 by raltunda          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    area = length * width
    print(f"Plot area : {area}")
