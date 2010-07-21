netmunge: eating your router's dogfood
--------------------------------------

Netmunge does the dirty job of parsing network device ASCII text
output for signs of life in an attempt to bring sanity to you, the
network engineer or network tools developer.

It can be used to plug into a multi-router command-line interface,
or used as a means of parsing complicated text output from RANCID.

It uses Yapps v2 grammars (see ``netmunge/grammars/source``) and parser
modules built by that system are included in the source code of `netmunge`.


Install
=======

::

  $ pip install netmunge

Or something. It's just a library, so if you want it to do anything,
you'll need to pass it some data.  We suggest feeding it with Notch,
since that will handle the (sort of expected) network router data
source.

Use
====

The 'netmunge' module creates an instance of its Parser class during
module initialisation.  Call the module's ``parse`` method, as below:

::

  import netmunge

  input = """
  Protocol  Address          Age (min)  Hardware Addr   Type   Interface
  Internet  10.0.0.0                -   ca00.1eb7.0038  ARPA   GigabitEthernet2/0
  Internet  10.0.0.1              147   ca01.1eb7.001c  ARPA   GigabitEthernet2/0
  """
  
  def parse_arp():
    return netmunge.parse('cisco', 'show arp', input) 

  for tup in parse_arp():
    print ','.join(tup)


