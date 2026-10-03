# Імпортуємо клас App — основний клас для створення Kivy-програми
from kivy.app import App

# Імпортуємо Screen для створення окремих екранів
# та ScreenManager для керування і перемикання між екранами
from kivy.uix.screenmanager import Screen, ScreenManager

# Імпортуємо Window для налаштування вікна програми
from kivy.core.window import Window

# Імпортуємо Builder для роботи з KV-розміткою
from kivy.lang import Builder

# Імпортуємо функції та словник кольорів Kivy
from kivy.utils import hex_colormap, colormap

# Імпортуємо Animation для створення анімацій
from kivy.animation import Animation

# Імпортуємо sp та dp для роботи з розмірами
from kivy.metrics import sp, dp

# Імпортуємо Image для роботи із зображеннями
from kivy.uix.image import Image

# Імпортуємо platform для визначення операційної системи
from kivy import platform

# Імпортуємо NumericProperty для створення числових властивостей Kivy
from kivy.properties import NumericProperty

# Імпортуємо Clock для виконання функцій через певний час
from kivy.clock import Clock

# Імпортуємо SoundLoader для завантаження та відтворення звуків
from kivy.core.audio import SoundLoader


# Створюємо клас головного меню
# Клас успадковує властивості та методи Screen

# KV-розмітка інтерфейсу вбудована у файл, щоб проєкту був потрібен лише main.py.
Builder.load_string(r"""
# Імпортуємо функцію для перетворення HEX-кольору у формат RGBA
#:import from_hex kivy.utils.get_color_from_hex

# Імпортуємо функцію rgba
#:import to_rgba kivy.utils.rgba

# Імпортуємо словник готових кольорів Kivy
#:import colormap kivy.utils.colormap


# Створюємо змінну з основним кольором кнопок
#:set main_color '#ef852e'

# Створюємо змінну з темнішим кольором кнопок
#:set main_color_dark "#c96e24"


# Задаємо шрифт для віджетів
<Widget>:

    # Встановлюємо шрифт Lemon-Regular.ttf
    font_name: 'assets/Lemon-Regular.ttf'


# Створюємо власний тип кнопки ButtonMenu
# @Button означає, що ButtonMenu успадковує Button
<ButtonMenu@Button>:

    # Встановлюємо розмір тексту кнопки
    font_size: "56sp"

    # Робимо текст жирним
    bold: True

    # Робимо стандартний фон кнопки повністю прозорим
    background_color: 0, 0, 0, 0

    # Вимикаємо автоматичне визначення розміру
    size_hint: None, None

    # Розміщуємо кнопку по центру горизонтально
    pos_hint: {"center_x": 0.5}

    # Встановлюємо ширину кнопки
    # texture_size[0] — ширина тексту
    # dp(40) — додатковий простір навколо тексту
    width: self.texture_size[0] + dp(40)


    # Малюємо власний фон кнопки перед самою кнопкою
    canvas.before:

        # Встановлюємо білий колір
        Color:
            rgba: colormap['white']

        # Створюємо зовнішній білий заокруглений прямокутник
        RoundedRectangle:

            # Розмір дорівнює розміру кнопки
            size: self.size

            # Позиція дорівнює позиції кнопки
            pos: self.pos

            # Заокруглюємо кути
            radius: [self.font_size]


        # Встановлюємо колір внутрішнього прямокутника
        # Якщо кнопка не натиснута — використовуємо main_color
        # Якщо кнопка натиснута — використовуємо main_color_dark
        Color:
            rgba: from_hex(main_color) if self.state == 'normal' else from_hex(main_color_dark)

        # Створюємо внутрішній заокруглений прямокутник
        RoundedRectangle:

            # Робимо його трохи меншим за зовнішній прямокутник
            size: self.size[0] - dp(6), self.size[1] - dp(6)

            # Зміщуємо його на 3dp,
            # щоб утворилася біла рамка
            pos: self.pos[0] + dp(3), self.pos[1] + dp(3)

            # Заокруглюємо кути
            radius: [self.font_size]


# Створюємо тип кнопки для іконок
# ButtonIcon успадковує всі властивості ButtonMenu
<ButtonIcon@ButtonMenu>:

    # Для кнопки використовуємо шрифт з іконками
    font_name: 'assets/typicons.ttf'


# Налаштовуємо екран головного меню
<Menu>:

    # Створюємо вертикальний контейнер
    BoxLayout:

        # Розташовуємо елементи зверху вниз
        orientation: "vertical"

        # Відступи від країв контейнера
        padding: "30dp"

        # Відстань між елементами
        spacing: "20dp"


        # Створюємо фон меню
        canvas:

            # Малюємо прямокутник із фоновою картинкою
            Rectangle:

                # Вказуємо шлях до картинки
                source: 'assets/images/back_menu.png'

                # Встановлюємо ширину фону 750dp
                # Висота дорівнює висоті контейнера
                size: dp(750), self.size[1]

                # Розташовуємо фон по центру
                pos: self.center_x - dp(750) / 2, self.y


        # Порожній віджет для створення відступу зверху
        Widget:

            # Він займає 5% доступної висоти
            size_hint_y: 0.05


        # Заголовок гри
        Label:

            # Текст заголовка
            # \n переносить текст на новий рядок
            text: "Quinea Pig\nCLICKER"

            # Розмір тексту
            font_size: "54sp"

            # Вирівнюємо текст по центру
            halign: "center"

            # Заголовок займає 15% висоти
            size_hint_y: 0.15


        # Зображення заголовка/логотипа
        Image:

            # Вказуємо шлях до картинки
            source: "assets/images/title.png"

            # Дозволяємо розтягувати зображення
            allow_stretch: True

            # Зображення займає 50% висоти
            size_hint_y: 0.5


        # Кнопка PLAY
        ButtonMenu:

            # Текст кнопки
            text: " PLAY "

            # Кнопка займає 15% висоти
            size_hint_y: 0.15


            # Код виконується при натисканні кнопки
            on_press:

                # Перемикаємося на екран гри
                root.manager.current = "game"

                # Встановлюємо напрямок переходу вліво
                root.manager.transition.direction = "left"


        # Контейнер для нижніх кнопок
        BoxLayout:

            # Контейнер займає 15% висоти
            size_hint_y: 0.15


            # Кнопка Settings
            ButtonIcon:

                # Unicode-код іконки налаштувань
                text: "\uE04F"

                # Викликаємо метод go_settings()
                on_press:
                    root.go_settings()


            # Порожній Widget створює простір між кнопками
            Widget:


            # Кнопка Exit
            ButtonIcon:

                # Unicode-код іконки виходу
                text: "\uE121"

                # Закриваємо програму
                on_press:
                    app.stop()


# Налаштовуємо екран Settings
<Settings>:

    # Створюємо вертикальний контейнер
    BoxLayout:

        # Елементи розташовуються зверху вниз
        orientation: "vertical"

        # Відступи від країв
        padding: "30dp"

        # Відстань між елементами
        spacing: "20dp"


        # Заголовок Settings
        Label:

            # Текст заголовка
            text: "Created\nBy\nMaksym!"

            # Розмір тексту
            font_size: "40sp"


        # Кнопка повернення
        ButtonMenu:

            # Текст кнопки
            text: "Back"

            # Кнопка займає 20% висоти
            size_hint_y: 0.2

            # Викликаємо метод повернення до меню
            on_press:
                root.go_menu()


# Налаштування класу RotatedImage
<RotatedImage>:

    # Малюємо трансформацію перед зображенням
    canvas.before:

        # Зберігаємо поточну матрицю трансформації
        PushMatrix

        # Створюємо обертання
        Rotate:

            # Кут обертання беремо з властивості angle
            angle: self.angle

            # Обертання навколо осі Z
            axis: 0, 0, 1

            # Обертання відбувається навколо центру картинки
            origin: self.center


    # Код після малювання зображення
    canvas.after:

        # Повертаємо попередню матрицю трансформації
        PopMatrix


# Налаштовуємо клас Fish
<Fish>:

    # Початкове зображення риби
    source: 'assets/images/fish_01.png'

    # Розмір не буде визначатися автоматично
    size_hint: None, None

    # Встановлюємо розмір риби 200×200dp
    size: dp(200), dp(200)

    # Дозволяємо розтягувати зображення
    allow_stretch: True

    # Робимо рибу невидимою на початку
    opacity: 0


# Налаштовуємо екран гри
<Game>:

    # Створюємо головний вертикальний контейнер
    BoxLayout:

        # Елементи розташовуються вертикально
        orientation: "vertical"

        # Відступи від країв
        padding: "30dp"

        # Відстань між елементами
        spacing: "20dp"


        # Малюємо фон гри
        canvas:

            # Створюємо прямокутник із фоновою картинкою
            Rectangle:

                # Шлях до фонового зображення
                source: 'assets/images/back_game.png'

                # Позиція фону
                pos: self.pos

                # Розмір фону
                size: self.size


        # Верхнє меню гри
        BoxLayout:

            # Верхнє меню займає 12% висоти
            size_hint_y: 0.12


            # Напис із рахунком
            Label:

                # Виводимо поточний рахунок
                # root.score — значення score з класу Game
                # str() перетворює число на текст
                text: str(root.score)

                # Розмір тексту
                font_size: '56sp'

                # Label займає 80% ширини
                size_hint_x: 0.8

                # Встановлюємо позицію Label
                pos_hint: {'center_x': 1}


            # Кнопка-іконка для повернення додому
            ButtonIcon:

                # Unicode-код іконки будинку
                text: '\uE08A'

                # Викликаємо метод go_home()
                on_press: root.go_home()


        # Основна ігрова область
        FloatLayout:

            # Ігрова область займає 76% висоти
            size_hint_y: 0.76

            # ID дозволяє звертатися до цього віджета з Python
            id: game_window


            # Заголовок поточного рівня
            Label:

                # ID заголовка
                id: level_title

                # Текст заголовка
                text: 'Level 1'

                # Розмір тексту
                font_size: '60sp'

                # Висоту задаємо вручну
                size_hint_y: None

                # Висота залежить від фактичного розміру тексту
                height: self.texture_size[1]

                # Розташовуємо заголовок по центру горизонтально
                x: root.width / 2 - self.width / 2

                # Встановлюємо початкову позицію по вертикалі
                y: '130dp'


            # Створюємо рибу
            Fish:

                # ID риби
                id: fish

                # Розташовуємо рибу по центру
                center: root.center


            # Напис, який показується після завершення рівня
            Label:

                # ID напису
                id: level_complete

                # Текст напису
                # \n переносить текст на новий рядок
                text: '    Level\ncomplete!'

                # Встановлюємо колір через HEX
                color: from_hex('#12F3AF')

                # Розмір тексту
                font_size: '50sp'

                # Висоту задаємо вручну
                size_hint_y: None

                # Встановлюємо висоту відповідно до розміру тексту
                height: self.texture_size[1]

                # Розташовуємо напис по центру горизонтально
                x: root.width / 2 - self.width / 2

                # Розташовуємо напис по центру вертикально
                # + dp(100) зміщує його вгору
                y: root.height / 2 - self.height / 2 + dp(100)

                # На початку напис невидимий
                opacity: 0


        # Нижнє меню гри
        BoxLayout:

            # Нижнє меню займає 12% висоти
            size_hint_y: 0.12


            # Кнопка налаштувань
            ButtonIcon:

                # Unicode-код іконки налаштувань
                text: '\uE04F'

                # Розташовуємо кнопку внизу
                pos_hint: {'y': 0}
""")

