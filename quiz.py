from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABckpjCYpDOBQ1d1K1E1m-eo_pEvyrTRpJU4lkH_Yf6FU_8IPwOM1yDNk-F5_5tT-NSwH0QxXny0blzf5MSTgw_RReWD71S3z0kUY34hzGekIEqP6zUdkRh8f4T_5CXbaiMll8SDMJe92WZN6sPhos3KDH4ujA09GG-rHFeQF0f_34YQsFY6NEPxWhqHkNvaJDTa0au'

f = Fernet(key)
print(f.decrypt(message))