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

    checks_performed = []

    # Check if the DataFrame is empty
    if df.empty:
        validation_results["is_valid"] = False
        validation_results["errors"].append("DataFrame is empty.")
        return validation_results
    else: 
        checks_performed.append("checked if DataFrame is empty")

    # Check reqired columns   
    if required_columns:
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            validation_results["is_valid"] = False
            validation_results["errors"].append(f"Missing columns: {missing_columns}")
        checks_performed.append(f"checked {len(required_columns)} required column(s)")
    
    # Check numeric columns
    if numeric_columns:
        non_numeric_columns = [col for col in numeric_columns if not pd.api.types.is_numeric_dtype(df[col])]
        if non_numeric_columns:
            validation_results["is_valid"] = False
            validation_results["errors"].append(f"Non-numeric columns: {non_numeric_columns}")
        checks_performed.append(f"checked {len(required_columns)} required column(s)")

    # Check for NaN values
    nan_columns = df.columns[df.isna().any()].tolist()
    if nan_columns:
        validation_results["is_valid"] = False
        validation_results["errors"].append(f"Columns with NaN values: {nan_columns}")
    checks_performed.append(f"checked {len(numeric_columns)} numeric column(s)")
    
    validation_results["validation_summary"] = f"Validation performed: {', '.join(checks_performed)}"

    return validation_results
