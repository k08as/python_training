# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group_contact import GroupContact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(GroupContact(firstname="Stas", lastname="Emelianov", title="Mr", email="emelianov.stanislav@gmail.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(GroupContact(firstname="", lastname="", title="", email=""))
    app.session.logout()
