import requests

def get_random_cat_link():
    response = requests.get('https://aws.random.cat/meow')
    cat_json = response.json()
    return cat_json['file']

def get_random_dog_link():
    response = requests.get('https://random.dog/woof.json')
    dog_json = response.json()
    return dog_json['url']