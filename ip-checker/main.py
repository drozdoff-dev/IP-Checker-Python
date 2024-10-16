# pyinstaller --add-data "D:\languages\python\python 3.10\Lib\site-packages\pyfiglet;./pyfiglet" -F -i "C:\Users\Mexpy\Desktop\ip-checker/icon.ico" main.py
#
# Это команда для компилирования в exe с библиотекой pyfiglet

import requests
from pyfiglet import Figlet, fonts, FigletFont
import folium
from colorama import init, Fore, Back, Style
import os
import msvcrt, sys
init()

path = os.getcwd()
paths = os.getcwd() + '/checked/'

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Страна]': response.get('country'),
            '[Код страны]': response.get('countryCode'),
            '[Город]': response.get('city'),
            '[Номер региона]': response.get('region'),
            '[Имя региона]': response.get('regionName'),
            '[Долгота]': response.get('lon'),
            '[Широта]': response.get('lat'),
            '[Провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
            '[Временная зона]': response.get('timezone'),
            '[Почтовый код]': response.get('zip'),
        }

        for k, v in data.items():
            print(Fore.CYAN + f'{k} ' + Fore.WHITE + ':' + ' ' + Fore.YELLOW + f'{v}')

        print(Fore.GREEN + '\n[OK] ' + Fore.WHITE + 'Информация спизжена успешно!')
        print(Style.RESET_ALL)

        if not os.path.exists('checked'):
            os.mkdir('checked')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(paths + f'{response.get("query")}_{response.get("city")}.html')

        print(Fore.GREEN + Style.BRIGHT + f'\nВ корневной директории программы, по пути [' + paths + f'{response.get("query")}_{response.get("city")}.html] Была сохранена карта местоположения данного IP адреса.')
        print(Style.RESET_ALL)
        print('Нажмите любую клавишу, чтобы закрыть окно.')

    except requests.exceptions.ConnectionError:
        print(Fore.RED + '\n[!] ' + Fore.WHITE + 'Проверьте пожалуйста ваше соединение.')
        print(Style.RESET_ALL)


def main():
    preview_text = Figlet(font='slant')
    print(Fore.RED + preview_text.renderText('MEXPY'))
    print(Style.RESET_ALL)
    ip = input('Пожалуйста введите IP-адрес: ')

    print('\n')
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()

key=msvcrt.getch()
if key==b'\r':
    sys.exit(0)