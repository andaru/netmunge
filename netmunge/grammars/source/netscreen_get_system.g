parser NetscreenGetSystem:
    ignore: '\\s+'
    token NUM: '[0-9]+'
    token WORD: '\\S+'
    token END: '$'

    rule item: "Product Name:" WORD {{ return ('product_name', WORD) }}
             | "Serial Number:" NUM {{ return ('serial', NUM) }}
             | "Hardware Version:" WORD {{ return ('hardware_version', WORD) }}
             | "File Name:" WORD {{ return ('image_name', WORD) }}
             
    rule get_system: {{ l = set() }} ( item {{ l.add(item) }} | '.' )* END
                     {{ return l }}
    

  
        
