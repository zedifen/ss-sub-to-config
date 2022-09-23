import json

'''
SIP008 Online Configuration Delivery
{
    "version": 1,
    "servers": [
        {
            // Server UUID to distinguish between servers when updating.
            "id": "27b8a625-4f4b-4428-9f0f-8a2317db7c79",
            "remarks": "Name of the server",
            "server": "example.com",
            "server_port": 8388,
            "password": "example",
            "method": "chacha20-ietf-poly1305",
            "plugin": "xxx",
            "plugin_opts": "xxxxx"
        }, 
        ...
    ],
    // The above fields are mandatory.
    // Optional fields for data usage:
    "bytes_used": 274877906944,
    "bytes_remaining": 824633720832
    // You may add other custom fields in the root object.
}
'''

def loads(s):
    return json.loads(s)


def dumps(obj: dict) -> str:
    return json.dumps(obj, indent=2)


def to_ss_servers_item(server: dict):
    return {
        'id': f"{server['id']}",
        'name': server['remarks'],
        'address': server['server'],
        'port': int(server['server_port']),
        'password': server['password'],
        'method': server['method'],
        'plugin': server['plugin'],
        'plugin_opts': server['plugin_opts'],
    }


def to_russ_servers_item(server: dict):
    return {
        'id': server['id'],
        'name': server['remarks'],
        'server': "{}:{}".format(server['server'], server['server_port']),
        'password': server['password'],
        'method': server['method'],
        'plugin': server['plugin'],
        'plugin_opts': server['plugin_opts'],
    }


def to_ss_config(sub: dict):
    return {
        'servers': list(map(to_ss_servers_item, sub['servers'])),
        'local_address': '127.0.0.1',
        'local_port': 8964,
        'bytes_used': sub['bytes_used'],
        'bytes_remaining': sub['bytes_remaining'],
    }


def to_russ_config(sub: dict):
    return {
        "select": 1,
        "autostart": False,
        "startminimized": False,
        "local_addr": "127.0.0.1:8964",
        "servers": list(map(to_russ_servers_item, sub['servers'])),
    }
