

import os

import unittest

from netmunge.grammars import timetra_show_router_bgp_summary


TEST_DATA = os.path.join('tests', 'testdata')


class TimetraShowRouterBgpSummaryTest(unittest.TestCase):
    """Tests for the timetra_show_router_bgp_summary module."""

    def testTimetraShowRouterBgpSummary(self):
        infile = open(os.path.join(TEST_DATA, 'timetra_show_router_bgp_summary'))
        indata = infile.read()
        out = sorted(timetra_show_router_bgp_summary.parse('parse', indata))

        self.assertEqual(out[0], ('bgpv4', '10.0.1.57', '64514'))
        self.assertEqual(out[1], ('bgpv4', '121.200.225.146', '64536'))
        self.assertEqual(out[2], ('bgpv4', '121.200.225.158', '64651'))
        self.assertEqual(out[3], ('bgpv4', '172.16.0.21', '64514'))
        self.assertEqual(out[4], ('bgpv4', '172.16.128.13', '64514'))
        self.assertEqual(out[5], ('bgpv4', '172.16.128.8', '64514'))
        
        
if __name__ == '__main__':
    unittest.main()
