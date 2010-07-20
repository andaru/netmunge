
import os

import unittest

from netmunge.grammars import cisco_show_arp


TEST_DATA = os.path.join('tests', 'testdata')


class CiscoShowArpTest(unittest.TestCase):
    """Tests for the cisco_show_arp.CiscoShowArp class."""

    def testCiscoShowArp(self):
        infile = open(os.path.join(TEST_DATA, 'cisco_show_arp'))
        indata = infile.read()
        out = sorted(cisco_show_arp.parse('parse', indata))

        self.assertEqual(
            out[0], ('arpv4',
                     '10.0.0.0', 'aa:02:12:2f:38:00', 'GigabitEthernet2/0'))
        self.assertEqual(
            out[1], ('arpv4',
                     '192.168.1.13', '00:39:8e:f8:9c:42', 'GigabitEthernet1/0'))
        self.assertEqual(
            out[2], ('arpv4',
                     '192.168.1.15', '00:3c:10:30:da:05', 'GigabitEthernet1/0'))
        self.assertEqual(
            out[3],
            ('arpv4',
             '192.168.1.200', 'ca:03:12:2f:00:1c', 'GigabitEthernet1/0'))
        self.assertEqual(
            out[4],
            ('arpv4',
             '192.168.1.254', '00:3c:10:0e:fe:ac', 'GigabitEthernet1/0'))
        
        
if __name__ == '__main__':
    unittest.main()
