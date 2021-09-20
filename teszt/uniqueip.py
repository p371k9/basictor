import os, sys
sys.path.append(os.path.relpath(".."))
from basictor import BasicTor

from requests import get
import unittest

class IpTest(unittest.TestCase):
    # https://stackoverflow.com/questions/17353213/init-for-unittest-testcase
    def __init__(self, *args, **kwargs):
        super(IpTest, self).__init__(*args, **kwargs)
        self.ips = list()    
        self.ips.append(self.get_ip()) 

    tor_proxies = {     
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'        
    }    
       
    def get_ip(self):
        return get('http://icanhazip.com', proxies = self.tor_proxies).text.strip()
        
    def test_uniqueip(self):
        """
        Testing how unique the generated Tor IPs are 
        """
        bt = BasicTor()  
        for i in range(12):  # Modify it if you want less or more tests!
            with self.subTest(i=i):
                bt.new_tor_identity()
                the_ip = self.get_ip()                
                print(the_ip)
                self.assertNotIn(the_ip, self.ips)
                self.ips.append(the_ip)

if __name__ == '__main__':
    unittest.main()                
