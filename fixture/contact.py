class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav']//a[text()='add new']").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("submit").click()
