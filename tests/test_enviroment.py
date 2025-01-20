# test_environment.py

# Core data science and ML packages
import numpy as np
import pandas as pd
from sklearn import datasets
import torch

# LLM and transformers tools
from transformers import pipeline
from langchain_community.llms import OpenAI  # Updated import
from langchain.chains import LLMChain

# Test that our imports work
def test_imports():
    print("Testing NumPy:", np.__version__)
    print("Testing Pandas:", pd.__version__)
    print("Testing PyTorch:", torch.__version__)
    print("Testing Transformers and LangChain: Successfully imported!")

if __name__ == "__main__":
    test_imports()