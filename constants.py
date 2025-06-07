# Screen settings
PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 + PANEL

# Game states
TITLE_SCREEN = 0
ADVENTURE_MENU = 1
GAMEPLAY = 2

# Button Colors
BUTTON_NORMAL = (120, 120, 120)
BUTTON_HOVER = (200, 200, 200)
BUTTON_TEXT = (255, 255, 255)

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Placeholder dimensions for enemies from Characters
DEFAULT_SIZE = 32
PLACEHOLDER_COLOR = (255, 0, 0)  # Red
ENEMY_SIZE = (64, 64)
# Player size
PLAYER_SIZE = (64, 64)

# Messages
MAX_MESSAGES = 5

# Animation
ANIMATION_SPEED = 0.2  # Adjust as needed

# Elements
ELEMENTS = ["Fire", "Ice", "Wind", "Water", "Light", "Dark", "None"]

# Define elemental weaknesses (element: [weak against])
ELEMENT_WEAKNESSES = {
    "Fire": ["Water", "Ice"],
    "Ice": ["Fire", "Wind"],
    "Wind": ["Ice", "Water"],
    "Water": ["Wind", "Fire"],
    "Light": ["Dark"],
    "Dark": ["Light"],
    "None": []  # Neutral has no specific weaknesses
}

# Damage multipliers
WEAKNESS_MULTIPLIER = 2.0  # Double damage when hitting weakness
RESISTANCE_MULTIPLIER = 0.5  # Half-damage when hitting resistance

# Base stats for enemies
ENEMY_TYPES = {
    "Goblin": {"base_hp": 20, "hp_scale": 5, "base_attack": 5, "attack_scale": 2,
               "base_defense": 2, "defense_scale": 1, "base_xp": 15, "xp_scale": 5, "graphic": "goblin_static"},
    "Orc": {"base_hp": 35, "hp_scale": 8, "base_attack": 8, "attack_scale": 3,
            "base_defense": 4, "defense_scale": 2, "base_xp": 25, "xp_scale": 8, "graphic": "orc_static"},
    "Skeleton": {"base_hp": 25, "hp_scale": 4, "base_attack": 7, "attack_scale": 2,
                 "base_defense": 1, "defense_scale": 1, "base_xp": 20, "xp_scale": 6, "graphic": "skeleton_static"},
    "Wolf": {"base_hp": 15, "hp_scale": 3, "base_attack": 10, "attack_scale": 3,
             "base_defense": 0, "defense_scale": 0, "base_xp": 18, "xp_scale": 4, "graphic": "wolf_static"},
    "Troll": {"base_hp": 50, "hp_scale": 12, "base_attack": 12, "attack_scale": 4,
              "base_defense": 6, "defense_scale": 2, "base_xp": 35, "xp_scale": 10, "graphic": "troll_static"},
    "Dragon": {"base_hp": 100, "hp_scale": 20, "base_attack": 20, "attack_scale": 6,
               "base_defense": 12, "defense_scale": 3, "base_xp": 60, "xp_scale": 15, "graphic": "dragon_static"},
    "Bandit": {"base_hp": 30, "hp_scale": 6, "base_attack": 9, "attack_scale": 3,
               "base_defense": 3, "defense_scale": 1, "base_xp": 22, "xp_scale": 7, "graphic": "bandit_static"},
    "Ghost": {"base_hp": 22, "hp_scale": 5, "base_attack": 14, "attack_scale": 4,
              "base_defense": 2, "defense_scale": 0, "base_xp": 28, "xp_scale": 8, "graphic": "ghost_static"},
    "Witch": {"base_hp": 28, "hp_scale": 6, "base_attack": 15, "attack_scale": 5,
              "base_defense": 3, "defense_scale": 1, "base_xp": 30, "xp_scale": 9, "graphic": "witch_static"},
    "Golem": {"base_hp": 65, "hp_scale": 15, "base_attack": 10, "attack_scale": 3,
              "base_defense": 15, "defense_scale": 4, "base_xp": 40, "xp_scale": 12, "graphic": "golem_static"},
    "Vampire": {"base_hp": 45, "hp_scale": 10, "base_attack": 16, "attack_scale": 5,
                "base_defense": 8, "defense_scale": 2, "base_xp": 38, "xp_scale": 11, "graphic": "vampire_static"},
    "Werewolf": {"base_hp": 40, "hp_scale": 9, "base_attack": 18, "attack_scale": 5,
                 "base_defense": 5, "defense_scale": 2, "base_xp": 32, "xp_scale": 9, "graphic": "werewolf_static"},
    "Minotaur": {"base_hp": 55, "hp_scale": 13, "base_attack": 14, "attack_scale": 4,
                 "base_defense": 9, "defense_scale": 3, "base_xp": 42, "xp_scale": 12, "graphic": "minotaur_static"},
    "Ogre": {"base_hp": 60, "hp_scale": 14, "base_attack": 13, "attack_scale": 4,
             "base_defense": 7, "defense_scale": 2, "base_xp": 38, "xp_scale": 11, "graphic": "ogre_static"},
    "Giant": {"base_hp": 80, "hp_scale": 18, "base_attack": 16, "attack_scale": 5,
              "base_defense": 10, "defense_scale": 3, "base_xp": 45, "xp_scale": 13, "graphic": "giant_static"},
    "Wraith": {"base_hp": 35, "hp_scale": 8, "base_attack": 17, "attack_scale": 5,
               "base_defense": 6, "defense_scale": 2, "base_xp": 36, "xp_scale": 10, "graphic": "wraith_static"},
    "Demon": {"base_hp": 70, "hp_scale": 16, "base_attack": 19, "attack_scale": 5,
              "base_defense": 11, "defense_scale": 3, "base_xp": 50, "xp_scale": 14, "graphic": "demon_static"},
    "Cyclops": {"base_hp": 75, "hp_scale": 17, "base_attack": 15, "attack_scale": 5,
                "base_defense": 8, "defense_scale": 2, "base_xp": 43, "xp_scale": 12, "graphic": "cyclops_static"},
    "Phoenix": {"base_hp": 85, "hp_scale": 19, "base_attack": 18, "attack_scale": 5,
                "base_defense": 9, "defense_scale": 3, "base_xp": 55, "xp_scale": 14, "graphic": "phoenix_static"}
}

