import random


def roll(dice, advantage=False, disadvantage=False):
    """Ex usage roll('3d6') -> random number between 3 and 18.
    roll('d20', advantage=True) -> rolls 2d20, returns the highest.
    roll('d10' disadvantage=True) -> rolls 2d10, returns the lowest"""
    error_message = "Invalid argument. Please use a string such as '2d20' or '3d6'"
    dice = dice.lower()
    if "d" not in dice:
        raise ValueError(error_message)
    if dice.startswith("d"):
        n = 1
        dice_type = int(dice.split("d")[1])
    else:
        n, dice_type = dice.split("d")
        n = int(n)
        dice_type = int(dice_type)
    if (advantage ^ disadvantage) and n == 1:
        n = 2
    rolls = [random.randint(1, dice_type) for _ in range(n)]
    print(rolls)
    if advantage and not disadvantage:
        return max(rolls)
    if disadvantage and not advantage:
        return min(rolls)
    return sum(rolls)


def get_closest_key(rolled_value, d):
    "Returns the closest value in a table based on a rolled value"
    for key in d.keys():
        if key >= rolled_value:
            return d[key]
    return None
