import pygame

from constants import TITLE_SCREEN, ADVENTURE_MENU, GAMEPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from modules.ui import Button, draw_stat_panel, draw_message_panel


class TitleScreen:
    def __init__(self, screen, title_font, button_font, title_img):
        self.screen = screen
        self.title_font = title_font
        self.button_font = button_font
        self.title_img = title_img
        self.instructions_showing = False
        self.instruction_text = [
            "Welcome to Truxican Standoff!",
            "A Simple Demo",
            "Level Up and Explore",
            "Scratch The RPG Itch",
            "Have fun!"
        ]

        # Create buttons
        center_x = SCREEN_WIDTH // 2
        self.start_button = Button(center_x - 100, 300, 200, 50, "Start Game", button_font,
                                   lambda: ADVENTURE_MENU)
        self.instruction_button = Button(center_x - 100, 370, 200, 50, "Instructions", button_font,
                                         self.toggle_instructions)
        self.quit_button = Button(center_x - 100, 440, 200, 50, "Quit Game", button_font,
                                  self.quit_game)
        self.back_button = Button(center_x - 100, 470, 200, 50, "Back", button_font,
                                  self.toggle_instructions)

    def toggle_instructions(self):
        self.instructions_showing = not self.instructions_showing
        return None

    def quit_game(self):
        pygame.quit()
        exit()

    def update(self, mouse_pos):
        self.start_button.update(mouse_pos)
        self.instruction_button.update(mouse_pos)
        self.quit_button.update(mouse_pos)
        if self.instructions_showing:
            self.back_button.update(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.instructions_showing:
                result = self.back_button.handle_event(event)
                if result is not None:
                    return result
                # If instructions are showing, don't process other buttons
                return None

            result = self.start_button.handle_event(event)
            if result is not None:
                return result

            result = self.instruction_button.handle_event(event)
            if result is not None:
                return result

            result = self.quit_button.handle_event(event)
            if result is not None:
                return result
        return None

    def draw(self):
        # Draw background
        self.screen.blit(self.title_img, (0, 0))

        # Draw title
        title_text = self.title_font.render("Truxican Standoff", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title_text, title_rect)

        # Draw buttons+
        self.start_button.draw(self.screen)
        self.instruction_button.draw(self.screen)
        self.quit_button.draw(self.screen)

        # Draw instructions if showing
        if self.instructions_showing:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0,0))

            y_offset = SCREEN_HEIGHT // 3
            for line in self.instruction_text:
                text_surface = self.button_font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
                self.screen.blit(text_surface, text_rect)
                y_offset += 40

            # Back button
            self.back_button.draw(self.screen)


