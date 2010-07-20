# "show port description" parser for Alcatel/Timetra TimOS
#

parser TimosShowPortDescription:
    ignore: '\\s+'
    token PORT: '[0-9/\.A-Za-z]+'
    token DESC: '.*\n'
    token END: '$'
    token ANY: '.'

    rule entry: 
        PORT DESC
        {{ return (('interface_description', PORT.strip(), DESC.strip())) }}

    rule parse: 
        ( ANY )* '\-*' {{ intf = set() }}
        ('Port Id.*Description' |
         'Port.*Slot .+' |
         ANY |
         entry {{ intf.add(entry) }})*
        END {{ return intf }}
