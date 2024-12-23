import requests

city_name = input("Enter city name: ")
api_key = "970f00d5eb01a878ac847bd6168aaf82"
api_url = (
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&"
    f"appid={api_key}"
)
print(api_url)

weatehr_info = requests.get(api_url)
# print(weatehr_info)
if weatehr_info.status_code == 200:
    res = weatehr_info.json()
    main_data = res.get("main")
    print("Main Data: ", main_data)
else:
    print("Error in the API request")
