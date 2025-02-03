# src/data/blood_test_processor.py

import pandas as pd
from pathlib import Path
from typing import Optional, Dict, List
from src.utils.logger import setup_logger
from src.utils.config import MLConfig

# Set up logging for this module
logger = setup_logger(__name__, Path("logs/blood_test_processor.log"))

class BloodTestProcessor:
    """
    Process and analyzes blood test results, preparing them for ML model interpretation.

    This class serves as the foundation for our blood test analysis system. It will:
    1. Load and validate blood test data
    2. Normalize values based on standard ranges
    3. Prepare data for our BERT model to understand and analyze

    Attributes:
        config (MLConfig): Configuration settings for data processing
        reference_ranges (Dict): Standard reference ranges for blood test values
    """

    def __init__(self, config: MLConfig):
        """
        Initialize the Blood Test Processor with configuration settings.

        Args:
            config (MLConfig): Configuration object containing processing parameters
        """

        self.config = config
        logger.info("Initilizing BloodTestProcessor")

        # Define standard ranges for common blood test metrics
        # These will be used to normalize values and detect abnormalities

        self.reference_ranges = {
            "glucose": {
                "min": 70,
                "max": 100,
                "unit": "mg/dL",
                "description": "Fasting blood glucose"
            },
            "cholesterol": {
                "min": 0,
                "max": 200,
                "unit": "mg/dL",
                "description": "Total cholesterol"
            }
            # We'll add more metrics as we expand the system
        }

    def normalize_value(self, metric: str, value: float) -> Dict:
        """
        Normalize a blood test value and determine if it's within normal range.

        This method helps standardize blood test results for our ML model by:
        1. Comparing values against standard reference ranges
        2. Calculating how far from normal a value is
        3. Preparing a structured analysis of the result

        Args:
            metric (str): The blood test metric being analyzed
            value (float): The test result value to normalize

        Returns:
            Dict: Analysis of the blood test value including:
            - normalized_value: Value scaled to standard range
            - is_normal: Boolean indicating if within normal range
            - description: Human-readable interpretation of the result
        """

        try:
            range_info = self.reference_ranges[metric]

            # Calculate where this value falls in the normal range
            range_width = range_info["max"] - range_info["min"]
            normalized_value = (value - range_info["min"]) / range_width

            # Determine if the value is within normal range
            is_normal = range_info["min"] <= value <= range_info["max"]

            # Prepare a human-readable description of the result
            if is_normal:
                description = f"{metric} is normal"
            else:
                if value < range_info["min"]:
                    description = f"{metric} is below normal"
                else:
                    description = f"{metric} is above normal"
            
            logger.info(f"Processed {metric} value: {value} {range_info['unit']}")

            return {
                "metric": metric,
                "value": value,
                "unit": range_info["unit"],
                "normalized_value": normalized_value,
                "is_normal": is_normal,
                "description": description
            }
        
        except KeyError:
            logger.error(f"Unkown blood test metric: {metric}")
            raise ValueError(f"Unknown blood test metric: {metric}")
        except Exception as e:
            logger.error(f"Error processing {metric}: {str(e)}")
            raise