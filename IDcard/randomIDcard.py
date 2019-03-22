# coding:UTF-8
import datetime
import random

'''
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:
1、地址码 
表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
2、出生日期码 
表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 
3、顺序码 
表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。 
4、校验码计算步骤
    (1)十七位数字本体码加权求和公式 
    S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
    Ai:表示第i位置上的身份证号码数字值(0~9) 
    Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
    (2)计算模 
    Y = mod(S, 11)
    (3)根据模，查找得到对应的校验码 
    Y: 0 1 2 3 4 5 6 7 8 9 10 
    校验码: 1 0 X 9 8 7 6 5 4 3 2
'''


class getRandomIDcard:
    """
    生成随机身份证号码
    性别可指定，默认随机，1-男、2-女
    """

    def __init__(self):
        self.sex = 0

    def getCheckBit(self, num17):
        """
        获取身份证最后一位，即校验码
        :param num17: 身份证前17位字符串
        :return: 身份证最后一位
        """
        Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checkCode = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        zipWiNum17 = zip(list(num17), Wi)
        S = sum(int(i) * j for i, j in zipWiNum17)
        Y = S % 11
        return checkCode[Y]

    def getAddrCode(self):
        """
        获取身份证前6位，即地址码
        :return: 身份证前6位
        """
        from IDcard.addr import addr
        addrIndex = random.randint(0, len(addr) - 1)
        return addr[addrIndex]

    def getBirthday(self, start="1950-01-01", end="2017-12-30"):
        """
        获取身份证7到14位，即出生年月日
        :param start: 出生日期合理的起始时间
        :param end: 出生日期合理的结束时间
        :return: 份证7到14位
        """
        days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
        birthday = datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
        return datetime.datetime.strftime(birthday, "%Y%m%d")

    def getRandomIdCard(self, sex=0):
        """
        获取随机身份证
        :param sex: 性别，默认为随机，1-男，2-女
        :return: 返回一个随机身份证
        """
        idNumber, addrName = self.getAddrCode()
        idCode = str(idNumber) + self.getBirthday()
        for i in range(2):
            idCode += str(random.randint(0, 9))

        if sex not in (1, 2) and self.sex == 0:
            self.sex = random.randint(1, 2)
        else:
            self.sex = sex

        idCode += str(random.randrange(self.sex, 9, 2))
        idCode += self.getCheckBit(idCode)
        return idCode


if __name__ == "__main__":
    for item in range(0, 10):
        print(getRandomIDcard().getRandomIdCard())
