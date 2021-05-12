class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav']//a[text()='add new']").click()
        self.filing_in_the_fields(contact)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//*[@id='nav']//a[text()='home']").click()

    def filing_in_the_fields(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.filing_in_the_fields(contact)
        wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
