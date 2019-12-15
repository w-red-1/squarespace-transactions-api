import os

from squarespace_transactions_api import Squarespace

store = Squarespace(os.environ.get('SS_API_KEY'))

data = store.request_transactions()

transaction = store.request_transaction('e9be28bc-d359-4480-87b4-77564d5921f4')
print(transaction)

for t in data['documents']:
	print(t['id'])