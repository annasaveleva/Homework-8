from margarita_def import do_dataframe
import pandas as pd


def test_do_dataframe_if_save():
    grid = {'ID': [1, 2, 3], 'Survived': [0, 0, 1], 'Fare': [0.0, 1, 0.0]}
    test_data = pd.DataFrame(grid)
    left = do_dataframe(test_data, True)
    right = pd.DataFrame({'ID': [3], 'Survived': [1], 'Fare': [0.0]})
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True))

def test_do_dataframe_if_not_save():
    grid = {'ID': [1, 2, 3], 'Survived': [0, 0, 1], 'Fare': [0.0, 1, 0.0]}
    test_data = pd.DataFrame(grid)
    left = do_dataframe(test_data, False)
    right = pd.DataFrame({'ID': [1], 'Survived': [0], 'Fare': [0.0]})
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True))

def test_do_dataframe_for_no_items():
    grid = {'ID': [1, 2, 3], 'Survived': [0, 0, 1], 'Fare': [2, 1, 3]}
    test_data = pd.DataFrame(grid)
    assert do_dataframe(test_data, False) == "There is no items"

def test_do_dataframe_for_no_Fare():
    grid = {'ID': [1, 2, 3], 'Survived': [0, 0, 1], 'Fare': [None, None, None]}
    test_data = pd.DataFrame(grid)
    assert do_dataframe(test_data, False) == "There is no items"

def test_do_dataframe_for_no_Survived():
    grid = {'ID': [1, 2, 3], 'Survived': [None, None, None], 'Fare': [0.0, 1, 0.0]}
    test_data = pd.DataFrame(grid)
    assert do_dataframe(test_data, False) == "There is no items"