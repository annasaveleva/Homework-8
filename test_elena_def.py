from elena_def import count_people


def test_count_people_counting():
    data = [' ,1, , , , ,8',
            ' ,1, , , , ,1',
            ' ,0, , , , ,5',
            ' ,0, , , , ,10',
            ' ,0, , , , ,3',
            ' ,1, , , , ,85',
            ' ,0, , , , ,50',
            ' ,1, , , , ,40']
    assert count_people(data) == (8, 2, 1, 3, 0)


def test_count_people_if_age_empty():
    data = [' ,1, , , , ,8',
            ' ,1, , , , ,',
            ' ,0, , , , ,5',
            ' ,0, , , , ,10',
            ' ,0, , , , ,3',
            ' ,1, , , , ,85',
            ' ,0, , , , ,50',
            ' ,1, , , , ,40']
    assert count_people(data) == (8, 1, 1, 3, 0)


def test_count_people_if_survived_empty():
    data = [' , , , , , ,8',
            ' ,1, , , , ,1',
            ' ,0, , , , ,5',
            ' ,0, , , , ,10',
            ' ,0, , , , ,3',
            ' ,1, , , , ,85',
            ' ,0, , , , ,50',
            ' ,1, , , , ,40']
    assert count_people(data) == (8, 1, 1, 3, 0)
