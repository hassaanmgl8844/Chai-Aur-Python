import requests


def fetch_random_user_api():
    # url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        userdata = user_data["id"]
        usercontent = user_data["content"]
        return userdata,usercontent
    else:
        raise Exception("Failed to Fetch data!")


def main():
    try:
        userdata, usercontent = fetch_random_user_api()
        print(f"Id: {userdata} , Content: {usercontent}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
