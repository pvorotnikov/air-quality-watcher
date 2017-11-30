import requests
import time
from bs4 import BeautifulSoup
from logger import logging



def load_content():
    r = requests.get('http://93.123.36.139/')
    if 200 == r.status_code:
        return r.text
    else:
        raise Exception('Error fetching content: {}'.format(r.status_code))

def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')

def publish(data):
    logging.info(data)
    pass


def run():
    try:
        content = load_content()
        data = parse_content(content)
        publish(data)
    except Exception as e:
        logging.error(str(e))


def main():
    while True:
        run()
        time.sleep(30 * 60) # sleep for 30min


if __name__ == "__main__":
    main()
