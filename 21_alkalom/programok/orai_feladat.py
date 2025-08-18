import requests

def i_fel():
    response = requests.get("https://httpbin.org/get")
    print(response.json())

def ii_fel():
    params = {"name": "Student", "course": "Python"}
    response = requests.get("https://httpbin.org/get", params=params)
    print(response.json())

def iii_fel():
    data = {"title": "Hello", "message": "World"}
    response = requests.post("https://httpbin.org/post", json=data)
    print(response.json())

def iv_fel():
    headers = {"Authorization": "Bearer token123", "Custom-Header": "MyValue"}
    response = requests.get("https://httpbin.org/headers", headers=headers)
    print(response.json())

def v_fel():
    response = requests.get("https://httpbin.org/ip")
    print(response.json())

def vi_fel():
    try:
        response = requests.get("https://httpbin.org/delay/3", timeout=2)
        print(response.json())
    except requests.exceptions.Timeout:
        print("Időtullépés")

def vii_fel():
    response = requests.get("https://httpbin.org/redirect/2", allow_redirects=True)
    print("végső url:", response.url)

def viii_fel():
    auth = ("user", "pass")
    response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=auth)
    print(response.status_code, response.json())

def ix_fel():
    status_code = [200, 404, 500]
    for code in status_code:
        response = requests.get(f'https://httpbin.org/status/{code}')
        print(f'státuszkód: '
              f'{response.status_code} - '
              f'{"Sikeres" if response.ok else "Hiba"}')

def x_fel():
    with requests.Session() as session:
        session.get("https://httpbin.org/cookies/set?cokie_name=cookie_value")
        cookie_response = session.get("https://httpbin.org/cookies/")
        print(cookie_response.json())

# print(globals())

def main():
    fel_cuntions = [func for name, func in globals().items()
                    if name.endswith("_fel") and callable(func)]

    for func in fel_cuntions:
        print(f'Meghívva: {func.__name__}')
        func()

# main()


feladatok = []

def feladat(func):
    feladatok.append(func)
    return func

@feladat
def elso_fel():
    print("első feladat fut!...")

@feladat
def masodik_fel():
    print("2. fel")

def main_():
    for func in feladatok:
        print(f"meghívva {func.__name__}")
        func()

main_()