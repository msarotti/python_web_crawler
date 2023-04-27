import os
from flask import Flask, render_template
from modules.forms import UrlForm
from modules.factories import CrawlerFactory, ContentTypeFactory


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=('GET', 'POST'))
def index():
    url = None
    link_list = []
    errors = []
    form = UrlForm()
    if form.validate_on_submit():
      try:
        url = form.url.data
        crawler = CrawlerFactory().create("web")
        content_type = ContentTypeFactory().create("html")
        link_list = crawler.crawl(url, content_type)
        form.url.data = ''
      except Exception as e:
        print(f"Error: {e}")

    else:
      errors = form.url.errors
    return render_template(
      'index.html',
      url=url,
      errors=errors,
      link_list=link_list,
      form=form
      )
