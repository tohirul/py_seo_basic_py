import requests

# Replace this with your Abstract API key.
API_KEY = "c314faf9-4813-4265-9835-782b3af50ff2"
mail_checkker_url = "https://api.mails.so/v1/validate"

email = input("Enter email: ")

# while loop to check email address input
while (email.strip() == "" or
       "@" not in email or
       "." not in email):
    print("Please enter a valid email address")
    email = input("Enter email: ")


def check_mail(mail_checkker_url: str, api_key: str, email: str) -> bool:
    headers: dict = {
        'x-mails-api-key': api_key
    }
    response = requests.get(
        f"{mail_checkker_url}?email={email}", headers=headers)
    data = response.json()
    # print(data)

    if not data.get("error"):
        print(data)
        validity = data.get("is_disposable", {}).get("value", False)
        print(validity)
        return not validity
    else:
        print(f"Error: {data.get('error')}")
        return False


is_valid = check_mail(mail_checkker_url, API_KEY, email)

print("Is the mail valid:\n", "Yes" if is_valid else "No")
