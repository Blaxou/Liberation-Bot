import re

import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
http = urllib3.PoolManager()


class Parser(object):
    """
This parser parses liberations from college Sismondi's website
    """

    def __init__(self):
        self.regexp = '([1-4])([A-Z]{2})(\d)?(?:\.)(DF|OS|OA|OC)(\d{2}) (H\d+)?-?(H\d+)?(.*)'
        self.lesson_regexp = '(\d)([A-Z]{2})(\d)?(?:\.)(DF|OS|OA|OC)(\d{2})'

    def get_page(self):
        url = "https://cours.sismondi.ch/ecran-1/affichage_open"
        with http.request('GET', url, preload_content=False) as f:
            self.soup = BeautifulSoup(f, "html.parser")

    def parse_page(self):
        librs = []
        for el in self.soup.find_all('div', 'slide-ecran-content'):
            res = self.isLibr(el)
            if res:
                librs.append(res)
        self.librs = librs

    def isLibr(self, el):
        header = el.find('h2', 'jou')
        text = el.find('div', 'field')
        if not header or not text:
            return
        header = header.get_text()
        text = text.get_text().rstrip()
        if text == '':
            return
        for line in text.split('\n'):
            m = self.match_libr(line)
            if m:
                return {'text': line, 'groups': m.groups(), 'header': header}

    def match_libr(self, text):
        return re.compile(self.regexp).match(text)

    def check(self):
        self.get_page()
        return self.parse_page()


if __name__ == '__main__':
    p = Parser()
    p.check()
    print(p.librs)
