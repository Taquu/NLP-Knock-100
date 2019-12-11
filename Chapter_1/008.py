def cipher(target):
    result = ""
    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

target = input("文字列を入力:")

#暗号化
result = cipher(target)
print("暗号化:" + str(result))

#複号化
result2 = cipher(result)
print("復号化:" + str(result2))
