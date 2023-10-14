# Python 3.7.5 64x
# [encoding = 'utf-8'] INFO: Use this fragment of code for supported Russian Laguage in files.
# console = Console(width=63)
# xsf = Xion Shell File
# scf = Shell Configuration File

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
os.system("title Xion. Version: v2[debug__mode: on]")
pyautogui.press("F11")

console = Console(width=63)
print(Panel.fit("Добро пожаловать в [yellow]Xion[/yellow]! Для продолжения войдите в систему.", title="Система"))

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
  console.print(Panel.fit("[blue]Xion[/blue] by Usersoft Incorpareted 2023-2025. Version [green]v2[/green] commands for begin: [yellow]--list[/yellow]; [yellow]--coms[/yellow]; [yellow]--ver[/yellow]; [yellow]--ver .stat[/yellow]"))

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
    console.print("[INFO]23x1: User entered [yellow]login_reg[/yellow] and [yellow]password_reg[/yellow]")
    time.sleep(1)
    console.print("[INFO]23x2: Entred is succeccfully! Get info...")
    console.print("[INFO]23x3: login: [green]admin[/green]; password:[green]******[/green]")
    console.print("[INFO]23x4: [yellow]main__system__status[/yellow] in [yellow]xion.main__system[/yellow] have info by [yellow]xion.main__system__status.info[/yellow]")
    console.print("[INFO]23x5: uploading modules from [yellow].main__system[/yellow]; com:  [yellow]--stat[/yellow]")
    time.sleep(2)
    console.print("[XION.MODULE][yellow]xion.main__system__list[/yellow]")
    time.sleep(0.7)
    console.print("[XION.MODULE][yellow]xion.main__system__licence[/yellow]")
    time.sleep(0.7)
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
    console.print("[INFO]23x6: uploading modules from [yellow]xion__xionnet[/yellow]...")
    time.sleep(2)
    console.print("[NET.MODULE][yellow]xion.main__xionnet__storeFilesLicence[/yellow]")
    time.sleep(0.7)
    console.print("[NET.MODULE][yellow]xion.main__xionnet__storeFilesReadme[/yellow]")
    time.sleep(0.7)
    console.print("[NET.MODULE][yellow]xion.main__xionnet__storeFilesPi[/yellow]")
    time.sleep(3)
    func__screenclear()

# Xionnet modules
def main__xionnet__storeFilesLicence():
    func__screenclear()
    print(Panel.fit("| Файл [yellow]licence.xsf[/yellow] |"))
    overflow_methods = [""]
    for overflow in overflow_methods:
        console.rule(overflow)
        console.print(style="yellow")
        console.print("")
        licence_open = open("C:\\xion\\builds\\v2\\store_files\\licence.xsf", 'r')
        screen_view = licence_open.read()
        print(screen_view)
        overflow_methods = [""]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="yellow")
            console.print("")
def main__xionnet__storeFilesReadme():
    func__screenclear()
    print(Panel.fit("| Файл [yellow]readme.xsf[/yellow] |"))
    overflow_methods = [""]
    for overflow in overflow_methods:
        console.rule(overflow)
        console.print(style="yellow")
        console.print("")
        licence_open = open("C:\\xion\\builds\\v2\\store_files\\readme.xsf", 'r', encoding = 'utf-8')
        screen_view = licence_open.read()
        print(screen_view)
        overflow_methods = [""]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="yellow")
            console.print("")
def main__xionnet__storeFilesPi():
    func__screenclear()
    print(Panel.fit("| Файл [yellow]pi.xsf[/yellow] |"))
    overflow_methods = [""]
    for overflow in overflow_methods:
        console.rule(overflow)
        console.print(style="yellow")
        console.print("")
        print("")
        licence_open = open("C:\\xion\\builds\\v2\\store_files\\pi.xsf", 'r')
        screen_view = licence_open.read()
        print(screen_view)
        overflow_methods = [""]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="yellow")
            console.print("")

