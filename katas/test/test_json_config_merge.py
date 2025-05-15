import json
import os
import unittest
from tempfile import NamedTemporaryFile
from typing import Any

from katas.json_config_merge import json_configs_merge

class TestJsonConfigMerge(unittest.TestCase):
    def create_temp_json(self, data: dict[str, Any]) -> str:
        """Helper to create a temporary JSON file and return its path."""
        temp_file = NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        json.dump(data, temp_file)
        temp_file.close()
        self.temp_files.append(temp_file.name)
        return temp_file.name

    def setUp(self):
        self.temp_files = []

    def tearDown(self):
        for file in self.temp_files:
            os.remove(file)

    def test_merge_two_simple_configs(self):
        file1 = self.create_temp_json({
            "user": {
                "name": "John",
                "age": 30
            },
            "settings": {
                "theme": "light",
                "language": "english"
            }
        })

        file2 = self.create_temp_json({
            "user": {
                "age": 31,
                "email": "john@example.com"
            },
            "settings": {
                "language": "spanish",
                "timezone": "UTC+1"
            }
        })

        expected = {
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

        result = json_configs_merge(file1, file2)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        result = json_configs_merge()
        self.assertEqual(result, {})