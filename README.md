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

## License

Copyright 2019 @ w-red-1

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.