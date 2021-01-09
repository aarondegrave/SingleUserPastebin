import requests
from bs4 import BeautifulSoup
import urllib.request
from random import randint
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('username', help="the username of the pastebin account", type=str)
args = parser.parse_args()


def func():
  check_against = []
  while True:
    time.sleep(1)
    page = 'https://pastebin.com/u/' + args.username
    html = requests.get(page).text
    bs = BeautifulSoup(html)
    plinks = bs.find_all('a')
    links = []
    for link in plinks:
      a = link.has_attr('href')
      if a:
        links.append(link.attrs['href'])
        with open('test.txt', 'w') as c:
          c.write(str(links))
    n = 9
    if check_against == links:
      continue
    else:
      for item in links:
        try:
          link_to_download = links[n]
          final_link = "https://pastebin.com/raw" + link_to_download
          unique = randint(1,100000)
          urllib.request.urlretrieve(final_link, 'info' + str(unique) + '.txt')
          n = n + 2
        except Exception:
          continue
    for item in links:
      check_against.append(item)
func()