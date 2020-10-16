""" Basically this parses html code and outputs tags using HTMLParser
This works on a file if you pass it in and just want to see the html tag details"""

from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for attr in attrs:
            if attr[1]:
                print(f'-> {attr[0]} > {attr[1]}')
            else:
                print(f'-> {attr[0]} > None')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for attr in attrs:
            if attr[1]:
                print(f'-> {attr[0]} > {attr[1]}')
            else:
                print(f'-> {attr[0]} > None')

    def handle_comment(self, data):
        # don't handle comments please
        pass
if __name__ == "__main__":
    parser = MyHtmlParser()
    Multi = []
    xp = open("hranktesttxt3.txt")
    for text in xp:
        parser.feed(text)

# -----------------------------------------------------
# This is another hackerrank version 
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {0}".format(tag))
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])
    def handle_endtag(self, tag):
        print("End   : {0}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print("Empty : {0}".format(tag))
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])
parser = MyHTMLParser()
n = int(input())
for i in range(n):
    parser.feed(input())

# This below version is my own but it didnd't pass the last test for some reason. If I add 
#for i in range(input()), parser.feed(input()) it worked fine :(

from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for attr in attrs:
            if attr[1]:
                print(f'-> {attr[0]} > {attr[1]}')
            else:
                print(f'-> {attr[0]} > None')    

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for attr in attrs:
            if attr[1]:
                print(f'-> {attr[0]} > {attr[1]}')
            else:
                print(f'-> {attr[0]} > None')    
 

    def handle_comment(self, data):
        # don't handle comments please
        pass 
if __name__ == "__main__":
    parser =  MyHtmlParser()
    Multi=[]
    x = int(input())
    while x != 0 and x <= 100:
        try:
            line = input()
        except EOFError:
            break
        if line:
            Multi.append(line)
        else:
            break
    text = '\n'.join(Multi)   
    parser.feed(text)