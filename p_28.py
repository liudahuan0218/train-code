import re
tels=["13100001234","18912344321","10086","18800007777"]
for tel in tels:
    ret=re.match("1\d{9}[0-3,5-6,8-9]",tel)
    if ret:
        print("结果是：",ret.group())
    else:
        print("%s不是想要的手机号" % tel)
