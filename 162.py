def hex_to_binary(hex_number):
    binary_number = bin(int(hex_number,16))[2:]
    return binary_number

hex_number = input("ใส่เลขฐาน16ลงไปค่าาาา:")
binary_result = hex_to_binary(hex_number)
print(f"เลขฐาน2ของ {hex_number} คือ {binary_result}")