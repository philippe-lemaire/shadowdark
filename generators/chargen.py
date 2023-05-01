from .dice_tools import roll
from .game_facts import classes, ancestries, backgrounds, stats_names
import random


def roll_stats():
    stats_rolled = [roll("3d6") for _ in range(6)]

    stats = {k: v for k, v in zip(stats_names, stats_rolled)}
    return stats, sum(stats_rolled)


class PC_Character:
    def __init__(self, stats_d, ancestry, background, class_):
        # stats
        for stat_name, value in stats_d.items():
            setattr(self, stat_name, value)
            setattr(self, f"{stat_name}_MOD", (value - 10) // 2)
        self.ancestry = ancestries[ancestry]
        self.background, self.background_description = backgrounds[background]
        self.class_ = classes[class_]
        # level
        self.level = 1
        # hp
        self.roll_hp()

    def roll_hp(self):
        if self.level == 0:
            rolled_hp = max(1, self.CON_MOD)
            if self.ancestry == "Dwarf":
                rolled_hp += 2

        else:
            classes_hit_dice = ["d8", "d6", "d4", "d4"]
            classes_d = {cl: hd for cl, hd in zip(classes, classes_hit_dice)}
            hd = classes_d.get(self.class_)

            if self.ancestry == "Dwarf":
                rolled_hp = max(1, roll(hd, advantage=True) + self.CON_MOD) + 2
            else:
                rolled_hp = max(1, roll(hd) + self.CON_MOD)
        print(rolled_hp)
        self.hp = rolled_hp

    def __repr__(self):
        return f"""{self.background} level {self.level} {self.ancestry} {self.class_} character with {self.hp} Hit Points.\n{[f"{attr}: {getattr(self, attr)}" for attr in stats_names]}"""


class NPC_Character(PC_Character):
    def __init__(self, level=0, ancestry=None):
        # Level
        self.level = level
        # Stats generation

        rolled_values = [roll("3d6") for _ in range(6)]
        for stat, rolled_value in zip(stats_names, rolled_values):
            setattr(self, stat, rolled_value)
            setattr(self, f"{stat}_MOD", (rolled_value - 10) // 2)

        # ancestry

        if ancestry is None:
            self.ancestry = random.choice(ancestries)
        # class

        if self.level == 0:
            self.class_ = "Peasant"
        else:
            self.class_ = random.choice(classes)
        # HP
        self.roll_hp()

        # background

        self.background, self.background_description = random.choice(backgrounds)
