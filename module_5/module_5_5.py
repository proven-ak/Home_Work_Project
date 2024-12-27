class User:
    def __init__(self, nickname, password, age):
        """
        nickname -
        password -
        age -
        """
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        """
        title - заголовок, строка
        duration - продолжительность, секунды
        time_now - секунда остановки (изначально 0)
        adult_mode - ограничение по возрасту, bool (False по умолчанию)
        """
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        """
        users - список объектов User
        videos - список объектов Video
        current_user - текущий пользователь, User
        """
        self.users = users
        self.videos = videos
        self.current_user = current_user