import vk_api
import configparser
import re

PARSER = configparser.ConfigParser()
PARSER.read('config/vk.conf')
VK_TOKEN = PARSER['AUTH']['TOKEN']
VK_VERSION = PARSER['MISC']['API_VERSION']

VK = vk_api.VkApi(token=VK_TOKEN, api_version=VK_VERSION)
VK = VK.get_api()

def get_subs(vkid):
    subs = VK.users.getSubscriptions(user_id=vkid)
    subs = (str(a) for a in subs['groups']['items'])
    data = VK.groups.getById(group_ids=','.join(subs), fields='description,status')
    parsed = []

    with open('parsed.csv', 'w', encoding='utf-8') as f:
        f.write('Name, Status, Description\n')
        for item in data:
            name = item.get('name', 'None').replace(',', ' ')
            status = item.get('status', 'None').replace(',', ' ')
            desc = item.get('description', 'None').replace(',', ' ')
            string = f'{name}, {status}, {desc}'.replace('\n', ' ') + '\n'
            string = string.replace('ё', 'е')
            print(string)
            f.write(string+'\n')

    # for item in data:
    #     parsed.append((item.get('name'), item.get('status'), item.get('description')))

#Insert VK ID here.
get_subs(12345)