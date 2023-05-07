import pygame


class Button:
    def __init__(
        self, x=0, y=0, width=10, height=10,
        text='Default', text_color=(240, 240, 240),
        normal_color=(0, 0, 0), hover_color=(50, 50, 50),
        font_size=20, font_family='Arial', center_x=True
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font_family = font_family
        w_width, w_height = pygame.display.get_window_size()
        if center_x:
            window_rect = pygame.Rect(0, 0, w_width, w_height)
            self.rect.centerx = window_rect.centerx
        self.is_hovered = False
        self.font = pygame.font.SysFont(font_family, font_size)
    
    def draw(self, window):
        image = self.font.render(self.text, True, self.text_color)
        image_rect = image.get_rect()
        image_rect.center = self.rect.center
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.normal_color
        pygame.draw.rect(window, color, self.rect)
        window.blit(image, (image_rect.x, image_rect.y))

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.is_hovered = True
                    break
                else:
                    self.is_hovered = False

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((600, 400))
    window.fill((253, 199, 255))
    clock = pygame.time.Clock()

    btn_start = Button(y=200, width=150, height=40, text='Start')
    btn_exit = Button(y=250, width=150, height=40, text='Exit')

    game = True
    while game:
        window.fill((253, 199, 255))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game = False
        
        btn_start.draw(window)
        btn_start.update(events)
        if btn_start.is_clicked(events):
            print('Игра начинается')

        btn_exit.draw(window)
        btn_exit.update(events)
        if btn_exit.is_clicked(events):
            print('Конец!')

        clock.tick(60)
        pygame.display.update()
