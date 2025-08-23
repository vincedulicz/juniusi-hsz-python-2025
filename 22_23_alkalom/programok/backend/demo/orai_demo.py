import requests
from bs4 import BeautifulSoup

def bs_test(soup):
    title = soup.find('h1') # első h1 tag
    if title:
        print("title: ", title.text)

    ps = soup.find_all('p') # minden tag p <p>/
    for p in ps:
        print(p.text)

    first_h1 = soup.find('h1')
    next_elem = first_h1.find_next() if first_h1 else None

    link = soup.find('a')
    pararent_div = link.find_parent('div')

    first_div = soup.find('div')
    if first_div:
        prev_p = first_div.find_all_previous('p')
        for p in prev_p:
            print(p.text)

def login_to_website():
    session = requests.Session()

    login_url = "https://example.com/login"
    cred = {"username": "user", "password": "pass"}

    response = session.post(login_url, data=cred)

    if response.status_code == 200:
        print("login sucess")
    else:
        print("login failed")

    profile_url = ".../profile"
    profile_resp = session.get(profile_url)

    # [...]

    profile_resp.text()

