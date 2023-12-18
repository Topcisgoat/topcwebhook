import requests

while True:
    webhook_url = input("webhook")

    if webhook_url.lower() == 'e':
        break

    response = requests.delete(webhook_url)

    if response.status_code == 204:
        print("done")
    else:
        print("fail")