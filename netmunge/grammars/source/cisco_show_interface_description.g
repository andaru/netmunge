# "show arp" parser for Cisco IOS
#

def _d(oper_status):
  """Returns the description from the mixed oper status/optional description"""
  if 'up' in oper_status:
    return oper_status.split('up')[1].strip()
  else:
    return oper_status.split('down')[1].strip()


%%


parser CiscoShowInterfaceDescription:
    ignore: '\\s+'
    token INTF: '[A-ZA-z]{2,3}[0-9/\.]+'
    token END: '$'
    token ANY: '.'
    token OPER: '(up|down|admin down).*'
    token ADMIN: '(up|down|admin down)'

    rule entry:
        INTF ADMIN OPER
        {{ return (('interface_description', INTF, _d(OPER))) }}

    rule parse: 
        ( ANY* ) 'Interface.*Description' {{ ints = set() }}
        (entry {{ ints.add(entry) }})*
        END {{ return ints }}
