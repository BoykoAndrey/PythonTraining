import pytest

from fixture.Application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(first_name="dfbdfb", middle_name="dfbdfb"))
    app.session.logout()
