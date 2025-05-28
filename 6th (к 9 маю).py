import pygame
import time
import random
import os

pygame.init()
pygame.font.init()

score = 0
current_vopr = 0
prav_otv = 0
vopr_all = 2
otvetili = False
end = False
vopr_nomr = 0
rezult = "ОШИБКА"
rezult_color = pygame.Color(105, 0, 198)
tim = 0
secl = 0
min = 0
past = 0

pygame.display.set_caption(f"викторина | вопрос №{vopr_nomr + 1} | очки: {score}")
window_surface = pygame.display.set_mode((700, 500))
background = pygame.Surface((700, 500))
background.fill(pygame.Color(168, 141, 138))

class vopr:
    def __init__(self, question, prav_otv, otv1, otv2, size, img):
        self.question = question
        self.prav_otv = prav_otv
        self.pic = pygame.image.load(img)
        self.pic = pygame.transform.scale(self.pic, (490,260))
        self.text = pygame.font.SysFont('Comic Sans MS', size)
        self.otvs = [
            otv1,
            otv2,
            prav_otv
        ]
        
class button():
    text: str
    def __init__(self, button_color, button_rect, button_text):
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.rect = button_rect
        self.color = button_color
        self.text = button_text
    
    def render(self):
        button_text = self.font.render(self.text, True, (250,250,250))
        pygame.draw.rect(window_surface, self.color, self.rect)
        button_rect_center = button_text.get_rect(center= self.rect.center)
        window_surface.blit(button_text, button_rect_center)

pygame.time.get_ticks
vopr1 = vopr("Когда началась Великая Отечественная война?","в 1941", "в 1945", "в 1940", 26, 'victorina_1.jpg')
vopr2 = vopr("Когда закончалась Великая Отечественная война?", "в 1945", "в 1941", "в 1944", 24, 'victorina_2.jpg')
vopr3 = vopr("Сколько дней длилась Блокада Ленинграда?", "875д", "870д", "800д", 27, 'victorina_1.jpg')
vopr4 = vopr("Когда началась Блокада Ленинграда?", "8 сент.", "6 сент.", "1 сент.", 30, 'victorina_1.jpg')
vopr5 = vopr("В какой день началась Великая Отечественная война?", "22 июн.", "9 сент.", "8 мая", 22, 'victorina_1.jpg')
vopr6 = vopr("Когда началась битва за Ленинград?", "10 июл.", "10 июн.", "10 сент.", 30, 'victorina_1.jpg')
vopr7 = vopr("Как называлась крепость, оборонявшаяся в первые дни войны?", "Брестская", "Познань", "Выборг", 19, 'victorina_3.jpg')
vopr8 = vopr("Когда открылся второй фронт?", "в 1944", "в 1942", "в 1941", 30, 'victorina_1.jpg')
vopr9 = vopr("Кто был главнокомандующим во время ВОВ?", "Сталин", "Талалихин", "Журавлёв", 27, 'victorina_5.jpg')
vopr10 = vopr("Где было самое большое танковое сражение?", "Прохоровка", "Щелково", "Устье", 27, 'victorina_1.jpg')
vopr11 = vopr("Какой город стал принадлежать России после ВОВ?", "Кёнигсберг", "Новгород", "Крым", 24, 'victorina_1.jpg')
vopr12 = vopr("Кто был союзником для СССР?", "США", "Япония", "Швеция", 30, 'victorina_4.jpg')
vopr13 = vopr("Какая тактика характерна для отечественных воен?", "партизанст.", "засады", "налёты", 24, 'victorina_7.jpg')
vopr14 = vopr("Какой тактикой пользовались немецкие захватчики?", "блицкриг", "лож. наступ", "Фабиева", 22, 'victorina_7.jpg')
vopr15 = vopr("Сколько дней длилась Великая Отечественная война?", "1418", "875", "1014", 22, 'victorina_1.jpg')

voprs = [
    vopr1,
    vopr2,
    vopr3,
    vopr4,
    vopr5,
    vopr6,
    vopr7,
    vopr8,
    vopr9,
    vopr10,
    vopr11,
    vopr12,
    vopr13,
    vopr14,
    vopr15
]

current_vopr = random.choice(voprs)
prav_otv = current_vopr.prav_otv
current_otvs = [
    current_vopr.otvs[0],
    current_vopr.otvs[1],
    current_vopr.otvs[2],
]
random.shuffle(current_otvs)
otv1 = current_otvs[0]
otv2 = current_otvs[1]
otv3 = current_otvs[2]

