from yulia_def import mean_age_for_class
import pandas as pd

def test_mean_age_for_class_countig():
    grid = {'Pclass': [1, 2, 3, 1, 2, 3], 'Age': [10, 0, 0, 15, 0, 0]}
    test_data = pd.DataFrame(grid)
    assert mean_age_for_class(test_data, 1) == 12.5


def test_mean_age_for_class_():
    grid = {'Pclass': [1, 2, 3, None, 2, 3], 'Age': [10, 0, 0, 15, 0, 0]}
    test_data = pd.DataFrame(grid)
    assert mean_age_for_class(test_data, 1) == 10


def test_mean_age_for_class():
    grid = {'Pclass': [1, 2, 3, 1, 2, 3], 'Age': [10, 0, 0, None, 0, 0]}
    test_data = pd.DataFrame(grid)
    assert mean_age_for_class(test_data, 1) == 10