class Menu(Screen):

    # Конструктор класу Menu
    # **kw приймає додаткові іменовані аргументи
    def __init__(self, **kw):

        # Викликаємо конструктор батьківського класу Screen
        super().__init__(**kw)

    # Метод для переходу до екрана гри
    # *args дозволяє приймати додаткові аргументи від події Kivy
    def go_game(self, *args):

        # Встановлюємо екран "game" як поточний
        self.manager.current = "game"

        # Встановлюємо напрямок анімації переходу — вліво
        self.manager.transition.direction = "left"

    # Метод для переходу до екрана налаштувань
    def go_settings(self, *args):

        # Встановлюємо екран "settings" як поточний
        self.manager.current = "settings"

        # Встановлюємо напрямок анімації переходу — вгору
        self.manager.transition.direction = "up"

    # Метод для виходу з програми
    def exit_app(self, *args):

        # Зупиняємо запущену програму
        app.stop()


# Створюємо клас екрана налаштувань
class Settings(Screen):

    # Конструктор класу Settings
    # **kwargs приймає додаткові іменовані аргументи
    def __init__(self, **kwargs):

        # Викликаємо конструктор батьківського класу Screen
        super().__init__(**kwargs)

    # Метод для повернення до головного меню
    def go_menu(self, *args):

        # Перемикаємо поточний екран на "menu"
        self.manager.current = "menu"

        # Встановлюємо напрямок переходу — вниз
        self.manager.transition.direction = "down"


