#TODO: Standardize parser library

import re


def parse_wiki(page):
    #the model eg. Acer A500
    name = re.findall('<th style.*>(\w+[A-Za-z0-9- ]*)</a', page)
    #The name of the stat eg. model
    header = re.findall('<th.*>(\w+[A-Za-z0-9- ]*)</', page)
    #The spec eg. 1.0 GHz
    spec = re.findall('<td.*>([A-Za-z0-9- ]*)</[span]?', page)
    for x in range(0, len(name)):
        post = "{" + header[0] + ":"
        post = post + " " + name[x]
        for y in range(0, len(spec) // len(name)):
            post = post + ",\n" + header[y + 1] + ":" + " "
            post = post + spec[x * (len(spec) // len(name)) + y]
        print(post)


def parse_ebay(self):
    pass