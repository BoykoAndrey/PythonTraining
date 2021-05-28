from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, home_phone=None, mobile_phone=None, work_phone=None,
                 secondary_phone=None, all_phones_from_home_page=None, id=None, email=None, email2=None, email3=None,
                 all_emails_from_home_page=None, address=None):
        self.first_name = first_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.last_name = last_name
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) or (
                self.first_name is None) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