class AdventureMenu:
    def __init__(self, screen, button_font, background_img, adventure_panel_img, message_system):
        self.screen = screen
        self.button_font = button_font
        self.background_img = background_img
        self.adventure_panel_img = adventure_panel_img
        self.message_system = message_system

        # Create adventure buttons
        self.adventure_buttons = [
            Button(SCREEN_WIDTH / 3, 200, 200, 50, "Explore", button_font, lambda: self.start_adventure("forest")),
            Button(SCREEN_WIDTH / 3, 260, 200, 50, "Shop", button_font, lambda: self.start_adventure("cave")),
            Button(SCREEN_WIDTH / 3, 320, 200, 50, "Rest", button_font, lambda: self.start_adventure("mountain")),
            Button(SCREEN_WIDTH / 3, 380, 200, 50, "Back", button_font, lambda: TITLE_SCREEN)
        ]

    def start_adventure(self, location, player_level=1):
        self.message_system.add_adventure_message(f"You head out to explore! {location}...")

        return GAMEPLAY


    def update(self, mouse_pos):
        for button in self.adventure_buttons:
            button.update(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.adventure_buttons:
                result = button.handle_event(event)
                if result is not None:
                    return result
        return None

    def draw(self):
        # Draw background
        self.screen.blit(self.background_img, (0, 0))

        # Draw adventure panel
        panel_rect = self.adventure_panel_img.get_rect(topleft=(100, 550))
        self.screen.blit(self.adventure_panel_img, panel_rect)

        # Draw title
        title_text = self.button_font.render("Town", True, (BLACK))
        title_rect = title_text.get_rect(center=(375, 175))
        self.screen.blit(title_text, title_rect)

        # Draw buttons
        for button in self.adventure_buttons:
            button.draw(self.screen)

        # Draw messages
        draw_message_panel(self.screen, self.message_system.get_adventure_messages(),
                           self.button_font, 100, 550, 600, 250)


class Gameplay:
    def __init__(self, screen, hero, enemy, button_font, background_img, stat_panel_img, message_system):
        self.screen = screen
        self.hero = hero
        self.enemy = enemy
        self.button_font = button_font
        self.background_img = background_img
        self.stat_panel_img = stat_panel_img
        self.message_system = message_system
        self.font = pygame.font.Font(None, 36)


        # Create gameplay buttons
        self.action_buttons = [
            Button(20, 550, 150, 50, "Attack", button_font, self.attack),
            Button(220, 550, 150, 50, "Defend", button_font, self.defend),
            Button(420, 550, 150, 50, "Use Item", button_font, self.use_item),
            Button(620, 550, 150, 50, "Run Away", button_font, lambda: ADVENTURE_MENU)
        ]


    def attack(self):
        # Attack logic
        damage = max(1, self.hero.attack - self.enemy.defense // 2)

        if isinstance(self.enemy.hp, str):
            self.enemy.hp = int(self.enemy.hp)

        self.enemy.hp -= damage
        self.message_system.add_hero_message(f"You hit {self.enemy.name} for {damage} damage!")

        if not self.enemy.is_alive():
            self.message_system.add_hero_message("Enemy defeated!")
            self.hero.gain_experience(20)
            return ADVENTURE_MENU

        # Enemy counterattack
        enemy_damage = self.enemy.attack
        actual_enemy_damage = self.hero.take_damage(enemy_damage)
        self.message_system.add_hero_message(f"Enemy attacks for {actual_enemy_damage} damage!")

        if not self.hero.is_alive():
            self.message_system.add_hero_message("You have been defeated!")
            return TITLE_SCREEN

        return None

    def defend(self):
        # Temporarily increase defense
        original_defense = self.hero.defense
        self.hero.defense += 5
        self.message_system.add_hero_message("You take a defensive stance!")

        # Enemy attack with reduced damage
        enemy_damage = self.enemy.attack
        actual_enemy_damage = self.hero.take_damage(enemy_damage)
        self.message_system.add_hero_message(f"Enemy attacks for {enemy_damage} damage!")

        # Reset defense
        self.hero.defense = original_defense

        if not self.hero.is_alive():
            self.message_system.add_hero_message("You have been defeated!")
            return TITLE_SCREEN

        return None

    def use_item(self):
        # Placeholder for item usage
        self.hero.heal(20)
        self.message_system.add_hero_message("You used a healing potion! +20 HP")
        return None

    def update(self, mouse_pos):
        for button in self.action_buttons:
            button.update(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.action_buttons:
                result = button.handle_event(event)
                if result is not None:
                    return result
        return None

    def draw(self):
        # Draw background
        self.screen.blit(self.background_img, (0, 0))
        # Draw stat panel
        draw_stat_panel(self.screen, self.hero, self.enemy, self.stat_panel_img, self.button_font)

        # Draw action buttons
        for button in self.action_buttons:
            button.draw(self.screen)

        # Draw messages
        draw_message_panel(self.screen, self.message_system.get_hero_messages(),
                           self.button_font, 0, 600, 800, 150)
        # draw_message_panel(self.screen, self.message_system.get_enemy_messages(),
        #                    self.button_font, 400, 600, 400, 150)