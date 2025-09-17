import requests
from bs4 import BeautifulSoup
import os


def getTasks():
    os.makedirs("tasks", exist_ok=True)

    for i in range(1, 851 + 1):
        try:
            print('[+] GET URL')
            url = f'https://euler.jakumo.org/problems/view/{i}.html'
            print(f'[URL]: {url}')
            print('[+] GET SRC')

            src = requests.get(url).text
            soup = BeautifulSoup(src, 'html.parser')

            print('[+] GET CONTENT')

            # Номер задачи
            numTask = soup.find("h3", class_="problem-info").get_text(strip=True)

            # Название задачи
            titleTask = soup.find("h2").get_text(strip=True)

            # Содержимое задачи
            contentTask = soup.find("div", class_="problem_content").get_text("\n", strip=True)

            print('[!] GET RESULTS')

            print('-' * 50)
            numberFile = numTask.split(' ')[-1]  # "Задача 1" -> "1"

            print('-' * 20, 'CREATE PYTHON FILE', '-' * 20)
            with open(f'tasks/task{numberFile}.py', 'w', encoding='utf-8') as file:
                file.write(f"'''\n{numTask}\n{titleTask}\n\n{contentTask}\n'''")

        except Exception as ex:
            print(f'[-] Error on task {i}: {ex}')


def main():
    print('-' * 20, 'START', '-' * 20)
    getTasks()
    print('-' * 20, 'FINISH', '-' * 20)


if __name__ == '__main__':
    main()
