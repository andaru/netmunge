
import os

import unittest

from netmunge.grammars import cisco_show_interface_description


TEST_DATA = os.path.join('tests', 'testdata')


class CiscoShowInterfaceDescriptionTest(unittest.TestCase):
    """Tests for the cisco_show_interface_description module."""

    def testCiscoShowInterfaceDescription(self):
        infile = open(
            os.path.join(TEST_DATA, 'cisco_show_interface_description'))
        indata = infile.read()
        out = sorted(cisco_show_interface_description.parse('parse', indata))

        self.assertEqual(
            out[0], ('interface_description', 'Et0/0', ''))
        self.assertEqual(
            out[1], ('interface_description', 'Gi0/0', ''))
        self.assertEqual(
            out[2], ('interface_description', 'Gi1/0', 'ubuntu:tap0'))
        self.assertEqual(
            out[3], ('interface_description', 'Gi2/0', 'gi1/0 r2'))
        
        
if __name__ == '__main__':
    unittest.main()
