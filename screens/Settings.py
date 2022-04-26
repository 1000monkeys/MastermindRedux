from helpers.Screen import Screen


class Settings(Screen):
    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager

        self.background_image = pygame.transform.scale(
            pygame.image.load("assets/enigma.jpg"),
            (1024, 786)
        )

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        """
        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()
        """
        pass
        
    def handle_events(self, events):
        super().handle_events(events)
        """
        for key in self.buttons.keys():
        """
        # for event in events:
        pass
