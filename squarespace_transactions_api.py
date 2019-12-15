import requests, json

app_version = '1.0'
api_base_url = 'https://api.squarespace.com'
api_version = '1.0'
user_agent = 'Python Squarespace Transactions API v' + api_version

# ?modifiedAfter={a}&modifiedBefore={b}&cursor={c}


class Squarespace(object):
    """
    The Squarespace class contains the various components needed to call the Squarespace Transactions API.
    """

    def __init__(self, api_key, api_base_url=api_base_url, api_version=api_version):
        self.api_key = api_key
        self.api_base_url = api_base_url
        self.api_version = api_version

        self.http = requests.Session()
        self.http.headers.update({'Authorization': 'Bearer ' + self.api_key})
        self.http.headers.update({'User-Agent': user_agent + '/' + app_version})

    def request(self, path, args=None):
        """ Construct and send a request to Squarespace """
        url = '%s/%s/%s' % (self.api_base_url, self.api_version, path)
        print('Request URL: ' + url)
        return self.validate_request(self.http.get(url, params=args))

    def submit(self, path, object):
        """ Construct an endpoint to post data to Squarespace """
        url = '%s/%s/%s' % (self.api_base_url, self.api_version, path)
        return self.validate_request(self.http.post(url, json=object))

    def validate_request(self, request):
        """ Validates a request before sending """
        if request.status_code == 200 or request.status_code == 201:
            return request.json()
        elif 400 <= request.status_code <= 599:
            raise RuntimeError('Status code: ' + str(request.status_code))

    def request_transaction(self, transaction_id):
        """ 
        Requests a single transaction from the Squarespace Transactions API: 
        https://developers.squarespace.com/commerce-apis/retrieving-documents
        """
        uri = 'commerce/transactions/' + transaction_id
        return self.request(uri)

    def request_transactions(self, **args):
        """ 
        Requests a maximum of 50 transactions from the Squarespace Transactions API: 
        https://developers.squarespace.com/commerce-apis/retrieving-specific-documents
        """
        uri = 'commerce/transactions/'
        return self.request(uri, args)