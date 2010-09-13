
import os

import unittest

from netmunge.grammars import cisco_show_process_cpu


TEST_DATA = os.path.join('tests', 'testdata')


class CiscoShowProcessCpuTest(unittest.TestCase):
    """Tests for the cisco_show_process_cpu.CiscoShowProcessCpu class."""

    def testCiscoShowArp(self):
        infile = open(os.path.join(TEST_DATA, 'cisco_show_process_cpu'))
        indata = infile.read()
        out = sorted(cisco_show_process_cpu.parse('parse', indata))
        print out

        self.assertEqual(
            out[0], ('cpu_process',
                     '1', '0.00%', '0.00%', '0.00%', 'Chunk Manager'))
        self.assertEqual(
            out[11], ('cpu_process',
                      '109', '8.29%', '2.64%', '0.75%', 'SSH Process'))

        
if __name__ == '__main__':
    unittest.main()
