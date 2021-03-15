
import requests
from bs4 import BeautifulSoup
import collections
import csv
import re

u = []
a = []
b = []


def generateCsv(urls,text,occ):
    with open('Output.csv', mode='w') as csv_file:
        fieldnames = ['Href', 'Anchor Text', 'Occurance']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        l = len(urls)
        for i in range(l):
            writer.writerow({'Href': urls[i], 'Anchor Text': text[i], 'Occurance': occ[i]})



def createCsv(urls):
    url = urls
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
   
    for link in soup.find_all('a'):
        u.append(link.get('href'))
        s=link.text
        a.append(s)

    # elements_count = collections.Counter(a)
    for i in a:
        count = 0
        for j in a:
            if i == j:
                count += 1
        b.append(count)
    # print(len(b))


with open("req.txt") as file:
    for line in file:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        for i in urls:
            print(i)
            createCsv(i);


generateCsv(u,a,b);
    
