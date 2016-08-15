

from model.group_data import Group
from random import randrange


def test_group_update_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New name")
    group.id = old_groups[index].id
    app.group.update_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)

#def test_group_update_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.update_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