# Name prefixes with added xp_scale
NAME_PREFIXES = [
    {"prefix": "", "xp_scale": 0},
    {"prefix": "Hungry ", "xp_scale": 1},
    {"prefix": "Fierce ", "xp_scale": 2},
    {"prefix": "Ancient ", "xp_scale": 3},
    {"prefix": "Young ", "xp_scale": -1},
    {"prefix": "Wild ", "xp_scale": 1},
    {"prefix": "Enraged ", "xp_scale": 2},
    {"prefix": "Corrupted ", "xp_scale": 3},
    {"prefix": "Savage ", "xp_scale": 2}
]

# Enemy name suffixes with added xp_scale
NAME_SUFFIXES = [
    {"suffix": "", "xp_scale": 0},
    {"suffix": " the Terrible", "xp_scale": 3},
    {"suffix": " the Weak", "xp_scale": -2},
    {"suffix": " of the Hills", "xp_scale": 1},
    {"suffix": " of the Forest", "xp_scale": 1},
    {"suffix": " the Destroyer", "xp_scale": 4},
    {"suffix": " the Hunter", "xp_scale": 2}
]

import random

from modules.characters import Enemy


def generate_enemy(x, y, enemy_type, hero_level=1, visual_scale=1.0, stat_multiplier=1.0, enemy_level=None):
    if enemy_type not in ENEMY_TYPES:
        raise ValueError(f"Unknown enemy type: {enemy_type}")
        
    config = ENEMY_TYPES[enemy_type]
    
    # Determine enemy level
    if enemy_level is None:
        enemy_level = max(1, hero_level + random.randint(-2, 2))
    
    # Calculate base stats with level scaling
    hp = config["base_hp"] + (config["hp_scale"] * (enemy_level - 1))
    attack = config["base_attack"] + (config["attack_scale"] * (enemy_level - 1))
    defense = config["base_defense"] + (config["defense_scale"] * (enemy_level - 1))
    base_xp = config["base_xp"] + (config["xp_scale"] * (enemy_level - 1))
    graphic_name = config["graphic"]
    
    # Apply stat multiplier for difficulty adjustment (separate from visual scaling)
    hp = int(hp * stat_multiplier)
    attack = int(attack * stat_multiplier)
    defense = int(defense * stat_multiplier)
    base_xp = int(base_xp * stat_multiplier)
    
    # Generate a name with prefix and suffix
    prefix_data = random.choice(NAME_PREFIXES)
    suffix_data = random.choice(NAME_SUFFIXES)
    
    # Apply name modifications
    prefix = prefix_data["prefix"]
    suffix = suffix_data["suffix"]
    name = f"{prefix}{enemy_type}{suffix}".strip()
    
    # Apply XP modifications from prefix and suffix
    xp_reward = max(1, base_xp + prefix_data["xp_scale"] + suffix_data["xp_scale"])
    
    # Choose element and weakness
    element = random.choice(ELEMENTS)
    if element in ELEMENT_WEAKNESSES:
        weakness = random.choice(ELEMENT_WEAKNESSES[element]) if ELEMENT_WEAKNESSES[element] else "None"
    else:
        weakness = "None"
    
    # Calculate visual scale factor based on enemy vs hero level - separate from stat scaling
    visual_scale_factor = 1.0 + (0.1 * (enemy_level - hero_level))
    visual_scale_factor = max(0.8, min(1.5, visual_scale_factor))  # Limit scale between 0.8 and 1.5
    final_visual_scale = visual_scale * visual_scale_factor
    
    return Enemy(
        x=x,
        y=y,
        name=name,
        level=enemy_level,
        attack=attack,
        defense=defense,
        xp_reward=xp_reward,
        weakness=weakness,
        element=element,
        hp=hp,
        scale=final_visual_scale,  # This is only used for visual scaling now
        graphic=graphic_name
    )