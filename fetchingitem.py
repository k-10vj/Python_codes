import requests
import csv

# Authentication
auth_token = ''
headers = {
    'Authorization': 'Bearer ' + auth_token,
    'Content-Type': 'application/json'
}

# Example API request to get list of items
response = requests.get('https://books.zoho.com/api/v3/items', headers=headers)

if response.status_code == 200:
    data = response.json()
    # Extract relevant information from the data
    items = data['items']

    # Extract fields you want to include in the CSV
    # Example: 'Item ID', 'Item Name', 'Rate', etc.
    rows = []
    for item in items:
        # Use get method to handle missing keys gracefully
        rate = item.get('rate', 'N/A')
        row = (item['item_id'], item['name'], rate)  # Adjust fields as needed
        rows.append(row)

    # Write data to CSV file
    # Write data to CSV file
    csv_filename = 'items.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header
        csv_writer.writerow(['Item ID', 'Item Name', 'Rate'])  # Adjust headers as needed

        # Write the rows
        for row in rows:
            csv_writer.writerow([str(cell).encode('utf-8').decode('utf-8') for cell in row])

    print(response.text)
