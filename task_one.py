import requests


def best_hero(url, heroes):
    dict_intell = dict()
    default_intell = 0
    best_hero = ''

    for i in heroes:
        url_request = url + i
        resp = requests.get(url=url_request)
        param_hero = resp.json()
        param_id = param_hero['results'][0]['powerstats']['intelligence']
        print(f'У супергероя {i[:-1]} интеллект - {param_id}')
        dict_intell[i[:-1]] = param_id

    for name, intell in dict_intell.items():
        if int(intell) > default_intell:
            default_intell = int(intell)
            best_hero = name

    print(f'Самый высокий интеллект у героя {best_hero}!')


url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes = ['Hulk/', 'Captain America/', 'Thanos/']
best_hero(url, heroes)