import unittest
import requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ipAddress": "8.8.8.8",
            "countryName": "United States",
            "cityName": "Mountain View",
            "regionName": "California",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States")
        self.assertEqual(result.get("city"), "Mountain View")
        self.assertEqual(result.get("region"), "California")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

        
    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                 "ipAddress": "8.8.8.8",
                 "countryName": "United States",
                 "cityName": "Mountain View",
                 "regionName": "California",
                },
            ),
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ipAddress": "8.8.8.8",
            "countryName": "United States",
            "cityName": "Mountain View",
            "regionName": "California",
        }
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States")
        self.assertEqual(result.get("city"), "Mountain View")
        self.assertEqual(result.get("region"), "California")

