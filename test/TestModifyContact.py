from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first(Contact("123", "123"))
