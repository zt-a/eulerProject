# https://euler.jakumo.org/problems/view/1.html
import requests
from bs4 import BeautifulSoup

def getTasks():
    try:
        for i in range(1, 51 + 1):
            print('[+] GET URL')
            url = f'https://euler.jakumo.org/problems/view/{i}.html'
            print(f'[URL]: {url}')
            print('[+] GET SRC')
            src = requests.get(url=url).text
            soup = BeautifulSoup(src, 'lxml')
            print('[+] GET BLOCK')
            mainBlock = soup.find("div", {'id': 'mainPage'})
            print('[+] GET CONTENT')

            numTask = mainBlock.find("div", {'class': 'modTitle'}).text
            print('[+] GET TITLE')
            titleTask = mainBlock.find("div", {'class': 'probTitle'}).text
            print('[+] GET PROBLEM')
            contentTask = mainBlock.find("div", {'class': 'problem_content'}).text
            print('[!] GET RESULTS')

            print('-' * 50)
            numberFile = numTask.split(' ')[-1]

            print('-' * 20, 'CREATE PYTHON FILE', '-' * 20)
            with open(f'tasks/task{numberFile}.py', 'w', encoding='utf-8') as file:
                file.write(f"'''\n{numTask}\n"
                           f"{titleTask}"
                           f"{contentTask}'''")

    except Exception as ex:
        print(f'[-]Error: {ex}')

    try:
        for i in range(52, 821 + 1):
            print('[+] GET URL')
            url = f'https://euler.jakumo.org/problems/view/{i}.html'
            print(f'[URL]: {url}')
            print('[+] GET SRC')
            src = requests.get(url=url).text
            soup = BeautifulSoup(src, 'lxml')
            print('[+] GET BLOCK')
            mainBlock = soup.find("div", {'id': 'mainPage'})
            print('[+] GET CONTENT')

            numTask = mainBlock.find("div", {'class': 'modTitle'}).text
            print('[+] GET TITLE')
            titleTask = mainBlock.find("div", {'class': 'probTitle'}).text
            print('[+] GET PROBLEM')
            contentTask = mainBlock.find("div", {'class': 'problemsItem'}).text
            print('[!] GET RESULTS')

            print('-' * 50)
            numberFile = numTask.split(' ')[-1]

            print('-' * 20, 'CREATE PYTHON FILE', '-' * 20)
            with open(f'tasks/task{numberFile}.py', 'w', encoding='utf-8') as file:
                file.write(f"'''\n{numTask}\n"
                           f"{titleTask}"
                           f"{contentTask}'''")

    except Exception as ex:
        print(f'[-]Error: {ex}')


def main():
    print('-'*20, 'START', '-'*20)
    getTasks()
    print('-'*20, 'FINISH', '-'*20)


if __name__ == '__main__':
    main()