f_read = open("README")
f_write = open("README[复件]", "w")

text = f_read.read()
f_write.write(text)

f_read.close()
f_write.close()