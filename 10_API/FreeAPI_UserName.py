import requests


def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        author = user_data["author"]
        authorcontent = user_data["content"]
        return author,authorcontent
    else:
        raise Exception("Failed to Fetch data!")


def main():
    try:
        author, authorcontent = fetch_random_user_api()
        print(
            f"Author: {author} , Content: {authorcontent}"
        )
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
