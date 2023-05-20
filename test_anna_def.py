from anna_def import count_men_women_of_selected_class
import pandas as pd


def test_count_men_women_of_selected_class():
    grid = {'Pclass': [1, 2, 3, 1, 2, 3, 1], 'Sex': ['female', 'male', 'female', 'male', 'male','male','male']}
    test_data = pd.DataFrame(grid)
    assert count_men_women_of_selected_class(test_data, 1) == (2, 1)


def test_count_men_women_of_selected_class_if_sex_is_empty():
    grid = {'Pclass': [1, 2, 1, 1, 2, 3, 1], 'Sex': ['female', 'male', None, 'male', 'male','male','male']}
    test_data = pd.DataFrame(grid)
    assert count_men_women_of_selected_class(test_data, 1) == (2, 1)


def test_count_men_women_of_selected_class_if_Pclass_is_empty():
    grid = {'Pclass': [1, 2, None, 1, 2, 3, 1], 'Sex': ['female', 'male', 'female', 'male', 'male','male','male']}
    test_data = pd.DataFrame(grid)
    assert count_men_women_of_selected_class(test_data, 1) == (2, 1)

