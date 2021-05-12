from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first(Group("123", "123", "123"))


def test_modify_group_name(app):
    app.group.modify_first(Group(name="New name"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="New header"))
