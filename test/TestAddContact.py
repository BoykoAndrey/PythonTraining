from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(first_name="dfbdfb", middle_name="dfbdfb"))
    app.session.logout()
