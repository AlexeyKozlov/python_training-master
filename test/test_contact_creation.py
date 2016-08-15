# -*- coding: utf-8 -*-
from model.contact_data import Contact_option


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact_option(first_name="Kamaz", middle_name="Petroviz", last_name="Testov", nick_name="petro", title="neznay",company="opensystem", address="moskva",
                         tel_home="228228", tel_mobile="8952282288", tel_work="84954443322", tel_fax="59944", email="petro@petro.ru",
                         email2="contact@petro.ru", homepage="petro.ru/home", address2="moskva", home="nesnay",
                         notes="toge nesnay")
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact_option.id_or_max) == sorted(new_contacts,key=Contact_option.id_or_max)


def test_add_new2(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact_option(first_name="Hren", middle_name="Testoviz", last_name="Petrov", nick_name="vasa", title="neznay",company="opensystem", address="moskva",
                         tel_home="228228", tel_mobile="8952282288", tel_work="84954443322", tel_fax="59944", email="petro@petro.ru",
                         email2="contact@petro.ru", homepage="petro.ru/home", address2="moskva", home="nesnay",
                         notes="toge nesnay")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact_option.id_or_max) == sorted(new_contacts,key=Contact_option.id_or_max)