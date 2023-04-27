from test.unit.webapp import client
from unittest import mock
from modules.factories import CrawlerFactory, ContentTypeFactory

def test_crawl(client, mocker):
    mocker.patch(
        "modules.services.crawler.WebCrawler.is_valid_url", return_value=True)
    mocker.patch("modules.services.content.Html.get", side_effect=[
    client.get("/page1").data.decode(),
    client.get("/page2").data.decode(),
    client.get("/page3").data.decode()])
    crawler = CrawlerFactory().create("web")
    content_type = ContentTypeFactory().create("html")
    link_list = crawler.crawl("/page1", content_type)
    assert {'/page1':['/page1','/page2'], '/page2':['/page2','/page3'], '/page3':[]} == link_list

def test_crawl_only_external_link(client, mocker):
    mocker.patch(
        "modules.services.crawler.WebCrawler.is_valid_url", return_value=True)
    mocker.patch("modules.services.content.Html.get", side_effect=[
    client.get("/page3").data.decode()])
    crawler = CrawlerFactory().create("web")
    content_type = ContentTypeFactory().create("html")
    link_list = crawler.crawl("/page3", content_type)
    assert {'/page3': []} == link_list

def test_crawl_no_link_page(client, mocker):
    mocker.patch(
        "modules.services.crawler.WebCrawler.is_valid_url", return_value=True)
    mocker.patch("modules.services.content.Html.get", side_effect=[
    client.get("/page_no_link").data.decode()])
    crawler = CrawlerFactory().create("web")
    content_type = ContentTypeFactory().create("html")
    link_list = crawler.crawl("/page_no_link", content_type)
    assert {'/page_no_link': [] } == link_list
