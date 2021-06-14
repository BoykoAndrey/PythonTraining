import random

from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("test", "test", "test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = Group("123", "123", "123")
    app.group.modify_group_by_id(group, old_group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = Group(name="New name")
    app.group.modify_group_by_id(group, old_group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = Group(header="New header")
    app.group.modify_group_by_id(group, old_group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
