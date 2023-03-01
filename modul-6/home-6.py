def group_them(**kwargs):
    pass

def test_group_them():
    assert group_them() == ''
    assert group_them(python='super') == 'Python is super'
    assert group_them(python='super', java='almost super') == 'Python is super\nJava is almost super'
