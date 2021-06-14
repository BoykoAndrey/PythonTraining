import random

from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.add(Contact(first_name="test"))
    old_contacts = db.get_contacts_list()
    old_contact = random.choice(old_contacts)
    contact = Contact("123", "123")
    app.contact.modify_contact_by_id(contact, old_contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contacts_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
