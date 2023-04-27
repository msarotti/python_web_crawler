from bs4 import BeautifulSoup
from urllib.request import urlopen

class Html:
    """A Content Manager Type specific for html

    It has the get method to get html content
    from the webpage and uses BeautifulSoup return
    a parsable object
    """
    @staticmethod
    def get(place: str) -> str:
        with urlopen(place) as requests:
            return requests.read()

    @staticmethod
    def create_soup(from_content: str) -> BeautifulSoup:
        return BeautifulSoup(from_content, features="html.parser")

