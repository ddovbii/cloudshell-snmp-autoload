from cloudshell.snmp.autoload.core.snmp_oid_template import SnmpMibOidTemplate
from cloudshell.snmp.core.domain.snmp_oid import SnmpMibOid

PORT_DESCR_NAME = SnmpMibOidTemplate("IF-MIB", "ifDescr")
PORT_NAME = SnmpMibOidTemplate("IF-MIB", "ifName")
PORT_DESCRIPTION = SnmpMibOidTemplate("IF-MIB", "ifAlias")
PORT_TYPE = SnmpMibOidTemplate("IF-MIB", "ifType")
PORT_MTU = SnmpMibOidTemplate("IF-MIB", "ifMtu")
PORT_SPEED = SnmpMibOidTemplate("IF-MIB", "ifHighSpeed")
PORT_MAC = SnmpMibOidTemplate("IF-MIB", "ifPhysAddress")
PORT_ADJACENT_REM_TABLE = SnmpMibOid('LLDP-MIB', 'lldpRemSysName')
PORT_ADJACENT_REM_PORT_DESCR = SnmpMibOidTemplate('LLDP-MIB', 'lldpRemPortDesc')
PORT_ADJACENT_LOC_TABLE = SnmpMibOid('LLDP-MIB', 'lldpLocPortDesc')
PORT_AUTO_NEG = SnmpMibOidTemplate('MAU-MIB', 'ifMauAutoNegAdminStatus')