# Xion modules
def main__system__list():
    list = Tree("[yellow]файлы[/yellow] в директории [green]store_files[/green]:")
    list.add("licence.xsf")
    list.add("readme.xsf")
    list.add("pi.xsf")
    rprint(list)
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
  commands_open = open("C:\\xion\\builds\\v2\\store_files\\coms.scf", 'r', encoding = 'utf-8')
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
    console.print("build:   2023_v2")
    time.sleep(2)
def main__system__title():
  func__screenclear()
  console__title()
def main__system__ver():
  console.print("--[yellow]v2[/yellow]")
def main__system__sc():
  func__screenclear()
def main__system__RESET():
  print(Panel.fit("[white on blue]Вы действительно хотите перезагрузить оболочку?"))
  choice = input("Да(Y) или Нет(N)? --")
  if choice == "y" or choice == "Y":
      pyautogui.press("F11")
      console.print("[red on white]ПРОИЗОВОДИМ ПЕРЕЗАГРУЗКУ...")
      time.sleep(3)
      os.system('start C:\\xion\\builds\\v2\\main.py')
      exit()
  elif choice == "n" or choice == "N":
      xion__main__system()
  else:
      xion__main__system()

# Modules with arguments:

# .STAT
def main__system__list_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--list[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
def main__system__licence_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--licence[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
def main__system__readme_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--readme[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
def main__system__grph_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--grph[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
def main__system__coms_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--coms[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
def main__system__stat_stat():
    console.print("Введённая вами команда невыполнима. Нельзя посмотреть статус статуса.")
    print(Panel.fit("[red]xion.main__system__stat[/red], arg:   [yellow].stat[/yellow]", title="[red]Erorr"))
def main__system__ver_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--ver[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
    time.sleep(1)
    console.print("[yellow]xion.main__system__ver[/yellow] have information by [yellow]xion.main__system__ver.stat[/yellow]")
    time.sleep(1)
    console.print("Upload...")
    time.sleep(2)
    print(Panel.fit("[white on green]Актуальная версия оболочки: v2"))
    time.sleep(2)
def main__system__sc_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--sc[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
def main__system__RESET_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]RESET[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")
def main__system__quitexit_stat():
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
    console.print("ver.shell:        [yellow]2[/yellow]")
    time.sleep(0.7)
    console.print("typewrite:      [yellow]--exit; --quit[/yellow]")
    time.sleep(0.7)
    console.print("status:           [black on green]Ok")

# .INFO
def main__system__list_info():
    console.print("[yellow]list[/yellow] - команда отображающая список файлов хранящихся непосредственно в папке [green]store_files[/green]")
    console.print("name           [yellow]list[/yellow]")
    console.print("module         [yellow]main__system__list[/yellow]")
def main__system__licence_info():
    console.print("[yellow]licence[/yellow] - команда отображающая лицензию, её номер и краткое содержание информации об оболочке.")
    console.print("name           [yellow]licence[/yellow]")
    console.print("module         [yellow]main__system__licence[/yellow]")
def main__system__readme_info():
    console.print("[yellow]readme[/yellow] - команда открывающая [bold]readme.xsf[/bold] в [green]store_files[/green]. Краткая документация к оболочке.")
    console.print("name           [yellow]readme[/yellow]")
    console.print("module         [yellow]main__system__readme[/yellow]")
def main__system__grph_info():
    console.print("[yellow]grph[/yellow] - команда которая производит графический тест оболочки, для показания минимальных возомжностей.")
    console.print("name           [yellow]grph[/yellow]")
    console.print("module         [yellow]main__system__grph[/yellow]")
def main__system__coms_info():
    console.print("[yellow]coms[/yellow] - команда отображающая все доступные к использванию команды, которые работают только в оболочке.")
    console.print("name           [yellow]coms[/yellow]")
    console.print("module         [yellow]main__system__coms[/yellow]")
def main__system__stat_info():
    console.print("[yellow]stat[/yellow] - команда отображающая все доступные модули. Модуль - это функция в коде, которая отвечает за выполнение той или иной команды.")
    console.print("name           [yellow]stat[/yellow]")
    console.print("module         [yellow]main__system__stat[/yellow] <- Пример модуля.")
def main__system__ver_info():
    console.print("[yellow]ver[/yellow] - команда кратко отображающая версию оболочки.")
    console.print("name           [yellow]ver[/yellow]")
    console.print("module         [yellow]main__system__ver[/yellow]")
def main__system__sc_info():
    console.print("[yellow]sc[/yellow] - команда очищающая консоль. Аналог cls.")
    console.print("name           [yellow]sc[/yellow]")
    console.print("module         [yellow]main__system__sc[/yellow]")
def main__system__RESET_info():
    console.print("[yellow]RESET[/yellow] - команда для принудительной перезагрузки")
    console.print("name           [yellow]RESET[/yellow]")
    console.print("module         [yellow]main__system__RESET[/yellow]")
def main__system__quitexit_info():
    console.print("[yellow]exit[/yellow] - команда отображающая все доступные к использванию команды, которые работают только в оболочке.")
    console.print("name           [yellow]exit[/yellow]")
    console.print("module         [yellow]main__system__exit[/yellow]; [yellow]main__system__quit[/yellow]")

# .MODE
def main__system__list_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__licence_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Xionnet")
    console.print("Change:           [yellow]Required Xionnet[/yellow]")
def main__system__readme_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Xionnet")
    console.print("Change:           [yellow]Required Xionnet[/yellow]")
def main__system__grph_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__coms_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__stat_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__ver_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__sc_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__RESET_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")
def main__system__quitexit_mode():
    print(Panel.fit("Загружаем данные..."))
    time.sleep(1)
    console.print("Mode:             [black on green]Launch from Shell")
    console.print("Change:           [red]No Possibility.[/red]")

# Self xionnet
def xion__xionnet(xionctrl):
    func__screenclear()
    print(Panel.fit("Для вывода списка, введите [yellow]store_files[/yellow]"))
    while xionctrl == 1:
        xionnet__action = console.input("[xionnet]get.file-- ")
        if xionnet__action == "licence.xsf" or xionnet__action == "Licence.xsf":
            main__xionnet__storeFilesLicence()
        elif xionnet__action == "readme.xsf" or xionnet__action == "Readme.xsf":
            main__xionnet__storeFilesReadme()
        elif xionnet__action == "pi.xsf" or xionnet__action == "Pi.xsf":
            main__xionnet__storeFilesPi()
        elif xionnet__action == 'store_files' or xionnet__action == "Store_files":
            store_files = Tree("[green]STORE_FILES[/green], Доступные файлы:")
            store_files.add("Licence.xsf")
            store_files.add("Readme.xsf")
            store_files.add("Pi.xsf")
            rprint(store_files)
            console.print("Пользователь: admin, Сеть: Xionnet, Оболочка: Xion")
        elif xionnet__action == "xion" or xionnet__action == "Xion" or xionnet__action == "shell" or xionnet__action == "Shell":
            xionctrl = xionctrl - 1
            console.print("Покидаем Xionnet...")
            xion__main__system()
        else:
            console.print("[red]Файла " + xionnet__action + " не найдено.")

# Self shell
def xion__main__system():
    in__action = console.input("[green]$")
    if in__action == "--list" or in__action == "--List":
        main__system__list()
    elif in__action == "--list .stat" or in__action == "--List .stat":
        main__system__list_stat()
    elif in__action == "--list .info" or in__action == "--List .info":
        main__system__list_info()
    elif in__action == "--list .mode" or in__action == "--List .mode":
        main__system__list_mode()
    elif in__action == "--licence .stat" or in__action == "--Licence .stat":
        main__system__licence_stat()
    elif in__action == "--licence .info" or in__action == "--Licence .info":
        main__system__licence_info()
    elif in__action == "--licence .mode" or in__action == "--Licence .mode":
        main__system__licence_mode()
    elif in__action == "--readme .stat" or in__action == "--Readme .stat":
        main__system__readme_stat()
    elif in__action == "--readme .info" or in__action == "--Readme .info":
        main__system__readme_info()
    elif in__action == "--readme .mode" or in__action == "--Readme .mode":
        main__system__readme_mode()
    elif in__action == "--grph" or in__action == "--Grph":
        main__system__grph()
    elif in__action == "--grph .stat" or in__action == "--Grph .stat":
        main__system__grph_stat()
    elif in__action == "--grph .info" or in__action == "--Grph .info":
        main__system__grph_info()
    elif in__action == "--grph .mode" or in__action == "--Grph .mode":
        main__system__grph_mode()
    elif in__action == "--coms" or in__action == "--Coms":
         main__system__coms()
    elif in__action == "--coms .stat" or in__action == "--Coms .stat":
        main__system__coms_stat()
    elif in__action == "--coms .info" or in__action == "--Coms .info":
        main__system__coms_info()
    elif in__action == "--coms .mode" or in__action == "--Coms .imode":
        main__system__coms_mode()
    elif in__action == "--stat" or in__action == "--Stat":
        main__system__stat()
    elif in__action == "--stat .stat" or in__action == "--Stat .stat":
        main__system__stat_stat()
    elif in__action == "--stat .info" or in__action == "--Stat .info":
        main__system__stat_info()
    elif in__action == "--stat .mode" or in__action == "--Stat .mode":
        main__system__stat_mode()
    elif in__action == "--title" or in__action == "--Title":
        main__system__title()
    elif in__action == "--ver" or in__action == "--Ver":
        main__system__ver()
    elif in__action == "--ver .stat" or in__action == "--Ver .stat":
        main__system__ver_stat()
    elif in__action == "--ver .info" or in__action == "--Ver .info":
        main__system__ver_info()
    elif in__action == "--ver .mode" or in__action == "--Ver .mode":
        main__system__ver_mode()
    elif in__action == "--sc" or in__action == "--Sc":
        main__system__sc()
    elif in__action == "--sc .stat" or in__action == "--Sc .stat":
        main__system__sc_stat()
    elif in__action == "--sc .info" or in__action == "--Sc .info":
        main__system__sc_info()
    elif in__action == "--sc .mode" or in__action == "--Sc .mode":
        main__system__sc_mode()
    elif in__action == "--RESET .stat":
        main__system__RESET_stat()
    elif in__action == "--RESET .info" or in__action == "--RESET .info":
        main__system__RESET_info()
    elif in__action == "--RESET .mode" or in__action == "--RESET .mode":
        main__system__RESET_mode()
    elif in__action == "--exit" or in__action == "--Exit" or in__action == "--quit" or in__action == "--Quit":
        pyautogui.press("F11")
        exit()
    elif in__action == "--exit .stat" or in__action == "--Exit .stat" or in__action == "--quit .stat" or in__action == "--Quit .stat":
        main__system__quitexit_stat()
    elif in__action == "--exit .info" or in__action == "--Exit .info" or in__action == "--quit .info" or in__action == "--Quit .info":
        main__system__quitexit_info()
    elif in__action == "--exit .mode" or in__action == "--Exit .mode" or in__action == "--quit .mode" or in__action == "--Quit .mode":
        main__system__quitexit_mode()
    elif in__action == "--xionnet .mode" or in__action == "--Xionnet .mode":
        xionctrl = 1
        xion__xionnet(xionctrl)
    elif in__action == "RESET":
        main__system__RESET()
    else:
        console.print("[red]Команда " + in__action + " неправильно введена или не существует.")

def load(login__reg):
    for i in tqdm(range(100), desc='ВХОДИМ...   ', unit=' ПОДОЖДИТЕ'):
        time.sleep(0.03)
    os.system("cls")
    preload__menu()
    message = print(Panel.fit("Добро пожаловать в оболочку " + login__reg + "!", title="[green]Приветствие[/green]"))
    time.sleep(3.5)
    os.system("cls")
    console__title()
    xion__main__system()

def auth(login__reg):
    password = input("Пароль от Аккаунта: ")
    if password == "sha256":
        overflow_methods = ["ДОСТУП РАЗРЕШЁН. ПРОИЗВОДИМ ВХОД"]
        for overflow in overflow_methods:
            console.rule(overflow)
            console.print(style="white")
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
