from ftplib import FTP
import getpass
import os

#создание укзанного каталога на сервере
def ftp_mkdir(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.mkd(args[0]))
    except:
        print("Ошибка")

#удаление указанного каталога на сервере
def ftp_rmdir(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.rmd(args[0]))
    except:
        print("Ошибка")

#смена текущего каталога на сервере
def ftp_cd(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.cwd(args[0]))
    except:
        print("Ошибка")
    return

#копирование указанного файла с сервера
def ftp_get(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    path = args[0]
    try:
        with open(path, 'wb') as f:
            print(ftp.retrbinary('RETR ' + path, f.write))
    except:
        print("Ошибка")

#копирование указанного файла на сервер
def ftp_put(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    path = args[0]
    try:
        ftype = path[len(path) - 3 : len(path)]
        if ftype == 'TXT':
            with open(path) as fobj:
                print(ftp.storlines('STOR ' + path, fobj))
        else:
            with open(path, 'rb') as fobj:
                print(ftp.storbinary('STOR ' + path, fobj))
    except:
        print("Ошибка")

#удаление указанного файла на сервере
def ftp_delete(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.delete(args[0]))
    except:
        print("Ошибка")
    return

#переименование указанного на сервере файла
def ftp_rename(ftp, args):
    if len(args) != 2:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.rename(args[0], args[1]))
    except:
        print("Ошибка")

#подключение к указанному серверу
def ftp_open_ftp(ftp, args):
    if len(args) != 1:
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.connect(args[0], 21))
    except:
        print("Ошибка при подключении")
        return
    user = input("Пользователь: ")
    password = getpass.getpass('Пароль: ')
    try:
        print(ftp.login(user, password))
    except:
        print("Ошибка при подключении")

#просмотр содержимого каталога
def ftp_ls(ftp, args):
    if (len(args) != 0):
        print("Недопустимое число аргументов")
        return
    print(ftp.retrlines('LIST'))

#изменение текущего каталога на локальном компьютере
def ftp_lcd(ftp, args):
    if (len(args) != 1):
        print("Недопустимое число аргументов")
        return
    os.chdir(args[0])

#разрыв соединения
def ftp_quit(ftp, args):
    if (len(args) != 0):
        print("Недопустимое число аргументов")
        return
    try:
        print(ftp.quit())
    except:
        pass
    exit(0)

commands = {
    'open' : ftp_open_ftp,
    'mkdir': ftp_mkdir,
    'rmdir': ftp_rmdir,
    'cd': ftp_cd,
    'get': ftp_get,
    'put': ftp_put,
    'delete': ftp_delete,
    'rename': ftp_rename,
    'lcd': ftp_lcd,
    'ls': ftp_ls,
    'quit': ftp_quit
    }

ftp = FTP()
while (True):
    temp = input('ftp> ').split(' ')
    command = temp[0]
    args = temp[1:]
    if (command not in commands):
        print("Недопустимая команда")
        continue
    commands[command](ftp, args)
