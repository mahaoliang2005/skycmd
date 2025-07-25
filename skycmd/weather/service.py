"""
Weather service module

This module provides functionality to fetch weather information from wttr.in.
"""

import requests


def get_weather_from_wttr(city_name):
    """
    Get weather information from wttr.in
    
    Args:
        city_name (str): Name of the city
    
    Returns:
        str: Weather information text
    """
    try:
        # Use wttr.in API to get weather information
        url = f"https://wttr.in/{city_name}?m&format=3"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return f"Error getting weather information: {e}"


def get_detailed_weather_from_wttr(city_name):
    """
    Get detailed weather information from wttr.in
    
    Args:
        city_name (str): Name of the city
    
    Returns:
        str: Detailed weather information text
    """
    try:
        # Use wttr.in API to get detailed weather information
        url = f"https://wttr.in/{city_name}?m"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error getting detailed weather information: {e}"
    
if __name__ == "__main__":
    get_weather_from_wttr("Shenzhen")