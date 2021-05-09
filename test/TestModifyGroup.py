from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group("123", "123", "123"))
    app.session.logout()
