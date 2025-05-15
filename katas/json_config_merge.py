import json
import os
from typing import Any

def recursive_merge(d1: dict[str, Any], d2: dict[str, Any]) -> dict[str, Any]:
    """
    Recursively merge two dictionaries, where values in d2 override those in d1.
    Nested dictionaries are merged recursively.
    """
    result = d1.copy()
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = recursive_merge(result[key], value)
        else:
            result[key] = value
    return result

def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Example:

        File: default.json
        {
          "user": {
            "name": "John",
            "age": 30
          },
          "settings": {
            "theme": "light",
            "language": "english"
          }
        }

        File: local.json
        {
          "user": {
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        Result:
        {
          "user": {
            "name": "John",
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "theme": "light",
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """
    merged_config: dict[str, Any] = {}

    for path in json_paths:
        if not os.path.isfile(path):
            print(f"Warning: File not found, skipping: {path}")
            continue

        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            merged_config = recursive_merge(merged_config, config)

    return merged_config



if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('default.json', 'production.json', 'us-east-1-production.json')
    print(config)
