
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import subprocess
import functools

from Parser.ExseptionsParserTrain import connection_terminated


HOST = 'https://www.tutu.ru/msk/'

flag = 0x08000000  # No-Window flag
webdriver.common.service.subprocess.Popen = functools.partial(
    subprocess.Popen, creationflags=flag)


def get_site_with_browser(url, station_1='', station_2=''):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 '
                           'Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile '
                           'Safari/537.36')
    options.headless = True

    try:
        browser = webdriver.Firefox(
            executable_path=r'C:\Users\Admin\PycharmProjects\TrainSchedule\Parser\Drivers\geckodriver.exe',
            service_log_path=os.devnull,
            options=options
        )

        browser.get(url)

        time.sleep(3)
        input_departure = browser.find_element_by_xpath('//*[@id="searchDepartureStationName"]').send_keys(station_1)

        time.sleep(3)
        input_arrive = browser.find_element_by_xpath('//*[@id="searchArrivalStationName"]').send_keys(station_2)

        time.sleep(5)
        button = browser.find_element_by_xpath(
            '/html/body/div[5]/div[2]/noindex/form/div/table/tbody/tr/td[7]/div/button/span[1]').click()

        time.sleep(5)

        with open('index.html', 'w', encoding='utf-8') as file:
            src = file.write(browser.page_source)
            return src

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()


def read_html():

    with open('index.html', 'r', encoding='utf-8') as file:
        html = file.read()

        return html


def parser(station_1, station_2):
    try:
        print(f'<START>: Starting parser {HOST}')

        get_site_with_browser(HOST, station_1, station_2)

        html = read_html()

        soup = BeautifulSoup(html, 'lxml')
        find_cards_trains = soup.find_all('div', class_='mobile__card__1wm2v')

        info = []

        for elem in find_cards_trains:
            test = elem.find('div', class_='mobile__price__a9w90')
            if test is not None:
                info.append(
                    {
                        'Departure': elem.find('div', class_='mobile__time__17sp3 mobile__depTime__nbGbJ').text.strip(),
                        'Arrival': elem.find('div', class_='mobile__time__17sp3 mobile__arrTime__2ALes').text.strip(),
                        'Path': elem.find('span', class_='mobile__route__bd86h').text.strip(),
                        'Price': test.find('span').get_text()
                    }
                )
        
        print(f'<END>: Ending parser {HOST}')
        if info:
            return info
        else:
            soup = BeautifulSoup(html, 'lxml')
            find_block = soup.find('div', class_='b-ls')

            title_block = find_block.find('div', class_='titleBlock').text.strip()
            station_select = find_block.find('p').text.strip()

            error = title_block + '\n' + station_select

            print(error)
            return error

    except Exception as ex:
        print(ex)
        error = connection_terminated()
        return error


def get_title_page():
    try:
        get_html = read_html()

        soup = BeautifulSoup(get_html, 'lxml')

        find_title = soup.find('h1', class_='t-ttl_second').text
        if find_title:

            print(f'<TITLE PAGE>: {find_title}')

            return find_title
        else:
            print('Not find title')
    except Exception as ex:
        print(ex)
