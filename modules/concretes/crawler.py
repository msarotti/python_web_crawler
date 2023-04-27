import validators
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from modules.abstracts.protocols import Crawler, Content

class WebCrawler:
  """A web crawler

  It manages web scraping returning all the links found in 
  a website, crawling only the domain and subdomain links
  """
  def __init__(self):
    self.urls_to_visit = []

  def crawl(self, start_url: str, content_type: Content) -> dict:
    link_list = {}
    self.urls_to_visit.append(start_url)
    while self.urls_to_visit:
      url = self.urls_to_visit.pop()
      if self.is_valid_url(url) and url not in link_list.keys():
        soup, domain = self.data_from_content(url, content_type)
        url_links = self.get_link_list(soup, domain)
        link_list[url] = url_links
        
    return link_list


  def get_link_list(
      self,
      soup: BeautifulSoup,
      domain: str
    ) -> list:
    url_links = []
    for link in soup.find_all('a'):
        link_domain = self.get_domain(link.get('href'))
        if self.is_in_domain(link_domain, domain) and not self.is_in_list(link.get('href'), self.urls_to_visit):
          self.urls_to_visit.append(link.get('href'))
          url_links.append(link.get('href'))
    return url_links


  def is_in_domain(self, link: str, domain: str) -> bool:
    if link is not None and link == domain:
      return True
    return False


  def is_in_list(self, link_domain: str, link_list: list):
    if link_domain in link_list:
      return True
    return False


  def is_valid_url(self, url: str) -> bool:
    return validators.url(url)


  def get_domain(self, url: str) -> str:
      t = urlparse(url).netloc
      return '.'.join(t.split('.')[-2:])


  def data_from_content(self, url: str, content_type: Content):
    html = content_type.get(url)
    soup = content_type.create_soup(html)
    domain = self.get_domain(url)
    return soup, domain