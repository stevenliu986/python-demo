def str_reverse(s):
    """
    字符反转
    :param s: 要反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    按照下标x和y对字符串进行切片
    :param s: 字符串
    :param x: 起始下标
    :param y: 结束下标
    :return: 字符串切片
    """
    return s[x:y]