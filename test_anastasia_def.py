from anastasia_def import count_middle_price

def test_count_middle_price():
    data = [' ,Survived, , , , ,Fare',
            ' ,1, , , , ,1',
            ' ,0, , , , ,10',
            ' ,0, , , , ,20',
            ' ,0, , , , ,30',
            ' ,1, , , , ,2',
            ' ,1, , , , ,3']
    assert count_middle_price(data) == (2, 20)


def test_count_middle_price_if_survived_is_empty():
    data = [' ,Survived, , , , ,Fare',
            ' ,1, , , , ,1',
            ' ,0, , , , ,10',
            ' ,0, , , , ,20',
            ' ,0, , , , ,30',
            ' ,None, , , , ,2',
            ' ,1, , , , ,3']
    assert count_middle_price(data) == (2, 20)


def test_count_middle_price_if_fare_is_empty():
    data = [' ,Survived, , , , ,Fare',
            ' ,1, , , , ,1',
            ' ,0, , , , ,10',
            ' ,0, , , , ,20',
            ' ,0, , , , ,30',
            ' ,1, , , , ,None',
            ' ,1, , , , ,3']
    assert count_middle_price(data) == (2, 20)