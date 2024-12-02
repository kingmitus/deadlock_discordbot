import requests 
import random

#no key neccesary for this data

url = f'https://data.deadlock-api.com/docs#/'
url2 = f'https://analytics.deadlock-api.com/docs#/'

def patch_notes():
    print(url/v1/patch-notes)

def builds():
    print(url/v1/builds)

def hero_id():
    print(url2/v2/hero)


def hero_items():
    id = (input('enter a hero id: '))
    print(url2/v2/hero/{id}/item-win-loss-stats)

def random_hero(builds):
    heros = [hero_id()]
    bam = random.choice(heros)
    return bam

def random_build(builds):
    hero_build = []
    for hero in builds:
        hero_build.append(hero)
    new_build = random.choice(hero_build)
    print(new_build)

