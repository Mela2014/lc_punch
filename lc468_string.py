class Solution:
    def validIPAddress(self, IP: str) -> str:
        # check IPv4 or IPv6
        if IP.count(".") == 3:
            # IPv4 address validation
            return "IPv4" if self.checkIPv4(IP) else "Neither"
        elif IP.count(":") == 7:
            # IPv6 address validation
            return "IPv6" if self.checkIPv6(IP) else "Neither"
        else:
            return "Neither"

    def checkIPv4(self, IP):
        tokens = IP.split(".")
        for token in tokens:
            if not token.isdigit() or len(token) != len(str(int(token))) or int(token) > 255:
                return False
        return True

    def checkIPv6(self, IP):
        tokens = IP.split(":")
        for token in tokens:
            if len(token) <1 or len(token) > 4 or any(x in token for x in "ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ"):
                return False
        return True

from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"

import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')
        if patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if patten_IPv6.match(IP) else "Neither" 
