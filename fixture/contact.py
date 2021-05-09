class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav']//a[text()='add new']").click()
        self.filing_in_the_fields(contact)
        wd.find_element_by_name("submit").click()

    def filing_in_the_fields(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.filing_in_the_fields(contact)
        wd.find_element_by_name("update").click()
