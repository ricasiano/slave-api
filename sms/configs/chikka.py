import os;
def chikka_config():
    config = {
        'client_id' : os.environ.get('CHIKKA_CLIENT_ID'),
        'secret_key' : os.environ.get('CHIKKA_SECRET_KEY'),
        'shortcode' : os.environ.get('CHIKKA_SHORTCODE'),
        'message_type' : 'REPLY',
        'request_cost': 'FREE',
        'url' : 'https://post.chikka.com/smsapi/request',
        'salt' : 'chikka_api_1',
    }
    return config
