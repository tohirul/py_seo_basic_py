import requests  # Import for formatting JSON output


def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()


def get_ip_details():
    ip = get_ip()['ip']
    print(f"IP: {ip}")
    response = requests.get(f'http://ip-api.com/json/{ip}')

    return response.json()


# person_name = input("Enter your name: ")
# print(person_name)
print(["Jhon Doe", "Jane Doe", "John Smith", "Jane Smith"])

if __name__ == '__main__':
    # Get public IP and print as prettified JSON
    res = get_ip()
    print("Public IP:")
    print(res)
    # Get IP details and print as prettified JSON
    ip_details = get_ip_details()
    print("\nIP Details:")
    print(ip_details)
