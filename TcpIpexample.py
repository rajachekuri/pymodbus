import time
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient("192.168.2.215", port=502, timeout=3)
client.connect()
print("connected")


read=client.read_coils(address =1,count =3,unit=1)
print(read.bits)

'''read=client.read_holding_registers(address = 1 ,count =2,unit=1)
print(read.registers)'''
