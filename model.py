import ping3
import read_ip

# ip_addresses = read_ip.read_ip()
# for ip_address in ip_addresses:
#     print(f"IP-address {ip_address} ping {ping3.ping(ip_address, timeout=1, unit='ms')}")


def ping_ip(ip_address):
    ping = ping3.ping(ip_address, timeout=3, unit='ms')
    if ping not in [False, None]:
        return f'Ping-{round(ping, 2)} ms'
    else:
        return 'Disconnect'

# ip_address = '192.168.186.106'
# print(ping_ip(ip_address))

# print(ping3.ping('192.168.186.117', timeout=5, unit='ms'))
# print(ping3.ping('192.168.186.113', timeout=5, unit='ms'))
# print(ping3.ping('192.168.186.191', timeout=5, unit='ms'))
# print(ping3.ping('192.168.186.192', timeout=5, unit='ms'))
# # print(ping3.ping('mail.ru', timeout=1, unit='ms'))

# ping3.verbose_ping('192.168.186.107', count=5)
# print(ping3.ping('192.168.186.107', timeout=1, unit='ms'))
