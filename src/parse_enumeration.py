from bs4 import BeautifulSoup
import sys
import json

def parse_enumerations(f):
    soup = BeautifulSoup(f)
    unordered = soup.find('ul')
    ordered = soup.find('ol')
    items = unordered.find_all('li')
    ritems = []
    for it in items:
        ritems.append(it.getText())
    return ritems


def main():
    f = sys.stdin
    print json.dumps(parse_enumerations(f))

if __name__ == "__main__":
    main()
