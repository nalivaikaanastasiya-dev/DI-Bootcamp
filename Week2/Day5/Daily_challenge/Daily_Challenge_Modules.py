import requests
import time
import sys
from typing import Optional, List

def measure_load_time(url: str) -> Optional[float]:
    """
    Measures the time it takes for a complete response from the given URL.
    
    :param url: The URL of the webpage to test (e.g., "https://www.google.com").
    :return: The elapsed time in seconds as a float, or None if the request failed.
    """
    try:
        # Start timing
        start_time = time.time()
        
        # Perform the GET request. 
        # We set a timeout (e.g., 10 seconds) to prevent the program from hanging indefinitely.
        response = requests.get(url, timeout=10)
        
        # Stop timing
        end_time = time.time()
        
        # Check if the response status code indicates success (2xx range)
        if response.status_code >= 200 and response.status_code < 300:
            load_time = end_time - start_time
            print(f"✅ Success (Status: {response.status_code})")
            return load_time
        else:
            print(f"⚠️ Failed to load (Status: {response.status_code})")
            return None

    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out after 10 seconds.")
        return None
    except requests.exceptions.RequestException as e:
        # Catches connection errors, DNS errors, etc.
        print(f"❌ Error during request: {e}")
        return None

if __name__ == "__main__":
    
    # List of websites to test
    test_sites: List[str] = [
        "https://www.google.com",
        "https://www.ynet.co.il", # Example site from prompt
        "https://www.imdb.com",   # Example site from prompt
        "https://www.amazon.com",
        "https://www.invalid-url-12345.com" # Example of a failed request
    ]

    print("--- Webpage Load Time Measurement ---")
    
    results = {}
    
    for url in test_sites:
        print(f"\nTesting URL: {url}")
        
        # Perform the measurement
        duration = measure_load_time(url)
        
        if duration is not None:
            results[url] = duration
            print(f"Load time: {duration:.4f} seconds")
        else:
            results[url] = "Failed"
            
    print("\n" + "=" * 50)
    print(f"{'TEST SUMMARY':^50}")
    print("=" * 50)
    
    for url, time_or_status in results.items():
        if isinstance(time_or_status, float):
            print(f"{url:<35}: {time_or_status:.4f} seconds")
        else:
            print(f"{url:<35}: {time_or_status}")
            
    print("=" * 50)