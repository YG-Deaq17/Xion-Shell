# Python 3.7.5 64x
# [encoding = 'utf-8'] INFO: Use this fragment of code for supported Russian Laguage in files.
# console = Console(width=63)

import os
import time
from tqdm import tqdm, tqdm_gui, trange
import pyautogui
import rich
from rich.tree import Tree
from rich import print as rprint
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich import style

os.system("cls")
os.system("title Xion. Version: 1v[debug__mode: off]")
pyautogui.press("F11")

console = Console(width=63)
print(Panel.fit("Добро пожаловать в [blue]Xion[/blue]! Для продолжения войдите в систему.", title="System"))

def auth__autoentry():
    pyautogui.press('a')
    pyautogui.press('d')
    pyautogui.press('m')
    pyautogui.press('i')
    pyautogui.press('n')
    pyautogui.press('Enter')
    pyautogui.press('s')
    pyautogui.press('h')
    pyautogui.press('a')
    pyautogui.press('2')
    pyautogui.press('5')
    pyautogui.press('6')
    pyautogui.press('Enter')
    # time.sleep(5)
    # pyautogui.press("-")
    # pyautogui.press("-")
    # pyautogui.press("s")
    # pyautogui.press("t")
    # pyautogui.press("a")
    # pyautogui.press("t")
    # pyautogui.press("Enter")

def console__title():
  console.print(Panel.fit("[blue]Xion[/blue] by Usersoft Incorpareted 2023-2025. Version [green]v1[/green] commands for begin: [yellow]--list[/yellow]; [yellow]--coms[/yellow]; [yellow]--ver[/yellow]; [yellow]--ver .stat[/yellow]"))

def main__system__status():
  os.system("start xionstatus_rel.py")

def func__screenclear():
  time.sleep(0.6)
  os.system("cls")

def preload__menu():
    print("Bootmenu launched...")
    time.sleep(2)
    os.system("cls")
    console.print("[green]Bootmenu launched...[green]")
    time.sleep(3)
    console.print("[INFO]23x1: [yellow]main__system__status[/yellow] in [yellow]xion.main__system[/yellow] have info by [yellow]xion.main__system__status.info[/yellow]")
    console.print("[INFO]23x2: uploading modules from [yellow].main__system[/yellow]; com:  [yellow]--stat[/yellow]")
    time.sleep(2)
    console.print("[XION.MODULE][yellow]xion.main__system__list[/yellow]")
    time.sleep(0.6)
    console.print("[XION.MODULE][yellow]xion.main__system__licence[/yellow]")
    time.sleep(0.6)
    console.print("[XION.MODULE][yellow]xion.main__system__readme[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__grph[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__status[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__coms[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__stat[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__title[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__ver[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__sc[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__RESET[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__exit[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__quit[/yellow]")
    time.sleep(3)
    func__screenclear()

def main__system__list():
    list = Tree("[yellow]файлы[/yellow] в директории [green]store_files[/green]:")
    list.add("licence.flx")
    list.add("readme.flx")
    rprint(list)
def main__system__licence():
  licence_open = open("C:\\xion\\builds\\v1\\store_files\\licence.flx", 'r')
  screen_view = licence_open.read()
  print(screen_view)
def main__system__readme():
  readme_open = open("C:\\xion\\builds\\v1\\store_files\\readme.flx", 'r',  encoding = 'utf-8')
  screenread_view = readme_open.read()
  print(screenread_view)
def main__system__grph():
  func__screenclear()
  print(Panel.fit("Если вы видите это окно. Значит отображения текста в окне прошло успешно. Это требуется для понимания вами что минимальная графика всё-таки более требовательна для оболочек вроде моей, вдобавок зрение более проще воспринимает окна чем голый текст, потому что глазу приходится напрягаться для различия одних элементов текста(информации), от других элементов консоли.", title="--grph"))
  time.sleep(5)
  func__screenclear()
  print(Panel.fit("[white on blue]Если текст имеет синий цвет, это обозначает что цветовая передача на минимальном уровне 8-битных цветов рабоатет корректно. Синий есть, 66,6% целостности оболочки и графические компоненты стабильны и работают нормально.", title="--grph"))
  time.sleep(3.7)
  func__screenclear()
  print(Panel.fit("[blue]Если вы видите синий цвет которым был размечен текст, значит функциональность смены и корректировки цвета в консоле работает правильно. Итог: Цвете передача корректная, графическая состовляющая имеет 100% целостности.", title="--grph"))
  time.sleep(3.7)
  func__screenclear()
  print(Panel.fit("[green]Тест окончен. Через 1.3 секунды окно закроется.", title="--grph"))
  time.sleep(1.3)
  func__screenclear()
