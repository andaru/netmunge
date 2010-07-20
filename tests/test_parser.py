#!/usr/bin/env python
#
# Copyright 2010 Andrew Fort. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os

import unittest

from netmunge import parser


TEST_DATA = os.path.join('tests', 'testdata')


class ParserTest(unittest.TestCase):
    """Tests for the parser module."""

    def setUp(self):
        self.parser = parser.Parser()
        
    def testCiscoShowArp(self):
        """This should match."""
        g1 = self.parser.get_grammar('cisco', 'show arp')
        self.assert_('CiscoShowArp' in dir(g1))
        self.assert_('parse' in dir(g1))

    def testCiscoShowArpValidTrailing(self):
        """This should also match."""
        g2 = self.parser.get_grammar('cisco', 'show arp local')        
        self.assert_('CiscoShowArp' in dir(g2))
        self.assert_('parse' in dir(g2))

    def testCiscoShowArpError(self):
        """These commands shouldn't match."""
        self.assertRaises(ValueError,
                          self.parser.get_grammar, 'cisco', 'show arp2')
        self.assertRaises(ValueError,
                          self.parser.get_grammar, 'cisco', 'show arpness')
        
        
if __name__ == '__main__':
    unittest.main()
