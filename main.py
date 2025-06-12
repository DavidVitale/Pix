import os
import random
import sys

import pygame

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PANEL, WHITE,
    TITLE_SCREEN, ADVENTURE_MENU, GAMEPLAY
)
from constants import ENEMY_TYPES
from constants import generate_enemy
from modules.animation import load_animation
from modules.characters import Hero
from modules.game_states import TitleScreen, AdventureMenu, Gameplay
from modules.messages import MessageSystem


def main():
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Pix")

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize clock
    clock = pygame.time.Clock()
    fps = 60

    # Initialize fonts
    title_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 36)

    # Load images
    title_img = pygame.image.load(os.path.join("assets", "title1.png")).convert_alpha()

    # Random backgrounds
    background_images = ["a1.png", "a2.png", "a3.png", "a4.png", "b1.png", "b2.png", "b3.png", "b4.png"]
    random_bg = random.choice(background_images)
    # Load and scale the background
    game_background = pygame.image.load(os.path.join("assets", random_bg)).convert_alpha()
    original_width = game_background.get_width()
    original_height = game_background.get_height()
    game_background = pygame.transform.scale(game_background,
                                             (original_width // 3, original_height // 3))


    adventure_background = pygame.image.load(os.path.join("assets", "adventure_menu.png")).convert_alpha()
    adventure_background = pygame.transform.scale(adventure_background, (SCREEN_WIDTH, SCREEN_HEIGHT + PANEL))
    stat_panel_img = pygame.image.load(os.path.join("assets", "panel.png")).convert_alpha()
    adventure_panel_img = pygame.image.load(os.path.join("assets", "adventure_panel.png")).convert_alpha()

    # Load animations
    hero_animation = load_animation(
        os.path.join("assets", "hero_idle.png"),
        64, 64, 4, 3.5
    )

    enemy_animation = load_animation(
        os.path.join("assets", "fly_idle.png"),
        64, 64, 1, 3.5
    )

    # Initialize a message system
    message_system = MessageSystem()
    # Initialize characters
    hero = Hero(SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2 - 50, "player")

    # Choose a random enemy type from the available types
    enemy_type = random.choice(list(ENEMY_TYPES.keys()))
    enemy = generate_enemy(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, enemy_type=enemy_type)
    enemy.load_graphic(player_size=None)


    def print_enemy_stats(enemy):
        """Print enemy stats safely."""
        if enemy:
            print(f"Enemy Name: {enemy.name}")
            print(f"Level: {enemy.level}")
            print(f"Hp: {enemy.hp}/{enemy.max_hp}")
            print(f"Attack: {enemy.attack}")
            print(f"Defense: {enemy.defense}")
            print(f"Xp_reward: {enemy.xp_reward}")
            print(f"Weakness: {enemy.weakness}")
            print(f"Element: {enemy.element}")
            print(f"Position: ({enemy.x}, {enemy.y})")
        else:
            print("Enemy is None")

    print_enemy_stats(enemy)



    # Initialize game states
    title_screen = TitleScreen(screen, title_font, button_font, title_img)
    adventure_menu = AdventureMenu(screen, button_font, adventure_background, adventure_panel_img, message_system)
    gameplay = Gameplay(screen, hero, enemy, button_font, game_background, stat_panel_img, message_system)

    # Set the initial game state
    current_game_state = TITLE_SCREEN



    # Game loop
    running = True
    while running:
        # Time delta for smooth animations
        dt = clock.tick(fps) / 1000.0

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle events based on the current game state
            if current_game_state == TITLE_SCREEN:
                result = title_screen.handle_event(event)
                if result is not None:
                    current_game_state = result

            elif current_game_state == ADVENTURE_MENU:
                result = adventure_menu.handle_event(event)
                if result is not None:
                    current_game_state = result

            elif current_game_state == GAMEPLAY:
                result = gameplay.handle_event(event)
                if result is not None:
                    current_game_state = result


        # Update based on current game state
        if current_game_state == TITLE_SCREEN:
            title_screen.update(mouse_pos)

        elif current_game_state == ADVENTURE_MENU:
            adventure_menu.update(mouse_pos)

        elif current_game_state == GAMEPLAY:
            gameplay.update(mouse_pos)
            hero_animation.update(dt)
            # enemy_animation.update(dt)

        # Draw based on the current game state
        if current_game_state == TITLE_SCREEN:
            title_screen.draw()

        elif current_game_state == ADVENTURE_MENU:
            adventure_menu.draw()

        elif current_game_state == GAMEPLAY:
            gameplay.draw()

            enemy_x_pos = SCREEN_WIDTH // 2 + 75
            enemy_y_pos = SCREEN_HEIGHT // 2 - 100
            if hasattr(enemy, 'image') and enemy.image is not None:
                screen.blit(enemy.image, (enemy_x_pos, enemy_y_pos))
            else: print('Enemy image not loaded properly')

            # Render and display only the enemy name
            font = pygame.font.SysFont(None, 30)
            name_text = font.render(f"{enemy.name}", True, WHITE)  # Removed "Name:" prefix

            # Position the text above the rectangle
            name_pos = (SCREEN_WIDTH // 2 + 200 - name_text.get_width() // 2, SCREEN_HEIGHT // 2 - 150)

            # Draw only the name text
            screen.blit(name_text, name_pos)



            # Draw hero and enemy animations
            hero_animation.draw(screen, hero.x - 64, hero.y - 64)
            enemy_animation.draw(screen, enemy.x + 170, enemy.y - 64)

        # Update the display
        pygame.display.flip()



    # Quit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()