def main__system__coms():
  commands_open = open("C:\\xion\\builds\\v1\\store_files\\coms.cf", 'r', encoding = 'utf-8')
  screencom_view = commands_open.read()
  print(screencom_view)
def main__system__stat():
    print(Panel.fit("[black on white]Загрузка статуса", title="--stat"))
    time.sleep(2)
    console.print("status:  [black on green]Ok")
    time.sleep(1)
    console.print("[yellow]main__system__status[/yellow] in [yellow]xion.main__system[/yellow] have info by [yellow]xion.main__system__status.info[/yellow]")
    console.print("uploading modules from [yellow].main__system[/yellow]; com:  [yellow]--stat[/yellow]")
    time.sleep(1)
    console.print("[yellow]xion.main__system__list[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__licence[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__readme[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__grph[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__status[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__coms[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__stat[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__title[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__ver[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__sc[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__RESET[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__exit[/yellow]")
    time.sleep(0.4)
    console.print("[yellow]xion.main__system__quit[/yellow]")
    time.sleep(1)
    console.print("status:  [black on green]Ok")
    time.sleep(2)
    console.print("shell:   Working")
    time.sleep(2)
    console.print("build:   2023_v1")
    time.sleep(2)
def main__system__title():
  func__screenclear()
  console__title()
def main__system__ver():
  console.print("--[yellow]1v[/yellow]")
def main__system__sc():
  func__screenclear()
def main__system__RESET():
  print(Panel.fit("[white on blue]Вы действительно хотите перезагрузить оболочку?"))
  choice = input("Да(Y) или Нет(N)? --")
  if choice == "y" or choice == "Y":
      pyautogui.press("F11")
      console.print("[red on white]ПРОИЗОВОДИМ ПЕРЕЗАГРУЗКУ...")
      time.sleep(3)
      os.system('start C:\\xion\\builds\\v1\\main.py')
      exit()
  elif choice == "n" or choice == "N":
      xion__main__system()
  else:
      xion__main__system()

