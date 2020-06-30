from vk_api import vk_api
import configparser
import time

lotsofids = []

def process_vk(domain):
    # TODO: OOP version of User object


    profile_fields = [
        'is_closed',
        'about',
        'activities',
        'career',
        'education',
        'interests',
        'occupation',
        'status'
    ]

    # Obtaining info from user profile

    #userinfo = vk.users.get(user_ids=domain, 
    #                        fields=','.join(profile_fields))

    # VK user ID
    #uid = userinfo[0]['id']
    
    # Obtaining user subscriptions
    communities = vk.users.getSubscriptions(user_id=domain)
    communities = communities['groups']['items']

    return communities

def parse_link(link):
    # We need to identify the link source
    # It can be either VK or Facebook
    # In other cases we raise an exception

    # TODO: Add domain-only input support

    if 'vk.com/' in link:
        print('Found VK profile link.')
        domain = ''.join(link.split('vk.com/')[1:])
        print(f'User domain is {domain}')
        process_vk(domain)

    else:
        raise TypeError('This link is not supported')


def print_welcome():
    print('''
Это - тестовая версия CUDDLE.
Пожалуйста, укажите ссылку на страницу ВКонтакте.
'''
        )

def test():
    data = vk.friends.get(user_id=11798189)
    data = data['items']
    temp = []
    counter = 0
    for friend in data:
        counter += 1
        print(f'working with {counter} of {len(data)}...')
        try:
            new = process_vk(friend)
            temp.extend(new)
            time.sleep(0.2)
        except vk_api.ApiError:
            time.sleep(0.2)
            continue

    temp = set(temp)
    with open('comms.txt', 'w', encoding='utf-8') as file:
        for item in temp:
            file.write(str(item) + '\n')


def main():
    while True:
        print_welcome()

        # Requesting profile link from user.
        link = str(input('> '))
        if link == 'done':
            setofids = set(lotsofids)
            with open('ids.txt', 'w', encoding='utf-8') as f:
                for i in setofids:
                    f.write(str(i) + '\n')

        else:
            parse_link(link)



# Initializing all modules responsible for working with APIs

config = configparser.ConfigParser()
config.read('config/vk.conf')

ACCESS_TOKEN = config['AUTH']['TOKEN']
API_VERSION = config['MISC']['API_VERSION']

vk = vk_api.VkApi(token=ACCESS_TOKEN, api_version=API_VERSION)
vk = vk.get_api()

if __name__ == '__main__':
    test()