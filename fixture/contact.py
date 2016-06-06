class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, group_contact):
        wd = self.app.wd
        self.change_field_value("firstname", group_contact.firstname)
        self.change_field_value("lastname", group_contact.lastname)
        self.change_field_value("title", group_contact.title)
        self.change_field_value("email", group_contact.email)

    def create(self, group_contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # fill contact form
        self.fill_contact_form(group_contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify_first_contact(self, group_contact, app):
        wd = self.app.wd
        app.open_home_page()
        self.select_first_contact()
        # init contact update
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(group_contact)
        # submit update
        wd.find_element_by_name("update").click()

    def delete_first_contact(self, app):
        wd = self.app.wd
        app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def count(self, app):
        wd = self.app.wd
        app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))