def xion__main__system():
    in__action = console.input("[green]$")
    if in__action == "--list" or in__action == "--List":
        main__system__list()
    elif in__action == "--list .stat" or in__action == "--List .stat":
        print(Panel.fit("Загрузка статуса",title="com: list"))
        time.sleep(2)
        console.print("type:             [yellow]file[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]list[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__list[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--list[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
    elif in__action == "--list .info" or in__action == "--List .info":
        console.print("[yellow]list[/yellow] - команда отображающая список файлов хранящихся непосредственно в папке [green]store_files[/green]")
        console.print("name           [yellow]list[/yellow]")
        console.print("module         [yellow]main__system__list[/yellow]")
    elif in__action == "--licence" or in__action == "--Licence":
        main__system__licence()
    elif in__action == "--licence .stat" or in__action == "--Licence .stat":
        print(Panel.fit("Загрузка статуса",title="com: licence"))
        time.sleep(2)
        console.print("type:             [yellow]file[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]licence[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__licence[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--licence[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
    elif in__action == "--licence .info" or in__action == "--Licence .info":
        console.print("[yellow]licence[/yellow] - команда отображающая лицензию, её номер и краткое содержание информации об оболочке.")
        console.print("name           [yellow]licence[/yellow]")
        console.print("module         [yellow]main__system__licence[/yellow]")
    elif in__action == "--readme" or in__action == "--Readme":
        main__system__readme()
    elif in__action == "--readme .stat" or in__action == "--Readme .stat":
        print(Panel.fit("Загрузка статуса",title="com: --readme"))
        time.sleep(2)
        console.print("type:             [yellow]file[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]readme[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__readme[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--readme[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
    elif in__action == "--readme .info" or in__action == "--Readme .info":
        console.print("[yellow]readme[/yellow] - команда открывающая [bold]readme.flx[/bold] в [green]store_files[/green]. Краткая документация к оболочке.")
        console.print("name           [yellow]readme[/yellow]")
        console.print("module         [yellow]main__system__readme[/yellow]")
    elif in__action == "--grph" or in__action == "--Grph":
        main__system__grph()
    elif in__action == "--grph .stat" or in__action == "--Grph .stat":
        print(Panel.fit("Загрузка статуса",title="com: grph"))
        time.sleep(2)
        console.print("type:             [yellow]test[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]grph[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__grph[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--grph[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
    elif in__action == "--grph .info" or in__action == "--Grph .info":
        console.print("[yellow]grph[/yellow] - команда которая производит графический тест оболочки, для показания минимальных возомжностей.")
        console.print("name           [yellow]grph[/yellow]")
        console.print("module         [yellow]main__system__grph[/yellow]")
    elif in__action == "--status.rel" or in__action == "--Status.rel":
        main__system__status()
    elif in__action == "--status.rel .stat" or in__action == "--Status.rel .stat":
        console.print("Введённая вами команда невыполнима. Недостаточно прав.")
        print(Panel.fit("[red]xion.main__system__status.rel[/red], arg:   [yellow].stat[/yellow]", title="[red]Erorr"))
    elif in__action == "--status.rel .info" or in__action == "--Status.rel .info":
         console.print("Модуль не найден... Невозможно выполнить команду.            *Защита команды администратором: [green]Включено[/green]*")
         print(Panel.fit("[red]xion.main__system__status.rel[/red], arg:   [yellow].info[/yellow]", title="[red]modul not founded..."))
    elif in__action == "--coms" or in__action == "--Coms":
         main__system__coms()
    elif in__action == "--coms .stat" or in__action == "--Coms .stat":
        print(Panel.fit("Загрузка статуса",title="com: coms"))
        time.sleep(2)
        console.print("type:             [yellow]comand[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]coms[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__coms[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--coms[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
    elif in__action == "--coms .info" or in__action == "--Coms .info":
        console.print("[yellow]coms[/yellow] - команда отображающая все доступные к использванию команды, которые работают только в оболочке.")
        console.print("name           [yellow]coms[/yellow]")
        console.print("module         [yellow]main__system__coms[/yellow]")
    elif in__action == "--stat" or in__action == "--Stat":
        main__system__stat()
    elif in__action == "--stat .stat" or in__action == "--Stat .stat":
        console.print("Введённая вами команда невыполнима. Нельзя посмотреть статус статуса.")
        print(Panel.fit("[red]xion.main__system__stat[/red], arg:   [yellow].stat[/yellow]", title="[red]Erorr"))
    elif in__action == "--stat .info" or in__action == "--Stat .info":
        console.print("[yellow]stat[/yellow] - команда отображающая все доступные модули. Модуль - это функция в коде, которая отвечает за выполнение той или иной команды.")
        console.print("name           [yellow]stat[/yellow]")
        console.print("module         [yellow]main__system__stat[/yellow] <- Пример модуля.")
    elif in__action == "--title" or in__action == "--Title":
        main__system__title()
    elif in__action == "--ver" or in__action == "--Ver":
        main__system__ver()
    elif in__action == "--ver .stat" or in__action == "--Ver .stat":
        print(Panel.fit("Загрузка статуса",title="com: ver"))
        time.sleep(2)
        console.print("type:             [yellow]comand[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]ver[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__ver[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--ver[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
        time.sleep(1)
        console.print("[yellow]xion.main__system__ver[/yellow] have information by [yellow]xion.main__system__ver.stat[/yellow]")
        time.sleep(1)
        console.print("Upload...")
        time.sleep(2)
        print(Panel.fit("[white on green]Актуальная версия оболочки: 1v"))
        time.sleep(2)
    elif in__action == "--ver .info" or in__action == "--Ver .info":
        console.print("[yellow]ver[/yellow] - команда кратко отображающая версию оболочки.")
        console.print("name           [yellow]ver[/yellow]")
        console.print("module         [yellow]main__system__ver[/yellow]")
    elif in__action == "--sc" or in__action == "--Sc":
        main__system__sc()
    elif in__action == "--sc .stat" or in__action == "--Sc .stat":
        print(Panel.fit("Загрузка статуса",title="com: sc"))
        time.sleep(2)
        console.print("type:             [yellow]comand[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]sc[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__sc[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--sc[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
    elif in__action == "--sc .info" or in__action == "--Sc .info":
        console.print("[yellow]sc[/yellow] - команда очищающая консоль. Аналог cls.")
        console.print("name           [yellow]sc[/yellow]")
        console.print("module         [yellow]main__system__sc[/yellow]")
    elif in__action == "RESET":
        main__system__RESET()
    elif in__action == "RESET .stat":
        print(Panel.fit("Загрузка статуса",title="com: RESET"))
        time.sleep(2)
        console.print("type:             [yellow]comand[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]RESET[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__RESET[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]RESET[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
    elif in__action == "--RESET .info" or in__action == "--RESET .Info":
        overflow_methods = ["Пояснение к RESET"]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="yellow")
            console.print("Написание производится строго заглавными буквами, потому что именно когда вы пишите заглавными буквами, вы потверждаете что действительно хотите сделать перезагрузку.")
    elif in__action == "--exit" or in__action == "--Exit" or in__action == "--quit" or in__action == "--Quit":
        pyautogui.press("F11")
        exit()
    elif in__action == "--exit .stat" or in__action == "--Exit .stat" or in__action == "--quit .stat" or in__action == "--Quit .stat":
        print(Panel.fit("Загрузка статуса",title="com: exit/quit"))
        time.sleep(2)
        console.print("type:             [yellow]comand[/yellow]")
        time.sleep(0.7)
        console.print("name:             [yellow]exit/quit[/yellow]")
        time.sleep(0.7)
        console.print("init:             [yellow]xion.main__system__exit;[/yellow]")
        console.print("                  [yellow]xion.main__system__quit[/yellow]")
        time.sleep(0.7)
        console.print("shell:            [yellow]xion[/yellow]")
        time.sleep(0.7)
        console.print("ver.shell:        [yellow]1[/yellow]")
        time.sleep(0.7)
        console.print("typewrite:      [yellow]--exit; --quit[/yellow]")
        time.sleep(0.7)
        console.print("status:           [black on green]Ok")
    elif in__action == "--exit .info" or in__action == "--Exit .info" or in__action == "--quit .info" or in__action == "--Quit .info":
        console.print("[yellow]exit[/yellow] - команда отображающая все доступные к использванию команды, которые работают только в оболочке.")
        console.print("name           [yellow]exit[/yellow]")
        console.print("module         [yellow]main__system__exit[/yellow]; [yellow]main__system__quit[/yellow]")
    else:
        console.print("[red]Неверно введена команда!")

def load(login__reg):
    for i in tqdm(range(100), desc='Enter to shell...   ', unit=' ticrate'):
        time.sleep(0.03)
    os.system("cls")
    preload__menu()
    message = print(Panel.fit("Добро пожаловать в оболочку " + login__reg + "!", title="[green]Enter is successfully![/green]"))
    time.sleep(3)
    os.system("cls")
    console__title()
    xion__main__system()

def auth(login__reg):
    password = input("Пароль от Аккаунта: ")
    if password == "sha256":
        overflow_methods = ["succeccfully"]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="bold green")
            console.print()
        load(login__reg)
    else:
        print("Неверно введён пороль!")
        auth(login__reg)

def user():
    login__reg = input("Имя пользователя: ")
    if login__reg == "admin":
        auth(login__reg)
    else:
        print("Неверное имя пользователя!")
        user()

auth__autoentry()
user()
while True:
    xion__main__system()
