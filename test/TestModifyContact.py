from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="test"))
    app.contact.modify_first(Contact("123", "123"))
