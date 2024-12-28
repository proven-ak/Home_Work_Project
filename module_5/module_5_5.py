
class User:
    def __init__(self, nickname, password, age):
        """
        nickname - имя пользователя, строка
        password - в хэшированном виде, число
        age - возраст, число
        """
        self.nickname = nickname
        self.password = password
        self.age = age

    def add(self, users):
        """
        Добавляет объект User в список, если его там еще нет
        users - список объектов User.
        """
        # Проверяем наличие пользователя в списке, если отсутствует
        # добавляем в список
        if self not in users:
            users.append(self)
        return users


class Video:
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration, time_now, adult_mode):

        # title - заголовок, строка
        # duration - продолжительность, секунды
        # time_now - секунда остановки (изначально 0)
        # adult_mode - ограничение по возрасту, bool (False по умолчанию)

        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def add(self, videos, *video_list):
        """
        Добавляет объект Video в список, если его там еще нет.
        """
        # videos - список объектов Video.
        # video_list - список добавляемых видео

        for video_init in video_list:
            if video_init.title not in [video.title for video in self.videos]:
                self.videos.append(video_init)
        print("!!!!!!!!videos", videos)
        return videos


class UrTube:
    def __init__(self, users, videos, current_user):

        # users - список объектов User
        # videos - список объектов Video
        # current_user - текущий пользователь, User

        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password, users, current_user):
        """
        Метод принимает на вход аргументы:
        nickname, password и пытается найти пользователя в users с такими же
        логином и паролем. Если такой пользователь существует,
        то current_user меняется на найденного.
        Password передаётся в виде строки, а сравнивается по хэшу.
        """
        # nickname - логин пользователя
        # password - пароль пользователя
        # users - список пользователей
        # current_user - текущий пользователь, User

    def register(self, nickname, password, age):
        """
        Метод register добавляет пользователя в список users,
        если пользователя с таким же nickname еще нет.
        После успешной регистрации, вход выполняется автоматически
        (current_user становится зарегистрированным пользователем).
        """

        # Проверка возраста текущего пользователя.
        if age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Проверка наличия пользователя с таким же nickname
        for user in self.users:
            if user.nickname == nickname:
                print("Войдите в аккаунт, чтобы смотреть видео")
                return

        # Регистрация нового пользователя
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему.")

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        # current_user - текущий пользователь, User
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None

    def add(self, *video_list):
        """
        Метод принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos, если с таким же названием видео ещё
        не существует. В противном случае ничего не происходит/
        """
        # videos - список объектов Video
        # video_list - добавляемый список объектов Video
        # video_item - элемент списка объектов Video

        for video_item in video_list:
            if video_item not in videos:
                videos.append(video_item)
        return videos

    def get_videos(self, get_str):
        """
        Метод производит поиск строки get_str без учета регистра
        в списке видео. Если есть совпадение возвращает список видео.
        """
        # get_str - строка для поиска в списке объектов videos
        # videos - список объектов Video
        # video - элемент списка videos

        result =[]

        for video in self.videos:
            if get_str.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_str):
        """
        Метод watch_video, который принимает название фильма,
        если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        """
        # videos - список объектов Video
        # video_item - элемент списка объектов Video

        # Поиск видео с точным названием
        for video_item in self.videos:
            if video_str == video_item.title:
                # Выводим отсчёт времени просмотра
                for second in range(video_item.time_now, video_item.duration + 1):
                    print(second, end=" ", flush=True)
                print(" Конец видео")

                # Сброс текущего времени просмотра
                video_item.time_now = 0
                return

        # Если видео не найдено
        print("Видео не найдено.")


# Код для проверки
if __name__ == "__main__":

    # Инициализация переменных.
    users = []          # Список пользователей
    videos = []         # Список видео

    # Создание объектов User
    # us1 = User(nickname="Ivanov", password=123, age=21)
    # us2 = User(nickname="Petrov", password=1234, age=22)
    # us3 = User(nickname="Sidorov", password=12345, age=23)

    # Добавление пользователей в список users
    # users.append(us1)
    # users.append(us2)
    # users.append(us3)

    # Вывод списка пользователей на консоль
    # print("-----users :", users)

    # Создание объектов Video
    v1 = Video('Лучший язык программирования 2024 года', 200, 0, False)
    v2 = Video('Для чего девушкам парень программист?', 10, 0, adult_mode=True)

    # Создание объектов UrTube
    ur = UrTube(users, videos, current_user=[])

    # Добавление видео
    ur.add(v1,v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    # ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    # print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    # ur.watch_video('Лучший язык программирования 2024 года!')


"""
Вывод в консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist
"""