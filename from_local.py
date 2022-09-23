from ss_sub_convert import loads, dumps, to_russ_config, to_ss_config

with open('sub.json') as f:
    sub = loads(f.read())


local_address = '127.0.0.1'
local_port = 1080

ss_config = to_ss_config(sub, local_address=local_address, local_port=local_port)
russ_config = to_russ_config(sub, local_address=local_address, local_port=local_port)

with open('config.json', mode='w') as f:
    f.write(dumps(ss_config))


with open('russ.json', mode='w') as f:
    f.write(dumps(russ_config))
