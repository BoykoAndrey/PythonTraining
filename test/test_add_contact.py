from model.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact(first_name="dfbdfb", middle_name="dfbdfb"))