button1 = button(pygame.Color(90,90,90), pygame.Rect(90,355,110,50), str(otv1))
button2 = button(pygame.Color(70,70,70), pygame.Rect(290,355,110,50), str(otv2))
button3 = button(pygame.Color(80,80,80), pygame.Rect(490,355,110,50), str(otv3))

score_font = pygame.font.SysFont('Comic Sans MS', 20)
total_font = pygame.font.SysFont('Comic Sans MS', 40)
tim_font = pygame.font.SysFont('Comic Sans MS', 30)

vopros_surface = current_vopr.text.render(current_vopr.question, False, (0, 0, 0))

clock = pygame.time.Clock()
counter = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.USEREVENT: 
            counter += 1
        elif end == True:
            background.fill(pygame.Color(10,10,10))
            pygame.display.set_caption("викторина | результаты")
            #тут цвет набраных очков
            if score <= 0:
                score_color = pygame.Color(200,0,0)
            elif score <= 14:
                score_color = pygame.Color(250,250,250)
            elif score == 15:
                score_color = pygame.Color(155,0,248)
                background.fill(pygame.Color(60,10,80))
            #тут оценка (нз зачем раздельно)
            if score <= 0:
                rezult_color = pygame.Color(150,0,0)
                rezult = "УЖАСНО"
            elif score <= 2:
                rezult_color = pygame.Color(200,0,0)
                rezult = "Очень плохо"
            elif score <= 5:
                rezult_color = pygame.Color(250,0,0)
                rezult = "Плохо"
            elif score <= 8:
                rezult_color = pygame.Color(250,250,250)
                rezult = "Нормально"
            elif score <= 10:
                rezult_color = pygame.Color(0,200,0)
                rezult = "Хорошо"
            elif score <= 13:
                rezult_color = pygame.Color(0,255,0)
                rezult = "Отлично!"
            elif score == 15:
                rezult_color = pygame.Color(105, 0, 198)
                rezult = "ИДЕАЛЬНО!!"

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                window_surface.blit(background, (0, 0))
                window_surface.blit(total_font.render(("Всего набрано очков: " + str(score) + "/15"), False, (score_color)), (50,50))
                window_surface.blit(tim_font.render(("Затрачено времени: " + str(tim)), False, (score_color)), (50,100))
                window_surface.blit(total_font.render(("Результат: " + str(rezult)), False, (rezult_color)), (50,170))
                pygame.display.update()
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button1.rect.collidepoint(event.pos):
                current_otv = otv1
                otvetili = True
                if current_otv == prav_otv:
                    score = score + 1
                else:
                    score = score - 1
            elif button2.rect.collidepoint(event.pos):
                current_otv = otv2
                otvetili = True
                if current_otv == prav_otv:
                    score = score + 1
                else:
                    score = score - 1
            elif button3.rect.collidepoint(event.pos):
                current_otv = otv3
                otvetili = True
                if current_otv == prav_otv:
                    score = score + 1
                else:
                    score = score - 1

            if otvetili == True:
                
                voprs.remove(current_vopr)
                
                if len(voprs) == 0:
                    end = True

                else:
                    current_vopr = random.choice(voprs)
                    prav_otv = current_vopr.prav_otv
                    current_otvs = [
                        current_vopr.otvs[0],
                        current_vopr.otvs[1],
                        current_vopr.otvs[2],
                    ]
                    random.shuffle(current_otvs)
                    otv1 = current_otvs[0]
                    otv2 = current_otvs[1]
                    otv3 = current_otvs[2]

                    button1 = button(pygame.Color(90,90,90), pygame.Rect(90,355,110,50), str(otv1))
                    button2 = button(pygame.Color(70,70,70), pygame.Rect(290,355,110,50), str(otv2))
                    button3 = button(pygame.Color(80,80,80), pygame.Rect(490,355,110,50), str(otv3))

                    vopros_surface = current_vopr.text.render(current_vopr.question, False, (0, 0, 0))

                    pygame.display.set_caption(f"викторина | вопрос №{vopr_nomr + 1} | очки:{score}")
                    vopr_nomr = vopr_nomr + 1
                    otvetili = False

        if counter == 60:
            min = min + 1
            counter = 0
        
        #время на показ
        if min == 0:
            tim = str(counter) + " сек"
        else:
            tim = str(min) + " мин и " + str(counter) + " секунд"
        
        window_surface.blit(background, (0, 0))
        window_surface.blit(current_vopr.pic, (100,90))
        window_surface.blit(current_vopr.text.render(current_vopr.question, False, (0, 0, 0)), (100,50))
        window_surface.blit(score_font.render(("вопрос №" + str(vopr_nomr + 1) + " очки: " + str(score)), False, (0, 0, 0)), (10,10))

        button1.render()
        button2.render()
        button3.render()

        pygame.display.update()