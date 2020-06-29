from vk_engine import VKEngine

def process_vk(domain):
    # TODO: OOP version of User object.

    # Getting info
    pass
    # Getting subscriptions
    vk_engine.fetch_user(domain)


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


def main():  
    print_welcome()

    # Requesting profile link from user.
    link = str(input('> '))
    parse_link(link)


# Initializing all modules responsible for working with APIs
# TODO: Use vk_api?
vk_engine = VKEngine()
vk_engine.read_config('config/vk.conf')

# DEBUGGING
vk_engine.debug_info()


if __name__ == '__main__':
    main()