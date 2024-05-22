import requests
import csv

# Authentication
auth_token = ''
headers = {
    'Authorization': 'Bearer ' + auth_token,
    'Content-Type': 'application/json'
}

# Example API request to get list of invoices
response = requests.get('https://books.zoho.com/api/v3/invoices', headers=headers)

if response.status_code == 200:
    data = response.json()
    # Extract relevant information from the data
    invoices = data['invoices']

    # Extract fields you want to include in the CSV
    # Example: 'Invoice Number', 'Customer Name', 'Amount', etc.
    rows = []
    for invoice in invoices:
        # Use get method to handle missing keys gracefully
        amount = invoice.get('amount', 'N/A')
        row = (invoice['invoice_number'], invoice['customer_name'], amount)  # Adjust fields as needed
        rows.append(row)

    # Write data to CSV file
    csv_filename = 'invoices.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header
        csv_writer.writerow(['Invoice Number', 'Customer Name', 'Amount'])  # Adjust headers as needed

        # Write the rows
        csv_writer.writerows(rows)

    print(f"CSV file '{csv_filename}' created successfully.")
else:
    print('Error:', response.status_code)
    print(response.text)
