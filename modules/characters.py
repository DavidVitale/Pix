import pygame
import os
from constants import (WEAKNESS_MULTIPLIER, DEFAULT_SIZE, PLACEHOLDER_COLOR,
                       ENEMY_TYPES, NAME_PREFIXES, NAME_SUFFIXES, ELEMENTS, ELEMENT_WEAKNESSES,
                       )
import random

class Hero:
    def __init__(self, x, y, name, level=1, hp=100, attack=10, defense=5, scale=1.0):
        self.x = x
        self.y = y
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = 0
        self.gold = 0
        self.scale = scale
        # Add other attributes as needed

    def update(self):
        # Update logic
        pass

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def gain_experience(self, amount):
        self.experience += amount
        # Level up logic

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)


class EnemyStats:
    """Handles all enemy stats and combat-related functionality"""
    def __init__(self, name, level, attack, defense, xp_reward, weakness, element, hp=50):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.weakness = weakness
        self.element = element
        self.hp = hp
        self.max_hp = hp

    def take_damage(self, amount, attack_element="NEUTRAL"):
        damage_multiplier = 1.0

        if attack_element in self.weakness:
            damage_multiplier = WEAKNESS_MULTIPLIER

        actual_damage = max(0, int((amount - self.defense) * damage_multiplier))
        self.hp = max(0, self.hp - actual_damage)

        return actual_damage, damage_multiplier > 1.0

    def is_alive(self):
        return self.hp > 0

class EnemyRenderer:
    """Handles enemy visual representation and graphical scaling"""
    def __init__(self, x, y, graphic, visual_scale=1.0):
        self.x = x
        self.y = y
        self.graphic = graphic
        self.visual_scale = visual_scale
        self.image = None
        self.rect = None

    def load_graphic(self, player_size=None):
        from constants import PLAYER_SIZE

        if player_size is None:
            player_size = PLAYER_SIZE

        def create_placeholder(width, height, label=None,color=PLACEHOLDER_COLOR):
            """Create a placeholder surface with the given dimensions and color"""
            surface = pygame.Surface((width, height))
            surface.fill(color)
            # Add text label if provided
            if label:
                font = pygame.font.SysFont('Arial', 12)
                text = font.render(label, True, (255, 255, 255))
                text_rect = text.get_rect(center=(width / 2, height / 2))
                surface.blit(text, text_rect)

            return surface

        def load_and_scale_image(path, width, height):
            """Load and scale an image, returning the loaded image or a placeholder on failure"""
            try:
                loaded_image = pygame.image.load(path).convert_alpha()
                return pygame.transform.scale(loaded_image, (width, height))
            except (pygame.error, FileNotFoundError) as e:
                print(f"Error loading image from {path}: {e}")
                return create_placeholder(width, height)
            except Exception as e:
                print(f"Unexpected error loading image: {type(e).__name__}: {e}")
                return create_placeholder(width, height)

        # Try to load the main graphic file
        image_path = os.path.join("mob", f"{self.graphic}.png")

        try:
            # Get original dimensions to calculate scaled size
            temp_image = pygame.image.load(image_path).convert_alpha()
            original_width = temp_image.get_width()
            original_height = temp_image.get_height()
            new_width = int(original_width * self.visual_scale)
            new_height = int(original_height * self.visual_scale)

            # Now use the helper function to load and scale
            self.image = load_and_scale_image(image_path, new_width, new_height)
        except (pygame.error, FileNotFoundError) as e:
            print(f"Error loading graphic for {self.graphic}.png: {e}")
            # Create a placeholder with the scaled default size
            self.image = create_placeholder(int(DEFAULT_SIZE * self.visual_scale), int(DEFAULT_SIZE * self.visual_scale))

        # Set the rect property for positioning
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        """Draws the enemy on the given Pygame surface."""
        if self.image and self.rect:
            # Blit the image using its rect for positioning
            surface.blit(self.image, self.rect)
        else:
            # This case should ideally not be reached if load_graphic has a fallback
            pygame.draw.rect(surface, (255, 0, 255), (self.x, self.y, 30, 30))  # Magenta

    def update_position(self):
        """Updates the rect position based on x and y coordinates"""
        if self.rect:
            self.rect.topleft = (self.x, self.y)

class Enemy:
    """Main enemy class that composes stats and visual components"""
    def __init__(self, x, y, name, level, attack, defense, xp_reward, weakness, element, graphic, hp=50, scale=1.0):
        # Create component objects
        self.stats = EnemyStats(
            name=name,
            level=level,
            attack=attack,
            defense=defense,
            xp_reward=xp_reward,
            weakness=weakness,
            element=element,
            hp=hp
        )
        
        self.renderer = EnemyRenderer(
            x=x,
            y=y,
            graphic=graphic,
            visual_scale=scale
        )
        
    # Property getters to maintain backward compatibility
    @property
    def name(self):
        return self.stats.name
        
    @property
    def level(self):
        return self.stats.level
    
    @property
    def hp(self):
        return self.stats.hp
    
    @hp.setter
    def hp(self, value):
        self.stats.hp = value
        
    @property
    def max_hp(self):
        return self.stats.max_hp
        
    @property
    def attack(self):
        return self.stats.attack
        
    @property
    def defense(self):
        return self.stats.defense
        
    @property
    def xp_reward(self):
        return self.stats.xp_reward
        
    @property
    def weakness(self):
        return self.stats.weakness
        
    @property
    def element(self):
        return self.stats.element
        
    @property
    def x(self):
        return self.renderer.x
        
    @x.setter
    def x(self, value):
        self.renderer.x = value
        self.renderer.update_position()
        
    @property
    def y(self):
        return self.renderer.y
        
    @y.setter
    def y(self, value):
        self.renderer.y = value
        self.renderer.update_position()
        
    @property
    def image(self):
        return self.renderer.image
        
    @property
    def rect(self):
        return self.renderer.rect
    
    @property
    def graphic(self):
        return self.renderer.graphic
        
    # Delegate method calls to the appropriate component
    def load_graphic(self, player_size=None):
        self.renderer.load_graphic(player_size)
        
    def draw(self, surface):
        self.renderer.draw(surface)
        
    def update(self):
        self.renderer.update_position()
        
    def take_damage(self, amount, attack_element="NEUTRAL"):
        return self.stats.take_damage(amount, attack_element)
        
    def is_alive(self):
        return self.stats.is_alive()

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