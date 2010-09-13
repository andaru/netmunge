# "show process cpu" parser for Cisco IOS
#

def strip(s):
    return s.strip()

%%


parser CiscoShowProcessCpu:
    ignore: '\\s+'
    token ANY: '.'
    token END: '$'
    token PID: '[0-9]+'
    token NUM: '[0-9]+'
    token SEC5: '[0-9\.%]+'
    token MIN1: '[0-9\.%]+'
    token MIN5: '[0-9\.%]+'
    token PROC: '[^ ].+'

    rule row:
        PID NUM NUM NUM SEC5 MIN1 MIN5 NUM PROC
        {{ return (('cpu_process', PID, SEC5, MIN1, MIN5, strip(PROC))) }}

    rule parse:
        ( ANY* ) 'PID.*Process' {{ procs = set() }}
        ( row {{ procs.add(row) }} )*
        END {{ return procs }}
