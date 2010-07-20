# "show router arp [dynamic|local|...]" parser for Alcatel/Timetra TimOS
#

parser TimosShowRouterArp:
    ignore: '\\s+'
    token NUM: '[0-9]+'
    token WORD: '\\S+'
    token INTF: '\\S+'  
    token END: '$'
    token ANY: '.'
    token IPV4: '([0-9]{1,3}\.){3}[0-9]{1,3}'
    token MAC: '([0-9a-f]{2}:){5}[0-9a-f]{2}'
    token EXPIRY: '[0-9]{2}h[0-9]{2}m[0-9]{2}s'

    rule entry: IPV4 MAC EXPIRY WORD INTF
                {{ return (('arp3tuple', IPV4, MAC, INTF)) }}

    rule parse: ( ANY )* '\-{3,}' {{ arps = set() }}
                (entry {{ arps.add(entry) }})*
                '\-{3,}' {{ return arps }}
