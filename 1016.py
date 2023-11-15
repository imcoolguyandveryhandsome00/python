def decimal_to_hex(decimal_number):
    hex_number = format(decimal_number, 'x')
    return hex_number

decimal_number = int(input("ใส่เลขฐาน10ลงไปค่าาาา: "))
hex_result = decimal_to_hex(decimal_number)
print(f"เลขฐาน 16 ของ {decimal_number} คือ {hex_result}")
