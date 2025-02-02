import requests

def get_second_to_last_url():
    base_url = "https://www.swapi.tech/api/people/"
    current_url = base_url
    second_to_last_url = None

    while current_url:
        response = requests.get(current_url)
        if response.status_code != 200:
            print(f"Error: Unable to fetch data from {current_url}")
            break
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Invalid JSON response from {current_url}")
            break

        if data.get("next"):
            second_to_last_url = current_url

        # go to the next page
        current_url = data.get("next")
    return second_to_last_url

result = get_second_to_last_url()
if result:
    print(f"The url of the second-to-last-page is: {result}")
else:
    print("There is no second-to-last page.")