# Створюємо клас для зображень, які можна обертати
class RotatedImage(Image):

    # Три крапки означають, що клас поки не містить додаткового коду
    ...


# Закоментований код — зараз він не виконується
# Тут планувалося створити пульсацію віджета
# через його збільшення та зменшення
# def polse_widget(self):

# Три крапки означали б порожню реалізацію методу
#     ...


# Створюємо клас Fish для роботи з рибою
# Fish успадковує можливості RotatedImage
class Fish(RotatedImage):

    # Зберігаємо інформацію про те,
    # чи зараз програється анімація кліку
    anim_play = False

    # Забороняємо взаємодію з рибою на початку
    interaction_block = True

    # Коефіцієнт збільшення риби під час анімації
    COEF_MULT = 1.5

    # Тут буде зберігатися назва поточної риби
    fish_current = None

    # Індекс поточної риби у списку рівня
    fish_index = 0

    # Тут буде зберігатися поточна кількість HP риби
    hp_current = None

    # Створюємо числову властивість для кута повороту
    # Початковий кут — 0 градусів
    angle = NumericProperty(0)


    # Завантажуємо звук кліку по рибі
    click_music = SoundLoader.load('assets/audios/bubble01.mp3')

    # Завантажуємо звук перемоги над рибою
    defeate_music = SoundLoader.load('assets/audios/fish_def.ogg')


    # Метод викликається після створення KV-властивостей віджета
    def on_kv_post(self, base_widget):

        # Отримуємо посилання на екран гри
        # parent — батьківський віджет
        # Кілька parent потрібні, щоб піднятися до Game
        self.GAME_SCREEN = self.parent.parent.parent

        # Викликаємо метод on_kv_post батьківського класу
        return super().on_kv_post(base_widget)


    # Метод створює та налаштовує нову рибу
    def new_fish(self, *args):

        # Отримуємо назву риби з поточного рівня
        # app.LEVEL — номер рівня
        # self.fish_index — номер риби
        self.fish_current = app.LEVELS[app.LEVEL][self.fish_index]

        # Встановлюємо шлях до зображення поточної риби
        self.source = app.FISHES[self.fish_current]['source']

        # Встановлюємо HP поточної риби
        self.hp_current = app.FISHES[self.fish_current]['hp']

        # Запускаємо анімацію появи та руху риби
        self.swim()


    # Метод відповідає за плавання риби на екран
    def swim(self):

        # Розміщуємо рибу за лівою межею ігрового екрана
        self.pos = (
            self.GAME_SCREEN.x - self.width,
            self.GAME_SCREEN.height / 2
        )

        # Робимо рибу повністю видимою
        self.opacity = 1

        # Створюємо анімацію руху риби до центру
        # x визначає кінцеву координату по горизонталі
        # duration=1 означає, що анімація триває 1 секунду
        swim = Animation(
            x=self.GAME_SCREEN.width / 2 - self.width / 2,
            duration=1
        )

        # Запускаємо анімацію на рибі
        swim.start(self)

        # Після завершення анімації
        # дозволяємо взаємодію з рибою
        swim.bind(
            on_complete=lambda w, a:
            setattr(self, "interaction_block", False)
        )


    # Метод викликається після перемоги над рибою
    def defeated(self):

        # Блокуємо натискання на рибу
        self.interaction_block = True

        # Створюємо анімацію обертання риби
        # angle збільшується на 360 градусів
        # d=1 — тривалість анімації 1 секунда
        # in_cubic — тип плавності анімації
        anim = Animation(
            angle=self.angle + 360,
            d=1,
            t='in_cubic'
        )


        # Зберігаємо старий розмір риби
        old_size = self.size.copy()

        # Зберігаємо стару позицію риби
        old_pos = self.pos.copy()


        # Розраховуємо новий розмір риби
        # Збільшуємо ширину та висоту у COEF_MULT * 3 рази
        new_size = (
            self.size[0] * self.COEF_MULT * 3,
            self.size[1] * self.COEF_MULT * 3
        )


        # Розраховуємо нову позицію риби
        # Це потрібно, щоб збільшення відбувалося приблизно від центру
        new_pos = (
            self.pos[0] - (new_size[0] - self.size[0]) / 2,
            self.pos[1] - (new_size[0] - self.size[1]) / 2
        )


        # Додаємо до анімації збільшення риби
        # а потім повернення до старого розміру
        anim &= (
            Animation(
                size=(new_size),
                t='in_out_bounce'
            )
            + Animation(
                size=(old_size),
                duration=0
            )
        )


        # Додаємо до анімації зміну позиції
        # а потім повернення на стару позицію
        anim &= (
            Animation(
                pos=(new_pos),
                t='in_out_bounce'
            )
            + Animation(
                pos=(old_pos),
                duration=0
            )
        )


        # Цей рядок створював би анімацію збільшення у 2 рази
        # та повернення до старого розміру
        # Зараз він закоментований і не виконується
        # anim = Animation(size=(self.size[0] * self.COEF_MULT * 2, self.size[1] * self.COEF_MULT * 2)) + Animation(size=old_size)


        # Додаємо до загальної анімації поступове зникнення риби
        anim &= Animation(opacity=0)

        # Запускаємо анімацію
        anim.start(self)

        # Відтворюємо звук перемоги над рибою
        self.defeate_music.play()


    # Метод обробляє натискання миші/тачскріна
    def on_touch_down(self, touch):

        # Перевіряємо, чи клік потрапив у рибу
        # collide_point повертає True, якщо точка знаходиться всередині віджета
        #
        # Також перевіряємо, чи не програється анімація
        # та чи не заблокована взаємодія
        if (
            not self.collide_point(*touch.pos)
            or self.anim_play
            or self.interaction_block
        ):

            # Якщо хоча б одна умова виконується —
            # припиняємо обробку кліку
            return


        # Перевіряємо, що анімація не програється
        # та взаємодія з рибою дозволена
        if not self.anim_play and not self.interaction_block:

            # Зменшуємо HP риби на 1
            self.hp_current -= 1

            # Збільшуємо рахунок гравця на 1
            self.GAME_SCREEN.score += 1

            # Відтворюємо звук кліку по рибі
            self.click_music.play()


            # Перевіряємо, чи риба ще має HP
            if self.hp_current > 0:

                # Зберігаємо поточний розмір риби
                old_size = self.size.copy()

                # Зберігаємо поточну позицію риби
                old_pos = self.pos.copy()


                # Розраховуємо новий розмір риби
                new_size = (
                    self.size[0] * self.COEF_MULT,
                    self.size[1] * self.COEF_MULT
                )


                # Розраховуємо нову позицію
                # щоб збільшення відбувалося приблизно від центру
                new_pos = (
                    self.pos[0] - (new_size[0] - self.size[0]) / 2,
                    self.pos[1] - (new_size[1] - self.size[1]) / 2
                )


                # Створюємо анімацію збільшення
                # та повернення до початкового розміру
                zoom_anim = (
                    Animation(
                        size=(new_size),
                        duration=0.05
                    )
                    + Animation(
                        size=(old_size),
                        duration=0.05
                    )
                )


                # Додаємо до анімації зміну позиції
                # та повернення до початкової позиції
                zoom_anim &= (
                    Animation(
                        pos=(new_pos),
                        duration=0.05
                    )
                    + Animation(
                        pos=(old_pos),
                        duration=0.05
                    )
                )


                # Запускаємо анімацію кліку
                zoom_anim.start(self)

                # Встановлюємо True,
                # щоб під час анімації не можна було клікнути повторно
                self.anim_play = True


                # Після завершення анімації
                # встановлюємо anim_play назад у False
                zoom_anim.bind(
                    on_complete=lambda *args:
                    setattr(self, "anim_play", False)
                )


            # Якщо HP риби стало 0
            else:

                # Запускаємо анімацію перемоги над рибою
                self.defeated()


                # Перевіряємо, чи є ще риби на поточному рівні
                if len(app.LEVELS[app.LEVEL]) > self.fish_index + 1:

                    # Переходимо до індексу наступної риби
                    self.fish_index += 1

                    # Через 1.2 секунди створюємо наступну рибу
                    Clock.schedule_once(
                        self.new_fish,
                        1.2
                    )

                # Якщо наступної риби немає
                else:

                    # Через 1.2 секунди завершуємо рівень
                    Clock.schedule_once(
                        self.GAME_SCREEN.level_complete,
                        1.2
                    )


        # Передаємо подію натискання батьківському класу
        return super().on_touch_down(touch)


