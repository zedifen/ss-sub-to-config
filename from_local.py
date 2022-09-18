from ss_sub_convert import loads, dumps, to_russ_config, to_ss_config

with open('sub.json') as f:
    sub = loads(f.read())


ss_config = to_ss_config(sub)
russ_config = to_russ_config(sub)

with open('config.json', mode='w') as f:
    f.write(dumps(ss_config))


with open('russ.json', mode='w') as f:
    f.write(dumps(russ_config))
