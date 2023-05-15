from kate_def import process
import pandas as pd


def test_process_if_save():
    df = pd.DataFrame({'Survived': [0, 1, 1, 0, 1], 'Sex': ['male', 'male', 'male', 'female', 'female']})
    left = process(df, 1)
    right = 2, 1
    assert left[0], left[1] == right

def test_process_if_not_save():
    df = pd.DataFrame({'Survived': [0, 1, 1, 0, 1], 'Sex': ['male', 'male', 'male', 'female', 'female']})
    left = process(df, 0)
    right = 1, 1
    assert left[0], left[1] == right

def test_process_if_save_emty():
    df = pd.DataFrame({'Survived': [0, None, 1, 0, 1], 'Sex': ['male', 'male', 'male', 'female', 'female']})
    left = process(df, 1)
    right = 1, 1
    assert left[0], left[1] == right