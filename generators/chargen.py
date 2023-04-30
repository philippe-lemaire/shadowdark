from .dice_tools import roll


def roll_stats():
    stats_name = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    stats_rolled = [roll("3d6") for _ in range(6)]

    stats = {k: v for k, v in zip(stats_name, stats_rolled)}
    return stats, sum(stats_rolled)
