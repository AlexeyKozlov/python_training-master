
from sys import maxsize


class Contact_option:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, title=None, company=None, address=None, tel_home=None,
                        tel_mobile=None, tel_work=None, tel_fax=None, email=None, email2=None, homepage=None, address2=None, home=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.tel_home = tel_home
        self.tel_mobile = tel_mobile
        self.tel_work = tel_work
        self.tel_fax = tel_fax
        self.email = email
        self.email2 = email2
        self.homepage = homepage
        self.address2 = address2
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
