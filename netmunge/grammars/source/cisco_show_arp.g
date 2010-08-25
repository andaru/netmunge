# "show arp" parser for Cisco IOS
#

def convert_mac(mac):
  """Converts cisco xxxx.xxxx.xxxx.format to xx:xx:xx:xx:xx:xx format."""
  return '%s:%s:%s:%s:%s:%s' % (mac[0:2],
                                mac[2:4],
                                mac[5:7],
                                mac[7:9],
                                mac[10:12],
                                mac[12:14])


%%


parser CiscoShowArp:
    ignore: '\\s+'
    token MAC: '\\S+'
    token INTF: '\\S+'  
    token END: '$'
    token ANY: '.'
    token IPV4: '([0-9]{1,3}\.){3}[0-9]{1,3}'
    token AGE: '([0-9]+|-)'

    rule entry: 'Internet' IPV4 AGE MAC 'ARPA' INTF
                {{ return (('arpv4', IPV4, convert_mac(MAC), INTF)) }}

    rule parse: {{ arps = set() }} ( ANY )* '(Protocol.*Interface)?'
                (entry {{ arps.add(entry) }})*
                END {{ return arps }}
