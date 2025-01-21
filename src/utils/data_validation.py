import pandas as pd
import numpy as np
from typing import List, Tuple, Dict, Union

def validate_dataset(
        df: pd.DataFrame,
        required_columns: List[str] = None,
        numeric_columns: List[str] = None
) -> Dict[str, Union[bool, List[str]]]:
    """
    Validate a pandas Dataframe for ML processing requirements.

    Args:
    df (pd.DataFrame): The DataFrame to validate.
    required_columns (List[str]): List of columns that must be present in the DataFrame.
    numeric_columns (List[str]): List of columns that must be numeric.

    Returns:
    Dict[str, Union[bool, List[str]]]: A dictionary with the validation results.

    """
    validation_results = {
        "is_valid": True,
        "errors": []
    }

    # Check if the DataFrame is empty
    if df.empty:
        validation_results["is_valid"] = False
        validation_results["errors"].append("DataFrame is empty.")
        return validation_results

    # Check if the DataFrame has NaN values    
    if required_columns:
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            validation_results["is_valid"] = False
            validation_results["errors"].append(f"Missing columns: {missing_columns}")
    
    # Check numeric columns
    if numeric_columns:
        non_numeric_columns = [col for col in numeric_columns if not pd.api.types.is_numeric_dtype(df[col])]
        if non_numeric_columns:
            validation_results["is_valid"] = False
            validation_results["errors"].append(f"Non-numeric columns: {non_numeric_columns}")
            