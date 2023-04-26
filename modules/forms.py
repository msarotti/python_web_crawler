from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class UrlForm(FlaskForm):
  """Creates a simple form with a field to
  send a url to crawl. 
  It has two validator, DataRequired() which tells the
  user that the url is mandatory and URL() which checks 
  that the field is populated with a correct url.
  """
  url = StringField("Url to crawl", validators=[DataRequired(), URL()])
  submit = SubmitField("Submit")
