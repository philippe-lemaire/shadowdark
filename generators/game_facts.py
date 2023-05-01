ancestries = ["Dwarf", "Elf", "Goblin", "Half-Orc", "Halfling", "Human"]
classes = ["Fighter", "Priest", "Thief", "Wizard"]
backgrounds = (
    ("Urchin", "You grew up in the merciless streets of a large city"),
    ("Wanted", "There's a price on your head, but you have allies"),
    ("Cult Initiate", "You know blasphemous secrets and rituals"),
    ("Thieves' Guild", "You have connections, contacts, and debts"),
    ("Banished", "Your people cast you out for supposed crimes"),
    ("Orphaned", "An unusual guardian rescued and raised you"),
    ("Wizard's Apprentice", "You have a knack and eye for magic"),
    ("Jeweler", "You can easily appraise value and authenticity"),
    ("Herbalist", "You know plants, medicines, and poisons"),
    ("Barbarian", "You left the horde, but it never quite left you"),
    ("Mercenary", "You fought friend and foe alike for your coin"),
    ("Sailor", "Pirate, privateer, or merchant — the seas are yours"),
    ("Acolyte", "You're well trained in religious rites and doctrines"),
    ("Soldier", "You served as a fighter in an organized army"),
    ("Ranger", "The woods and wilds are your true home"),
    ("Scout", "You survived on stealth, observation, and speed"),
    ("Minstrel", "You've traveled far with your charm and talent"),
    ("Scholar", "You know much about ancient history and lore"),
    ("Noble", "A famous name has opened many doors for you"),
    ("Chirurgeon", "You know anatomy, surgery, and first aid"),
)
stats_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]


talents = (
    # fighter
    {
        2: "Gain Weapon Mastery with one additional weapon",
        3: "+1 to melee and ranged attacks",
        7: "+2 to Strength, Dexterity, or Constitution stat",
        10: "Choose one kind of armor. You get +1 AC from that armor",
        12: "Choose a talent or +2 points to distribute to stats",
    },
    # priest
    {
        2: "Gain advantage on casting one spell you know",
        3: "+1 to melee or ranged attacks",
        7: "+1 to priest spellcasting checks",
        10: "+2 to Strength or Wisdom stat",
        12: "Choose a talent or +2 points to distribute to stats",
    },
    # thief
    {
        2: "Gain advantage on initiative rolls (reroll if duplicate)",
        3: "Your Backstab deals +1 dice of damage",
        6: "+2 to Strength, Dexterity, or Charisma stat",
        10: "+1 to melee and ranged attacks",
        12: "Choose a talent or +2 points to distribute to stats",
    },
    # wizard
    {
        2: "Make 1 random magic item of a type you choose (pg. 282)",
        3: "+2 to Intelligence stat or +1 to wizard spellcasting checks",
        8: "Gain advantage on casting one spell you know",
        10: "Learn one additional wizard spell of any tier you know",
        12: "Choose a talent or +2 points to distribute to stats",
    },
)

talents_dict = {cl: talent for cl, talent in zip(classes, talents)}
