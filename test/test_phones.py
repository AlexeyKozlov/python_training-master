import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.tel_home == clear(contact_from_edit_page.tel_home)
    assert contact_from_home_page.tel_work == clear(contact_from_edit_page.tel_work)
    assert contact_from_home_page.tel_mobile == clear(contact_from_edit_page.tel_mobile)
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.tel_home == contact_from_edit_page.tel_home
    assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work
    assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile
    assert contact_from_view_page.home == contact_from_edit_page.home

def clear(s):
    return re.sub("[() -]","",s)
