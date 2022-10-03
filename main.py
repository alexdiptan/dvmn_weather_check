import requests


def get_weather(city: str, language: str = 'en') -> str:
    payload = {"MmnTq": "", "lang": language}
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    cities = ['череповец', 'london', 'аэропорт шереметьево']
    for city in cities:
        print(get_weather(city, 'ru'))
