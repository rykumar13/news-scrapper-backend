import requests


def main():
    # url = "http://127.0.0.1:5000/"
    url = "http://localhost:8080/"
    raw_response = requests.get(url=url, auth=('api_username', 'api_password'))

    if raw_response.status_code == 200:
        result = raw_response.json()
        print(result)
    else:
        print(str(raw_response.status_code) + " - " + raw_response.text)


if __name__ == "__main__":
    main()
