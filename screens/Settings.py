from helpers.Container import Container
from helpers.Screen import Screen
from helpers.TextDisplay import TextDisplay


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

        items = list()
        items.append(
            TextDisplay(
                screen,
                text="Optie menu:",
                #text="Welcome to Mastermind, Challenge your brain!",
                position=(10, 10),
                text_color=(255, 255, 255),
                background_color=None,
                border_color=None,
                font_size=48,
                padding=10
            )
        )
        items.append(
            TextDisplay(
                screen,
                text="Taal:",
                position=(40, 150),
                font_size=36,
            )
        )
        self.container = Container(
            pygame,
            screen,
            items,
            (55, 42, 34),
            (255, 255, 255),
            15
        )

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.container.draw()
        """
        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()
        """
        
    def handle_events(self, events):
        super().handle_events(events)
        """
        for key in self.buttons.keys():
        """
        # for event in events:
        pass
