from html_to_json import convert_html
from bs4 import BeautifulSoup


def preprocess_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    try:
        soup.a.div.string = '!!qoute!!'
        soup.select('a[title="view author"]')[0].string = '!!author!!'
        return soup.prettify()
    except:
        return ''
