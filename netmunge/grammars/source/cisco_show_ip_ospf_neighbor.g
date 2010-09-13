# "show ip ospf neighbor" parser for Cisco IOS
#


%%


parser CiscoShowIpOspfNeighbor:
    ignore: '\\s+'
    token PRIO: '[0-9]+'
    token STATE: '[A-ZA-z0-9/\.]+'
    token INTF: '[A-ZA-z0-9/\.]+'
    token END: '$'
    token ANY: '.'
    token OPER: '(up|down|admin down).*'
    token ADMIN: '(up|down|admin down)'
    token IPV4: '([0-9]{1,3}\.){3}[0-9]{1,3}'
    token IPV4_2: '([0-9]{1,3}\.){3}[0-9]{1,3}'
    token TIME3: '([0-9]{2}:[0-9]{2}:[0-9]{2})'

    rule neighbor:
        IPV4 PRIO STATE ( "-" )? TIME3 IPV4_2 INTF
        {{ return (('ospf_neighbor', IPV4, PRIO, STATE, TIME3, INTF)) }}
        
    rule parse:
        ( ANY* ) 'Neighbor.*Interface' {{ neigh = set() }}
        (neighbor {{ neigh.add(neighbor) }})*
        END {{ return neigh }}
