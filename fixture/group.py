class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.filing_in_the_fields(group)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def filing_in_the_fields(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def modify_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.filing_in_the_fields(group)
        wd.find_element_by_name("update").click()
        self.open_groups_page()
