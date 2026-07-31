def hash_index(key, table_size):
    return key % table_size

key = int(input("Enter key: "))
table_size = int(input("Enter table size: "))

index = hash_index(key, table_size)

print("Hash Index =", index)