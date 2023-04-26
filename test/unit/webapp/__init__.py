import pytest
from flask import Flask, render_template

from app import app

"""Initialize the testing environmentxw
"""
@pytest.fixture
@app.route('/page1', methods=('GET', 'POST'))
def page1():
    return render_template(
      'tests/page1.html',
      )

@pytest.fixture
@app.route('/page2', methods=('GET', 'POST'))
def page2():
    return render_template(
      'tests/page2.html',
      )

@pytest.fixture
@app.route('/page3', methods=('GET', 'POST'))
def page3():
    return render_template(
      'tests/page3.html',
      )

@pytest.fixture
@app.route('/page_no_link', methods=('GET', 'POST'))
def page_no_link():
    return render_template(
      'tests/page_no_link.html',
      )


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = "b337f7fcd5fc6e2dc3ee9751b73399535c2f6232991c394f"
    
    client = app.test_client()
    
    yield client