def hex_to_decimal(hex_number):
    decimal_number = int(hex_number,16)
    return decimal_number

hex_number = input("ใส่เลขฐาน16ลงไปค่าาาา: ")
decimal_result = hex_to_decimal(hex_number)
print(f"เลขฐาน 10 ของ {hex_number} คือ {decimal_result}")