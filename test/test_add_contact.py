# -*- coding: utf-8 -*-
from model.group_contact import GroupContact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(GroupContact(firstname="Stas", lastname="Emelianov", title="Mr", email="emelianov.stanislav@gmail.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(GroupContact(firstname="", lastname="", title="", email=""))
    app.session.logout()
