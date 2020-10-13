import math, sys, os

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    totalCost = meal_cost + tip + tax
    float_value=totalCost-math.floor(totalCost)
    if float_value>.5:
      totalCost += 1
    return int(totalCost)

if __name__ == "__main__":
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))