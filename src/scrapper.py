#!/usr/bin/python
# encoding=utf-8

import json
import requests

from collections.abc import Iterable
from bs4 import BeautifulSoup

class website:
    def __init__(self, url):
        self.url = url
        self.request = requests.get(url)
        self.textohtml = self.request.text
        self.soup =  BeautifulSoup(self.textohtml, "html.parser")
    def print(self) -> None:
        print('[' + self.url + ']: ' + self.textohtml)

class scrapper:
    def __init__(self, urls):
        self.parsedUrls = []
        self.urls = urls
        for url in urls:
            self.parsedUrls.append(website(url))
    def scrap(self) -> Iterable:
        output = []
        return output
    def print(self) -> None:
        for url in self.parsedUrls:
            url.print()

result = scrapper(['https://nogueivi.github.io'])
result.print()
