# -*- coding: utf-8 -*-
from model.group_contact import GroupContact

def test_modify_first_contact(app):
    app.contact.modify_first_contact(GroupContact(firstname="F1", lastname="F2", title="Mrs", email="f1.f2@gmail.com"), app)