# Створюємо клас екрана гри
class Game(Screen):

    # Створюємо властивість для зберігання рахунку
    # Початкове значення — 0
    score = NumericProperty(0)


    # Завантажуємо фонову музику
    back_sound = SoundLoader.load(
        'assets/audios/Black_Swan_part.mp3'
    )

    # Зациклюємо фонову музику
    # Після завершення вона починається спочатку
    back_sound.loop = True

    # Завантажуємо звук завершення рівня
    level_complete_sound = SoundLoader.load(
        'assets/audios/level_complete.ogg'
    )


    # Метод викликається перед входом на екран Game
    def on_pre_enter(self, *args):

        # Обнуляємо рахунок
        self.score = 0

        # Встановлюємо перший рівень
        app.LEVEL = 0

        # Ховаємо напис про завершення рівня
        self.ids.level_complete.opacity = 0

        # Встановлюємо індекс першої риби
        self.ids.fish.fish_index = 0

        # Викликаємо метод батьківського класу
        return super().on_pre_enter(*args)


    # Метод викликається після входу на екран Game
    def on_enter(self, *args):

        # Створюємо анімацію появи заголовка рівня
        label_animation = (

            # Переміщуємо заголовок у центр
            Animation(
                y=(self.height - self.ids.level_title.height) / 2 + dp(100),
                duration=1
            )

            # Поступово робимо заголовок видимим
            + Animation(
                opacity=1,
                duration=1
            )

            # Переміщуємо заголовок вгору за межі екрана
            + Animation(
                y=self.height,
                duration=1
            )
        )


        # Додаємо плавне зникнення заголовка
        label_animation &= (
            Animation(
                opacity=1,
                duration=2
            )
            + Animation(
                opacity=0,
                duration=1
            )
        )


        # Запускаємо анімацію для заголовка рівня
        label_animation.start(self.ids.level_title)

        # Після завершення анімації запускаємо start_game
        label_animation.bind(
            on_complete=self.start_game
        )


        # Запускаємо фонову музику
        self.back_sound.play()

        # Викликаємо метод батьківського класу
        return super().on_enter(*args)


    # Метод запускає гру після завершення анімації заголовка
    # animation — об'єкт завершеної анімації
    # widget — віджет, на якому була анімація
    def start_game(self, animation, widget):

        # Створюємо першу рибу
        self.ids.fish.new_fish()


    # Метод викликається після завершення всіх риб рівня
    def level_complete(self, *args):

        # Цей рядок був би способом просто показати напис
        # self.ids.level_complete.opacity = 1


        # Створюємо анімацію збільшення розміру напису
        anim_zoom = Animation(
            font_size=dp(70),
            d=0.3
        )


        # Додаємо до анімації появу напису
        anim_zoom &= Animation(
            opacity=1,
            d=0.3
        )


        # Переходимо до наступного рівня
        app.LEVEL += 1

        # Запускаємо анімацію напису
        anim_zoom.start(self.ids.level_complete)

        # Зменшуємо гучність фонової музики
        self.back_sound.volume = 0.5

        # Відтворюємо звук завершення рівня
        self.level_complete_sound.play()


    # Метод повернення до головного меню
    def go_home(self):

        # Створюємо коротку анімацію зникнення риби
        fish_disapear_anim = Animation(
            opacity=0,
            duration=0.1
        )

        # Запускаємо анімацію зникнення риби
        fish_disapear_anim.start(self.ids.fish)

        # Зупиняємо фонову музику
        self.back_sound.stop()

        # Переходимо до головного меню
        self.manager.current = "menu"

        # Встановлюємо напрямок переходу вправо
        self.manager.transition.direction = "right"


