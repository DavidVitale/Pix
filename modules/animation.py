import pygame


class Animation:
    def __init__(self, sprite_sheet, sprite_width, sprite_height, num_sprites, scale=1.0):
        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.2
        self.frame_timer = 0

        # Extract frames from a sprite sheet
        for i in range(num_sprites):
            original_frame = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            original_frame.blit(sprite_sheet, (0, 0),
                                (i * sprite_width, 0, sprite_width, sprite_height))

            # Scale if needed
            if scale != 1.0:
                new_width = int(sprite_width * scale)
                new_height = int(sprite_height * scale)
                scaled_frame = pygame.transform.scale(original_frame, (new_width, new_height))
                self.frames.append(scaled_frame)
            else:
                self.frames.append(original_frame)

    def update(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def draw(self, screen, x, y):
        screen.blit(self.get_current_frame(), (x, y))


def load_animation(path, sprite_width, sprite_height, num_sprites, scale=1.0):
    sprite_sheet = pygame.image.load(path).convert_alpha()
    return Animation(sprite_sheet, sprite_width, sprite_height, num_sprites, scale)

# def create_enemy_placeholder(enemy_type, size=(64, 64), color=(255, 0, 0)):
#     surface = pygame.Surface(size, pygame.SRCALPHA)
#     width, height = size
#     pygame.draw.rect(surface, color, (0, 0, width, height))
#     # Add text to placeholder
#     font = pygame.font.SysFont('Arial', 12)
#     text = font.render(enemy_type, True, (255, 255, 255))
#     text_rect = text.get_rect(center=(width / 2, height / 2))
#     surface.blit(text, text_rect)

    return surface