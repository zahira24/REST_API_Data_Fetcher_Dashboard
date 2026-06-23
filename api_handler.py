# api_handler.py
# This file handles all API requests and error handling

import requests

def fetch_data(url, timeout=10):
    """
    Fetch data from a public API with error handling
    """

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # raises error for bad status codes

        # Try to convert response to JSON
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("⏰ Error: Request timed out!")
        return None

    except requests.exceptions.ConnectionError:
        print("🌐 Error: Connection failed!")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}")
        return None

    except ValueError:
        print("❌ Error: Response is not valid JSON!")
        return None

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None