# Створюємо основний клас програми
class ClickerApp(App):

    # Зберігаємо номер поточного рівня
    # Початковий рівень — 0
    LEVEL = 0


    # Створюємо словник із даними про риб
    FISHES = {

        # Дані першої риби
        'fish1':
            {
                # Шлях до зображення першої риби
                'source': 'assets/images/fish_01.png',

                # Кількість HP першої риби
                'hp': 10
            },


        # Дані другої риби
        'fish2':
            {
                # Шлях до зображення другої риби
                'source': 'assets/images/fish_02.png',

                # Кількість HP другої риби
                'hp': 20
            }
    }


    # Створюємо список рівнів
    LEVELS = [

        # Перший рівень містить три риби
        # Перша риба має 10 HP
        # Друга риба має 10 HP
        # Третя риба має 20 HP
        ['fish1', 'fish1', 'fish2']
    ]


    # Метод створення основного інтерфейсу програми
    def build(self):

        # Створюємо менеджер екранів
        sm = ScreenManager()

        # Додаємо екран головного меню
        # name="menu" — його унікальне ім'я
        sm.add_widget(
            Menu(name="menu")
        )

        # Додаємо екран гри
        # name="game" — його унікальне ім'я
        sm.add_widget(
            Game(name="game")
        )

        # Додаємо екран налаштувань
        # name="settings" — його унікальне ім'я
        sm.add_widget(
            Settings(name="settings")
        )

        # Повертаємо менеджер екранів
        # Він стає головним віджетом програми
        return sm


# Перевіряємо, чи програма запущена не на Android
if platform != 'android':

    # Якщо це ПК, встановлюємо розмір вікна 400×600
    Window.size = (400, 600)


# Створюємо об'єкт програми
app = ClickerApp()

# Запускаємо програму
app.run()