import csv
import re
from simplegmail import Gmail
from simplegmail.query import construct_query

# Function to extract the email address from the sender field
def extract_email(sender):
    match = re.search(r'[\w\.-]+@[\w\.-]+', sender)
    if match:
        email = match.group(0).strip().lower()  # Strip whitespace and convert to lowercase
        return email
    return None

# Function to load email addresses from a CSV file
def load_important_addresses(file_path):
    addresses = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            addresses.append(row['email'].strip().lower())  # Strip whitespace and convert to lowercase
    return addresses

# Function to mark emails appropriately
# Args taken give age range in days and file path
def mark_emails_based_on_importance(older_than_days, newer_than_days, file_path='important_addresses.csv'):
	print("Loading important addresses from:", file_path)
	important_addresses = load_important_addresses(file_path)
	print("Important addresses loaded.")
	
	# Initialize the Gmail object
	gmail = Gmail()
	print("Gmail object initialized.")
	
	# Construct the query parameters to get emails from the past 10 days
	query_params = {
		"older_than": (older_than_days, "day"),
		"newer_than": (newer_than_days, "day"),
		"label": "inbox"  # Ensure we are targeting the Inbox only
	}
	print("Query parameters constructed:", query_params)
	
	# Retrieve messages based on the query parameters
	messages = gmail.get_messages(query=construct_query(query_params))
	print("Messages retrieved:", len(messages))
	
	# Counters for important and unimportant messages
	important_count = 0
	unimportant_count = 0
	
	# Iterate over the messages and mark them accordingly
	for message in messages:
		if message:  # Check message is not None
			from_address = extract_email(message.sender)
                
			try:
				if from_address in important_addresses:
					print("Marking as important:", from_address)
					message.mark_as_important()
					important_count += 1
				else:
					print("Trashing:", from_address)
					message.trash()
					unimportant_count += 1
			except Exception as e:
				print("Error processing message from:", from_address, "\nError:", e)
	print("Messages marked as important:", important_count)
	print("Messages marked as trash:", unimportant_count)

if __name__ == "__main__":
    older_than_days = 5  # Change this value as needed
    newer_than_days = 90   # Change this value as needed
    mark_emails_based_on_importance(older_than_days, newer_than_days)      
