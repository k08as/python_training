# -*- coding: utf-8 -*-
from model.group_contact import GroupContact


def test_add_contact(app):
    app.contact.create(GroupContact(firstname="Stas", lastname="Emelianov", title="Mr", email="emelianov.stanislav@gmail.com"))


def test_add_empty_contact(app):
    app.contact.create(GroupContact(firstname="", lastname="", title="", email=""))
