from bs4 import BeautifulSoup
from typing import Protocol


class Content(Protocol):
    """A Content Manager Abstraction
    """
    @staticmethod
    def get(place: str) -> str:
        """Get content to crawl """
        ...

    @staticmethod
    def create_soup(from_content) -> BeautifulSoup:
        """ Create a parsable object with the retreived """
        ...

class Crawler(Protocol):
    """A Crawler Abstraction
    """
    def crawl(self, start_url: str, content: Content) -> set:
        """Manage thw crawling logic
        """
        ...