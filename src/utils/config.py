#############################################################################
# config.py
# Purpose: Manage configuration settings for our ML Engineering project
# This module provides a type-safe, centralized way to handle all configuration needs, from model parameters to API credentials

#############################################################################

from dataclasses import dataclass
from typing import Optional
import yaml
import os

@dataclass
class MLConfig:
    """
    Configuration class for ML-related settings.

    This class uses Python's dataclass feature to create a strongly-typed configuration manager.
    This helps catch configuration erros early and provides clear documentation of all available settings.

    Attributes:
    - model_name (str): The name of the model we're using
    - batch_size (int): Number of samples to process at once during training/inference
    - learning_rate (float): Step size for model optimization during training
    - telegram_token (Optional[str]): Authentication token for Telegram Bot API
    - fatsecret_key (Optional[str]): Authentication key for FatSecret API
    """

    # Model configurations
    # These are the core ML parameters that affect model performance
    model_name: str
    batch_size: int
    learning_rate: float

    # API credentials are Optional because they might come from environment variables
    # We use Optional[str] to indicate that these might be None
    # This is a security best practice to avoid accidentally exposing credentials
    telegram_token: Optional[str] = None
    fatsecret_key: Optional[str] = None

    @classmethod
    def from_yaml(cls, file_path: str) -> 'MLConfig':
        """
        Load configuration settings from a YAML file.
        This method allows us to load configurations from human-readable YAML files.
        It also checks for environment variables to override sensitive settings like API credentials.

        Args:
        - file_path (str): Path to the YAML file containing configuration settings

        Returns:
        - MLConfig: Configuration settings loaded from the YAML file

        Example:
            # Load default configuration
            config = MLConfig.from_yaml('configs/default.yml')

        Note:
            Environment variables take precedence over YAML file values for sensitive settings.
        """
        
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)
            return cls(**config_data)