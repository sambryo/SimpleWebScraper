from urllib import urlopen 
import os 
import sys
import strings 
import praw #github.com/praw-dev/praw



def download_and_save(url, filename, directory_data): 
    data = urlopen(url).read()
    if is_duplicate(data, directory_data):
        return 
    with open(filename, mode='wb') as output: 
        output.write(data)

def is_duplicate(data, directory_data): 
    h = hash(data)
    if h in directory_data: 
        with open(directory_data[h]) as fid: 
            existing_data = fid.read()
        return existin_data == data
    return False

def scan_hash(direname): 
    sub_items = os.listdir(dirname)
    filename = (os.path.join(dirname, f) for f in sub_items)
    filename = (f for f in filename if not os.path.isdir(f))
    data = {}
    for f in filename: 
        with open(f) as fid:
            data[hash(fid.read())] = f
    return data

#def scrape()
