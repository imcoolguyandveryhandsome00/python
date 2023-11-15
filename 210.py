def binary_to_decimal(binary_number):
    decimal_number = int(binary_number,2)
    return decimal_number

binary_number = input(" ใส่เลขฐาน2ลงไปค่าาาา: ")
decimal_result = binary_to_decimal(binary_number)

print(f"เลขฐาน 10 ของ {binary_number} คือ{decimal_result}")