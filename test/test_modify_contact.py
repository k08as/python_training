# -*- coding: utf-8 -*-
from model.group_contact import GroupContact

def test_modify_first_contact(app):
    if app.contact.count(app) == 0:
        app.contact.create(GroupContact(firstname="first", lastname="last"))
    app.contact.modify_first_contact(GroupContact(firstname="F1", lastname="F2", title="Mrs", email="f1.f2@gmail.com"), app)