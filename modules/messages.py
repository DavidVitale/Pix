from collections import deque

from constants import MAX_MESSAGES


class MessageSystem:
    def __init__(self):
        self.hero_messages = deque(maxlen=MAX_MESSAGES)
        # self.enemy_messages = deque(maxlen=MAX_MESSAGES)
        self.adventure_messages = deque(maxlen=MAX_MESSAGES)

    def add_hero_message(self, message):
        self.hero_messages.append(message)

    # def add_enemy_message(self, message):
    #     self.enemy_messages.append(message)

    def add_adventure_message(self, message):
        self.adventure_messages.append(message)

    def get_hero_messages(self):
        return list(self.hero_messages)

    # def get_enemy_messages(self):
    #     return list(self.enemy_messages)

    def get_adventure_messages(self):
        return list(self.adventure_messages)

    def clear_all_messages(self):
        self.hero_messages.clear()
        # self.enemy_messages.clear()
        self.adventure_messages.clear()