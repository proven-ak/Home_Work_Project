
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
        Добавляет объект User в список, если его там еще нет.
        users - список объектов User.
        """
        # Проверяем наличие пользователя в списке
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

    def __add__(self, videos):
        """
        Добавляет объект Video в список, если его там еще нет.
        videos - список объектов Video.
        """
        # Проверяем наличие video в списке
        if self not in videos:
            videos.append(self)
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
        Метод register, который принимает три аргумента: nickname,
        password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        # nickname - логин пользователя
        # password - пароль пользователя
        # age - возраст пользователя
    def log_out(self, current_user):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        # current_user - текущий пользователь, User

    def add(self, videos, *video_list):
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

        for video in self.videos:
            if get_str.lower() in video.title.lower():
                return video






# Код для проверки
if __name__ == "__main__":
    # Создание списка пользователей
    users = []
    videos = []

    # Создание объектов User
    us1 = User(nickname="Ivanov", password=123, age=21)
    us2 = User(nickname="Petrov", password=1234, age=22)
    us3 = User(nickname="Sidorov", password=12345, age=23)

    # Добавление пользователей в список users
    users.append(us1)
    users.append(us2)
    users.append(us3)

    # Вывод списка пользователей на консоль
    print("-----users :", users)

    # Создание объектов Video
    v1 = Video('Лучший язык программирования 2024 года', 200, 0, False)
    v2 = Video('Для чего девушкам парень программист?', 10, 0, adult_mode=True)

    # Добавление видео в список videos
    videos.append(v1)
    videos.append(v2)

    # Вывод списка видео на консоль
    print("-----videos: ", videos)

    # Создание объектов UrTube
    ur = UrTube(users, videos, current_user=us1)

    print("-----ur: ", ur)

    # Добавление видео
    ur.add(videos, v1, v2)

    print("-----ur.add: ", ur)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

"""
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
"""

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