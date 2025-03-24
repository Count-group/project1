import requests


class HTTPRequestUtility:
    def __init__(self):
        pass

    def send_request(self, url, method='GET', params=None, headers=None):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, params=params, headers=headers)
            elif method.upper() == 'POST':
                response = requests.post(url, data=params, headers=headers)
            elif method.upper() == 'PUT':
                response = requests.put(url, data=params, headers=headers)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                print(f"不支持的请求方法: {method}")
                return None

            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP 错误发生: {http_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'请求错误发生: {req_err}')
        return None

    