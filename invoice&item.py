import requests
import csv

# Authentication
access_token = ""
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Fetch Invoice Data
invoices_url = "https://books.zoho.com/api/v3/invoices"
invoices_response = requests.get(invoices_url, headers=headers)
invoices_data = invoices_response.json()

# Fetch Item Data
items_url = "https://books.zoho.com/api/v3/items"
items_response = requests.get(items_url, headers=headers)
items_data = items_response.json()

# Check the structure of invoices_data
print("Invoices Data:", invoices_data)

# Check the structure of items_data
print("Items Data:", items_data)

# Combine invoice and item data horizontally
combined_data = []

# Determine the correct key to access invoice data
invoice_key = 'invoices' if 'invoices' in invoices_data else 'data'

# Ensure that both datasets have the same number of rows
num_rows = min(len(invoices_data[invoice_key]), len(items_data['items']))

# Prepare combined rows
for i in range(num_rows):
    invoice = invoices_data[invoice_key][i]
    line_item = invoice.get('line_items', [{}])[0]
    item = items_data['items'][i]

    combined_row = [
        invoice['invoice_id'],
        invoice['customer_name'],
        invoice['total'],
        line_item.get('item_id', ''),
        line_item.get('item_name', ''),
        line_item.get('rate', ''),
        item['item_id'],
        item['name'],
        item['rate']
    ]
    combined_data.append(combined_row)

# Write combined data to a CSV file
csv_file_path =
try:
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write headers
        writer.writerow(['Invoice ID', 'Customer Name', 'Invoice Amount', 'Line Item ID', 'Line Item Name', 'Line Item Rate',
                         'Item ID', 'Item Name', 'Item Rate'])

        # Write combined data
        writer.writerows(combined_data)

    print("CSV file has been saved to:", csv_file_path)
except Exception as e:
    print("An error occurred while saving the CSV file:", e)
