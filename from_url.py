subscribe_url = 'https://some.v2board.site/api/v1/client/subscribe?token=TOKEN&flag=shadowsocks'

import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(subscribe_url, headers=headers)

with urllib.request.urlopen(req) as response:
    return_content = response.read()


from ss_sub_convert import loads, dumps, to_russ_config, to_ss_config

sub = loads(return_content)

ss_config = to_ss_config(sub)
russ_config = to_russ_config(sub)

with open('config.json', mode='w') as f:
    f.write(dumps(ss_config))


with open('russ.json', mode='w') as f:
    f.write(dumps(russ_config))
