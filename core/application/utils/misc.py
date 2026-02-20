from typing import Generator
from transformers import AutoTokenizer
from core.settings import settings


def flatten(nested_list: list) -> list:
    return [item for sublist in nested_list for item in sublist]
