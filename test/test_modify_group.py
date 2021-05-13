from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test", "test", "test"))
    app.group.modify_first(Group("123", "123", "123"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(name="New name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    app.group.modify_first(Group(header="New header"))
