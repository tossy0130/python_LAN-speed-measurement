from ping3 import ping, verbose_ping


# print(ping('192.168.254.226'))

print(verbose_ping('192.168.254.204', timeout=0.5, count=8, ttl=64, unit='ms'))
