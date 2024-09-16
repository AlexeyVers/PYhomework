from time import sleep
class User:
    user_base = []

    def log_in(nickname, password):
        base = User.user_base
        if not base:
            User.user_base.append([str(nickname), hash(password)])
            return nickname
        else:
            for i in base:
                if nickname == i[0]:
                    if password != i[1]:
                        print('Пароль не подходит')
                    else:
                        return nickname
                else:
                    User.user_base.append([str(nickname), hash(password)])
                    return nickname

    def register(nickname, password, age):
        base = User.user_base
        if not base:
            User.user_base.append([str(nickname), hash(password), int(age)])
            return [str(nickname), hash(password), int(age)]
        else:
            for i in base:
                if nickname == i[0]:
                    print('Такой пользователь уже существует')
            else:
                User.user_base.append([str(nickname), hash(password), int(age)])
                return [str(nickname), hash(password), int(age)]



class Video:
    video_base = []

    def add_video(title, duration, adult_mode):
        video = Video.video_base
        if not video:
            Video.video_base.append([str(title), int(duration), 0, bool(adult_mode)])
        else:
            for i in video:
                if title in i:
                    print('Такое видео уже существует')
                else:
                    Video.video_base.append([str(title), int(duration), 0, bool(adult_mode)])
                    break

    def get_video(title):
        video = Video.video_base
        result = []
        if not video:
            print('Нет такого видео')
        else:
            for i in video:
                if title.lower() in i[0].lower():
                    result.append(i)
                else:
                    print('Нет такого видео')
            return result

    def watch_video(title):
        vish_list = Video.get_video(title)
        quantity = 0
        if UrTube.current_user:
            for video in vish_list:
                if title.lower() == video[0].lower():
                    if video[2]:
                        if UrTube.current_user[2] >= 18:
                              while quantity < video[1]:
                                  sleep(1)
                                  quantity += 1
                                  print(quantity)
                        else:
                            print('Вым рано такое смотреть')
                    else:
                        while quantity < video[1]:
                            sleep(1)
                            quantity += 1
                            print(quantity)
            else:
                print('Войдите в аккаунт чтобы смотреть видео')


class UrTube:
    videos = Video.video_base
    users = User.user_base
    current_user = []

    def log_in(nickname, password, age):
        if User.log_in(nickname, password, age):
            current_user = User.log_in(nickname, password, age)
            UrTube.current_user = current_user

    def register(nickname, password, age):
        current_user = User.register(nickname, password, age)
        UrTube.current_user = current_user

    def log_out():
        UrTube.current_user = []

    def add(title, duration, adult_mode):
        Video.add_video(title, duration, adult_mode)

    def get_videos(title):
        Video.get_videos(title)

    def watch_video(title):
        Video.watch_video(title)


UrTube.register('Lesha', 158, 18)
UrTube.add('video', 2, True)
UrTube.watch_video('video')
UrTube.log_out()
UrTube.watch_video('video')
UrTube.add('viva', 2, False)
UrTube.watch_video('viva')
