__author__ = 'Evgeny'
import re
from model.contact_data import Contact_option

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def enter_contact_create(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create(self, contact_option):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact_option)
        self.enter_contact_create()
        self.home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact_option):
        wd = self.app.wd
        self.change_field_value("firstname", contact_option.first_name)
        self.change_field_value("middlename", contact_option.middle_name)
        self.change_field_value("lastname", contact_option.last_name)
        self.change_field_value("nickname", contact_option.nick_name)
        self.change_field_value("title", contact_option.title)
        self.change_field_value("company", contact_option.company)
        self.change_field_value("address", contact_option.address)
        self.change_field_value("home", contact_option.tel_home)
        self.change_field_value("mobile", contact_option.tel_mobile)
        self.change_field_value("work", contact_option.tel_work)
        self.change_field_value("fax", contact_option.tel_fax)
        self.change_field_value("email2", contact_option.email)
        self.change_field_value("email3", contact_option.email2)
        self.change_field_value("homepage", contact_option.homepage)
        self.change_field_value("address2", contact_option.address2)
        self.change_field_value("phone2", contact_option.home)
        self.change_field_value("notes", contact_option.notes)

    def change_field_value(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//input[@name='selected[]']")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def update_first_contact(self):
        self.delete_contact_by_index(0)


    def update_contact_by_index(self, index, new_contact_option):
        wd = self.app.wd
        #open modification form for first contact
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//img[@title='Edit']")[index].click()
        #fill contact form
        self.fill_contact_form(new_contact_option)
        #submit modification
        wd.find_element_by_name("update").click()
        self.home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('img[alt="Edit"]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact_option(first_name=firstname,last_name=lastname,id=id))
        return list(self.contact_cache)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("home").click()

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact_option(first_name=firstname,last_name=lastname,id=id,
                              tel_home=homephone,tel_work=workphone,
                              tel_mobile=mobilephone,home=secondaryphone)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_home = re.search("H: (.*)",text).group(1)
        tel_work = re.search("W: (.*)",text).group(1)
        tel_mobile = re.search("M: (.*)",text).group(1)
        home = re.search("P: (.*)",text).group(1)
        return Contact_option(tel_home=tel_home,tel_work=tel_work,
                              tel_mobile=tel_mobile,home=home)