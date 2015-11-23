from requests import Session, get
from bs4 import BeautifulSoup as Soup
from sys import version as pyVersion
from cookielib import LWPCookieJar
import re
import os

if 'PyPy' in pyVersion:
    BS_PARSER = r'html.parser'
else:
    BS_PARSER = r'lxml'

class ProjectEuler(object):
    def __init__(self, cookieFile = "COOKIES"):
        self.cookieFile = cookieFile
        self.s = self.getSession()
        self.login()

    def getSession(self):
        s = Session()
        s.headers.update({'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'})
        s.cookies = LWPCookieJar(self.cookieFile)  
        if os.path.exists(self.cookieFile):
            s.cookies.load()
        return s

    def isLogin(self, page):
        return "Logged in as" in page.text

    def login(self):
        s = self.s
        url = "https://projecteuler.net"
        page = s.get(url)
        if self.isLogin(page):
            return True
        for _ in range(5):
            page = s.get(r"https://projecteuler.net/sign_in")
            print "Enter your username:",
            usr = raw_input()
            print "Enter your password:",
            pwd = raw_input()
            captcha = s.get("https://projecteuler.net/captcha/show_captcha.php")
            tmpfile = r'captcha.png'
            f = open(tmpfile, 'wb')
            f.write(captcha.content)
            f.close()
            os.startfile(tmpfile)
            print "Enter the captchar:",
            code = re.findall(r'\d{5}', raw_input())[0]
            os.remove(tmpfile)
            data = {'captcha': code, 'password': pwd, 'remember_me': 1, 'sign_in': "Sign In", 'username': usr}
            page = s.post(url=r"https://projecteuler.net/sign_in", data = data)
            if self.isLogin(page):
                s.cookies.save()
                return True
        return False

    def getSolvedProblems(self):
        def clean(p):
            return int(re.findall(r"\d+", p.div.get_text())[0])
        s = self.s
        url = r"https://projecteuler.net/progress"
        page = s.get(url)
        soup = Soup(page.text, BS_PARSER)
        raw = soup('td', class_="problem_solved")
        return map(clean, raw)

def getTitle(n):
    print "Getting Problem "+str(n)+"'s title"
    url = r"https://projecteuler.net/problem="+str(n)
    try:
        page = get(url)
    except:
        return None
    soup = Soup(page.text, BS_PARSER)
    return soup('div', id='content')[0].h2.get_text()

if __name__ == "__main__":
    pe = ProjectEuler()
    print pe.getSolvedProblems()
