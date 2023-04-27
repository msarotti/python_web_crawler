from modules.abstracts.protocols import Crawler, Content
from modules.services.content import Html
from modules.services.crawler import WebCrawler

class CrawlerFactory:
  """Creates a crawler according to the passed type
  """
  def create(self, crawler_type: str) -> Crawler:
    if crawler_type == "web":
      return WebCrawler()
    raise ValueError("Invalid crawler type")

class ContentTypeFactory:
  """Creates a content type manager according to the passed type
  """
  def create(self, content_type: str) -> Content:
    if content_type == "html":
      return Html()
    raise ValueError("Invalid content type")
