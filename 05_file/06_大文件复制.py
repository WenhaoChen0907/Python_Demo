f_read = open("README")
f_write = open("README[复件]", "w")


while True:
    text = f_read.readline()

    # 判断是否还有内容
    if not text:
        break

    f_write.write(text)

f_read.close()
f_write.close()