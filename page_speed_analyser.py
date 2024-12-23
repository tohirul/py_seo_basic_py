import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def analyze_page_speed(url):
    # Set up Chrome with performance logging
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}  # type: ignore

    # Initialize ChromeDriver with the desired capabilities
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for efficiency
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # Start timing and load the page
    print(f"Analyzing page speed for {url}...")
    start_time = time.time()
    driver.get(url)
    load_time = time.time() - start_time

    # Get Navigation Timing performance metrics
    nav_timing_script = """
        return window.performance.timing;
    """
    nav_timing = driver.execute_script(nav_timing_script)

    # Calculate key metrics
    dom_content_loaded = (
        nav_timing["domContentLoadedEventEnd"] -
        nav_timing["navigationStart"]
    ) / 1000
    load_event = (nav_timing["loadEventEnd"] -
                  nav_timing["navigationStart"]) / 1000

    # Print results
    print(f"Page Load Time: {load_time:.2f} seconds")
    print(f"DOM Content Loaded: {dom_content_loaded:.2f} seconds")
    print(f"Full Page Load Event: {load_event:.2f} seconds")

    # Close browser
    driver.quit()

    # Return results as a dictionary
    return {
        "url": url,
        "page_load_time": round(load_time, 2),
        "dom_content_loaded": round(dom_content_loaded, 2),
        "full_page_load": round(load_event, 2)
    }


# Main function
if __name__ == "__main__":
    url = input("Enter the URL to analyze: ")
    results = analyze_page_speed(url)
    print("\nAnalysis Complete!")
