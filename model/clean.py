import csv, json
import os
import random

def loadCSV(csv_file):
    with open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data
def loadJSON(json_file):
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)
    return data

def makeJSON(csv_file, json_file):
    random.seed(1340)
    data = loadCSV(csv_file)
    # installs = set(d['Installs'].replace(',','').replace('+','') for d in data)

    for i, d in enumerate(data):
        if random.randint(1, 100) < 60:
            d['partition'] = 'train'
        else:
            d['partition'] = 'test'
        d['index'] = i
        d['Installs'] = d['Installs'].replace(',','').replace('+','')

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def split_image():
    folders = ['0','1','5','10','50','100','500','1000','5000','10000','50000','100000','500000','1000000','5000000','10000000','50000000','100000000','500000000','1000000000']
    for f in folders:
        os.makedirs('../data/icon/{}/'.format(f), exist_ok=True)

    # data
    data = loadJSON(json_file)

    for d in data:
        if d['app_id'] == 'fail':
            continue
        src = '../data/icon/{}.jpg'.format(d['index'])
        dest = '../data/icon/{}/{}.jpg'.format(d['Installs'], d['index'])

        os.rename(src, dest)

def split_image2():
    folders = ['0','1','5','10','50','100','500','1000','5000','10000','50000','100000','500000','1000000','5000000','10000000','50000000','100000000','500000000','1000000000']
    for partition in ['train', 'test']:
        os.makedirs('../data/icon/{}/'.format(partition), exist_ok=True)
        for f in folders:
            os.makedirs('../data/icon/{}/{}/'.format(partition, f), exist_ok=True)

    # data
    data = loadJSON(json_file)

    for d in data:
        if d['app_id'] == 'fail':
            continue

        src = '../data/icon/{}/{}.jpg'.format(d['Installs'], d['index'])
        dest = '../data/icon/{}/{}/{}.jpg'.format(d['partition'], d['Installs'], d['index'])

        os.rename(src, dest)

if __name__ == '__main__':
    csv_file = '../data/csv/google_play_with_img.csv'
    json_file = '../data/json/google_play_all.json'
    # makeJSON(csv_file, json_file)
    # split_image()
    # split_image2()
