import requests
import configparser


class RequestException(Exception):
        def __init__(self, text, code):
            self.txt = text
            self.code = code

class AccessDenied(Exception):
        def __init__(self):
            self.txt = 'VK API returns AccessDenied error.'

class VKEngine():

    token = None
    master = None
    ver = 5.82

    def __init__(self, token=None, ver=ver):
        if token:
            self.token = token
        self.ver = ver

    def read_config(self, filename):
        # TODO: Use python built-in config parser module
        config = configparser.ConfigParser()
        config.read(filename)
        self.token = config['AUTH']['TOKEN']
        self.ver = config['MISC']['API_VERSION']


    def _req(self, method, **kwargs):

        r = requests.get('https://api.vk.com/method/' + method,
                         params={**kwargs, 'access_token': self.token, 'v':self.ver, 'lang':'ru'}).json()

        if 'error' in list(r):
            code = r['error']['error_code']
            description = r['error']['error_msg']
            if code == 15:
                raise AccessDenied()
            else:
                raise RequestException(f'VK API Returned an error code {code}: {description}', code)
        else:
            return r['response']


    def fetch_user(self, uid, **kwargs):
        data = self._req('users.get', user_ids=uid, **kwargs)
        if len(data) == 1:
            return data[0]
        return data

    def debug_info(self):
        print(f'VK API VERSION: {self.ver}')
        print(f'TOKEN: {self.token}')