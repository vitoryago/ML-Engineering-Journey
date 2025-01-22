# ML Engineering Utilities

This module contains utility functions that support our ML Engineering workflow. These utilities are designed to handle common tasks in data processing, validation, and model deployment.

## Data Validation

The `data_validation.py` module provides tools for validating datasets before ML processing. This helps catch common issues early in the ML pipeline.

### Features

- DataFrame validation for required columns
- Numeric data type verification
- Empty dataset detection
- Missing value identification

### Usage Example

```python
from src.utils.data_validation import validate_dataset
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': ['a', 'b', 'c']
})

# Validate the DataFrame
result = validate_dataset(
    df=df,
    required_columns=['feature1'],
    numeric_columns=['feature1']
)

# Check validation results
if result['is_valid']:
    print("Dataset is valid!")
else:
        print("Validation errors:", result['errors'])
    ```