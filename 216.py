def binary_to_hex(binary_number):
    hex_number = hex(int(binary_number,2))[2:].upper()
    return hex_number

binary_number = input("ใส่เลขฐาน2ลงไปค่าาาา: ")
hex_result = binary_to_hex(binary_number)
print(f"เลขฐาน 16 ของ {binary_number} คือ {hex_result}")
