# "show router bgp summary" parser for Alcatel/Timetra TimOS
#

parser TimosShowRouterBgpSummary:
    ignore: '\\s+'

    token END: '$'
    token ANY: '.'
    token IPV4: '([0-9]{1,3}\.){3}[0-9]{1,3}'
    token ASN: '[0-9]{1,7}'

    rule neighbor: IPV4 ASN ( ANY )* {{ return (('bgpv4', IPV4, ASN)) }}
    rule parse: ( ANY )* '\-{3,}' {{ neigh = set() }}
                ( neighbor {{ neigh.add(neighbor) }} )*
                '\={3,}' ( ANY )* END {{ return neigh }}
