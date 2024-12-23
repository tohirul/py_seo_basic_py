import requests

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
api_key = 'AIzaSyDo5ie5mIioI4ayomiC6tHZFRVJLv4DaWM'
url_to_analyze = input("Enter the URL to analyze: ")

# check if the URL is valid using while loop
while not (url_to_analyze.startswith("http://") or
           url_to_analyze.startswith("https://")):
    print("Invalid URL!!!")
    url_to_analyze = input("Enter the URL to analyze: ")


def create_url(url: str, api_key: str, url_to_analyze: str) -> str:
    return f"{url}?url={url_to_analyze}&key={api_key}"


insight_result = requests.get(create_url(url, api_key, url_to_analyze))

if insight_result.status_code == 200:
    print("PageSpeed Insights API request successful.")
    site_id = insight_result.json().get("id")
    loading_experience = insight_result.json().get("loadingExperience")

    site_categories = insight_result.json().get(
        "lighthouseResult").get("categories")
    site_environments = insight_result.json().get(
        "lighthouseResult").get("environments")
    site_audits = insight_result.json().get("lighthouseResult").get("audits")

    site_interactive = site_audits.get("interactive")
    print(f"Site interactive: {site_interactive}")

    site_legacy_javascript = site_audits.get("legacy-javascript")
    print(f"Site legacy javascript: {site_legacy_javascript}")
