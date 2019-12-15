# Squarespace Transactions API

A Python module to access the [Squarespace Transactions API](https://developers.squarespace.com/commerce-apis/transactions-api-overview).

```
data = store.request_transactions()
for t in data['documents']:
	print(t['id'])
```

## Prerequisites

* A Squarespace website eligible for orders and [API key](https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys)

## Accessing the API

### Installation

* Create a virtual environment: `python3 -m venv env`
* Activate the environment: `source env/bin/activate`
* Add your API key as an environment variable: `export SS_API_KEY=<YOUR_API_KEY>`
* Install dependencies: `pip3 install -r requirements.txt`
* Run the application: `python3 test_api.py`

### Using the module

* Add your API key as an environment variable: `export SS_API_KEY=<YOUR_API_KEY>`
* Import the module: `import squarespace_transactions_api`
* Access the API: `store = Squarespace(os.environ.get('SS_API_KEY'))`
* Request a single transaction: `transaction_data = store.request_transaction(transaction_id=transaction_id)`
* Request latest 50 transactions: `transaction_data = store.request_transactions()`

## Contributing & Support

For support, bug reporting, feature requests, improvements, suggestions or questions, please feel free to submit a pull request or open an issue.