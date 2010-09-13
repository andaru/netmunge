
import os

import unittest

from netmunge.grammars import cisco_show_ip_ospf_neighbor


TEST_DATA = os.path.join('tests', 'testdata')


class CiscoShowIpOspfNeighborTest(unittest.TestCase):
    """Tests for cisco_show_ip_ospf_neighbor.CiscoShowIpOspfNeighbor class."""

    def testCiscoShwoIpOspfNeighbor(self):
        infile = open(os.path.join(TEST_DATA, 'cisco_show_ip_ospf_neighbor'))
        indata = infile.read()
        out = sorted(cisco_show_ip_ospf_neighbor.parse('parse', indata))

        self.assertEqual(
            out[0], ('ospf_neighbor', '10.255.0.0', '0', 'FULL/',
                     '00:00:33', 'GigabitEthernet3/0'))

        self.assertEqual(
            out[1],('ospf_neighbor', '10.255.0.2', '0', 'FULL/',
                    '00:00:31', 'GigabitEthernet2/0'))
        
        
if __name__ == '__main__':
    unittest.main()
