import vk_api
import configparser
from tokenizer import tokenize


# Getting info from .conf file to connect to VK API
PARSER = configparser.ConfigParser()
PARSER.read('config/vk.conf')
VK_TOKEN = PARSER['AUTH']['TOKEN']
VK_VERSION = PARSER['MISC']['API_VERSION']

# Initialising VK API object
VK = vk_api.VkApi(token=VK_TOKEN, api_version=VK_VERSION)
VK = VK.get_api()


# Call this function with a valid VK ID
# It returns dictionary {word : number of matches}

def get_subs(domain):
    # TODO: Remove subscriptions limit
    # VK API allows parse maximum 500 communities per request.
    limit = 300

    req = VK.users.get(user_ids=domain)
    vkid = req[0]['id']
    name = req[0]['first_name'] + ' ' + req[0]['last_name']

    subs = VK.users.getSubscriptions(user_id=vkid)
    subs = [str(a) for a in subs['groups']['items'][:limit]]


    data = VK.groups.getById(group_ids=','.join(subs), fields='description,status')
    words = {}

    for item in data:
        tokens = tokenize(item.get('name','') + ' ' + item.get('status','') + ' ' + item.get('description',''))
        for word in tokens:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
                
    return name, words

if __name__ == "__main__":
    q = int(input('Enter valid VK ID: '))
    print(get_subs(q))