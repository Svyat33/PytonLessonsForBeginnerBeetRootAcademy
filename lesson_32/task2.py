import json
import requests
import urllib.request


if __name__ == "__main__":
    url = urllib.request.urlopen('https://api.pushshift.io/reddit/comment/search/')
    obj = json.load(url)
    with open('data.json', 'w') as outfile:
        i = 0
        store = []
        while i < 10:
            obj1 = obj['data'][i]['author']
            obj2 = obj['data'][i]['body']
            store.append({'author': obj1, 'comments': obj2})
            print("Author: {}\nComments: {}\n{:*^50}".format(obj1, obj2, 'next comment'))
            i += 1
        json.dump(store, outfile)
