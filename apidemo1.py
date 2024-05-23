import requests
import time

# Zoho Books API endpoint
API_ENDPOINT = "https://books.zoho.com/api/v3/invoices"

# Your Zoho Books API credentials
CLIENT_ID = ""
CLIENT_SECRET = ""
REFRESH_TOKEN = ""

def get_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        return response.json()["access_token"]
    except Exception as e:
        print("Failed to get access token:", e)
        return None

def fetch_invoices(access_token):
    headers = {
        "Authorization": "Zoho-oauthtoken " + access_token
    }
    try:
        response = requests.get(API_ENDPOINT, headers=headers)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        return response.json()["invoices"]
    except Exception as e:
        print("Failed to fetch invoices:", e)
        return None

def main():
    while True:
        access_token = r""
        if access_token:
            invoices = fetch_invoices(access_token)
            if invoices:
                print("Fetched invoices:", invoices)
                # Process the fetched invoices here
                time.sleep(60)  # Sleep for 60 seconds before making the next request
            else:
                print("Failed to fetch invoices. Retrying in 5 seconds...")
                time.sleep(5)
        else:
            print("Failed to get access token. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    main()
