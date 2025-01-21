import pandas as pd
import pytest
from src.utils.data_validation import validate_dataset

def test_validate_dataset():
    
    # Create a DataFrame for testing
    test_df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': [10.5, 20.1, 30.2],
        'category': ['A', 'B', 'C']
    })

    # Test the function with a valid DataFrame
    result = validate_dataset(
        df=test_df,
        required_columns=['id', 'value', 'category'],
        numeric_columns=['id', 'value']
    )

    assert result['is_valid'] == True
    assert len(result['errors']) == 0

    # Test with missing columns
    result = validate_dataset(
        df=test_df,
        required_columns=['missing_column'],
        numeric_columns=['id']
    )

    assert result['is_valid'] == False
    assert any('missing_column' in error for error in result['errors'])

