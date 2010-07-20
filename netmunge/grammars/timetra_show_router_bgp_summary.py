# Begin -- grammar generated by Yapps
import sys, re
from yapps import runtime

class TimosShowRouterBgpSummaryScanner(runtime.Scanner):
    patterns = [
        ("'\\={3,}'", re.compile('\\={3,}')),
        ("'\\-{3,}'", re.compile('\\-{3,}')),
        ('\\s+', re.compile('\\s+')),
        ('END', re.compile('$')),
        ('ANY', re.compile('.')),
        ('IPV4', re.compile('([0-9]{1,3}\\.){3}[0-9]{1,3}')),
        ('ASN', re.compile('[0-9]{1,7}')),
    ]
    def __init__(self, str,*args,**kw):
        runtime.Scanner.__init__(self,None,{'\\s+':None,},str,*args,**kw)

class TimosShowRouterBgpSummary(runtime.Parser):
    Context = runtime.Context
    def neighbor(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'neighbor', [])
        IPV4 = self._scan('IPV4', context=_context)
        ASN = self._scan('ASN', context=_context)
        while self._peek('ANY', 'IPV4', "'\\={3,}'", context=_context) == 'ANY':
            ANY = self._scan('ANY', context=_context)
        return (('bgpv4', IPV4, ASN))

    def parse(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'parse', [])
        while self._peek("'\\-{3,}'", 'ANY', context=_context) == 'ANY':
            ANY = self._scan('ANY', context=_context)
        self._scan("'\\-{3,}'", context=_context)
        neigh = set()
        while self._peek("'\\={3,}'", 'IPV4', context=_context) == 'IPV4':
            neighbor = self.neighbor(_context)
            neigh.add(neighbor)
        self._scan("'\\={3,}'", context=_context)
        while self._peek('END', 'ANY', context=_context) == 'ANY':
            ANY = self._scan('ANY', context=_context)
        END = self._scan('END', context=_context)
        return neigh


def parse(rule, text):
    P = TimosShowRouterBgpSummary(TimosShowRouterBgpSummaryScanner(text))
    return runtime.wrap_error_reporter(P, rule)

if __name__ == '__main__':
    from sys import argv, stdin
    if len(argv) >= 2:
        if len(argv) >= 3:
            f = open(argv[2],'r')
        else:
            f = stdin
        print parse(argv[1], f.read())
    else: print >>sys.stderr, 'Args:  <rule> [<filename>]'
# End -- grammar generated by Yapps