import csv
import multiprocessing as mp
# self script
import tool

def save_img(name, url):
    print(name)
    icon_folder = '../data/icon/'
    res = tool.get_source(url).content
    with open('{}{}.jpg'.format(icon_folder, name), 'wb') as f:
        f.write(res)

if __name__ == '__main__':
    csv_file = '../data/csv/google_play_with_img.csv'
    with open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    tasks = [(i, d['img_url'], ) for i, d in enumerate(data) if d['img_url']]
    print(len(tasks))

    pool = mp.Pool(processes=12)
    pool.starmap(save_img, tasks)
    # save_img(0, data[0]['img_url'])
