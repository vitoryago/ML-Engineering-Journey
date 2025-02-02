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