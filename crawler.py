from bs4 import BeautifulSoup
import os
import requests
from urllib.request import Request, urlopen

def copysol(link, quest):
    print("copysol")
    source_code = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    text = urlopen(source_code).read()
    soup = BeautifulSoup(text, 'html.parser')
    tag = soup.ol
    filename = quest + ".txt"
    f = open(filename, 'a')
    f.write('\n')
    for item in tag.findAll('li'):
        f.write(item.text)
        f.write('\n')
    f.close()


def ext_solution(link, quest):
    url=link
    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.findAll('a', {'class':None}):
        href=link.get('href')
        if(href.count('viewsolution')==1):
            nlink = "https://www.codechef.com"+href
            copysol(nlink, quest)
            break


def crawler(username):
    try:
        os.mkdir(username)
        os.chdir(username)
    except(Exception):
        os.chdir(username)
    url="https://www.codechef.com/users/"+username
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a', {'class':None}):
        href=link.get('href')
        quest = link.text
        if(href.count('status')==1):
            link = ("https://www.codechef.com"+(href))
            ext_solution(link, quest)


username=input("Enter your CodeChef's username: ")
crawler(username)