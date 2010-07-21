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

__all__ = ['parse', 'Parser']

import re

# All compiled grammars must be imported manually here.

from netmunge.grammars import cisco_show_arp
from netmunge.grammars import cisco_show_interface_description
from netmunge.grammars import timetra_show_port_description
from netmunge.grammars import timetra_show_router_arp
from netmunge.grammars import timetra_show_router_bgp_summary

# Grammars by their RANCID device type name and command regexp.
# Command regexps are matched exactly; for example, if the router
# output for the commands 'show arp' and 'show arp local' or some
# other suffix are to be handled by the same grammar, the regexp
# must match all relevant suffixes. It must also handle valid
# shortenings of the command that may be passed to it.

GRAMMARS = {
    # Cisco IOS
    ('cisco', r'sh(o|ow)? arp(?: [^|]*)?'): cisco_show_arp,
            
    ('cisco', r'sh(o|ow)? int(?:e|er|erf|erfa|erfac|erface)? desc(?:r|ri|rip|'
     'ript|ripti|riptio|ription)?'): cisco_show_interface_description,

    # Alcatel/Timetra TimOS
    ('timetra', r'sh(o|ow)? rout(?:e|er)? arp(?: [^|]*)?'):
    timetra_show_router_arp,
    
    ('timetra', r'sh(o|ow)? rout(?:e|er)? bgp? su(m|mm|mma|mmar|mmary)?'):
    timetra_show_router_bgp_summary,
    
    ('timetra', r'sh(o|ow)? port? desc(?:r|ri|rip|ript|ripti|riptio|ription)?'):
    timetra_show_port_description,
    
    }


class Parser(object):
    """Netmunge's caching wrapper around Yapps grammars and parsers."""

    def __init__(self):
        self._grammars = {}
        self._regexes = {}

    def get_grammar(self, vendor, command):
        """Returns a relevant grammar module for the vendor and command.

        Args:
          vendor: A string, the vendor name to search for.
          command: A string, the command that was entered.

        Returns:
          A Yapps grammar module.

        Raises:
          ValueError: There was no grammar for the vendor and command.
        """
        if not self._regexes:
            for _v, _c_r in GRAMMARS.iterkeys():             
                if vendor == _v:
                    if not (_c_r + '$') in self._regexes:
                        self._regexes[_c_r + '$'] = {}
                    self._regexes[_c_r + '$'][vendor] = GRAMMARS[(_v, _c_r)]
        for reg in self._regexes.iterkeys():
            # TODO(afort): Build own cache when >100 regexes likely.
            if re.compile(reg).match(command):
                if vendor in self._regexes[reg]:
                    return self._regexes[reg][vendor]
        raise ValueError('No grammar found for (%r, %r)' % (vendor, command))

    def parse(self, vendor, command, router_output):
        """Parses output of a router command for a given vendor.

        Args:
          vendor: A string, the vendor name to search for.
          command: A string, the command that was entered.
          router_output: A string, the router's response - our input.

        Returns:
          An iterable of tuples (the tabulated data).
          The tuples first element is a string which defines what the
          values in the columns mean. The remaining tuple elements are
          the columns.

        Raises:
          ValueError: There was no grammar for the vendor and command.
        """
        grammar = self._grammars.get((vendor, command))
        if grammar is None:
            grammar = self.get_grammar(vendor, command)
            self._grammars[(vendor, command)] = grammar
        return grammar.parse('parse', router_output)


_parser = Parser()


def parse(vendor, command, input):
    return _parser.parse(vendor, command, input)
