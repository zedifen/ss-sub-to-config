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
        'id': f"{server['id']}",
        'name': server['remarks'],
        'server': "{}:{}".format(server['server'], server['server_port']),
        'password': server['password'],
        'method': server['method'],
        'plugin': server['plugin'],
        'plugin_opts': server['plugin_opts'],
    }


def to_ss_config(sub: dict, local_address: str = '127.0.0.1', local_port: int = 8964):
    return {
        'servers': list(map(to_ss_servers_item, sub['servers'])),
        'local_address': local_address,
        'local_port': local_port,
        'bytes_used': sub.get('bytes_used', 1024),
        'bytes_remaining': sub.get('bytes_remaining', 1024),
    }


def to_russ_config(sub: dict, local_address: str = '127.0.0.1', local_port: int = 8964):
    return {
        "select": 1,
        "autostart": False,
        "startminimized": False,
        "local_addr": f"{local_address}:{local_port}",
        "servers": list(map(to_russ_servers_item, sub['servers'])),
    }
