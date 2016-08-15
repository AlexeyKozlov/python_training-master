
from model.contact_data import Contact_option
from random import randrange

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact_option(first_name="Test",middle_name="Semenov"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact_option(first_name="444", middle_name="555", last_name="666", nick_name="petro", title="neznay",company="opensystem", address="moskva",
                         tel_home="228228", tel_mobile="8952282288", tel_work="84954443322", tel_fax="59944", email="petro@petro.ru",
                         email2="contact@petro.ru", homepage="petro.ru/home", address2="moskva", home="nesnay",
                         notes="toge nesnay")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact_option.id_or_max) == sorted(new_contacts,key=Contact_option.id_or_max)

