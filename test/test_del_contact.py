# -*- coding: utf-8 -*-
from model.group_contact import GroupContact

def test_delete_first_contact(app):
    if app.contact.count(app) == 0:
        app.contact.create(GroupContact(firstname="first", lastname="last"))
    app.contact.delete_first_contact(app)