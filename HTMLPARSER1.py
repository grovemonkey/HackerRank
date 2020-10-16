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
    n = int(input())
    for i in range(n):
        parser.feed(input())

