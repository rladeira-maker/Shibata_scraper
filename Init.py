#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Init.py
#
#  Copyright 2023 Live session user <mint@mint>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from Scrape import scrape


def init(seed_url):
    browserBIN = '/usr/bin/firefox'
    options = Options()
    options.binary_location = browserBIN
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    service = Service(r'/home/mint/webscrap/geckodriver')
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(seed_url)
    driver.implicitly_wait(2)
    sleep(7)
    elem = driver.find_element(By.CSS_SELECTOR, ".lgpd--cookie-accept")
    elem.click()
    driver.implicitly_wait(2)
    sleep(7)
    return driver

