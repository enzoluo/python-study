def format_str(field, tablename, where):
    '''
    typecode    必选
    s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
    r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
    c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
    o，将整数转换成 八  进制表示，并将其格式化到指定位置
    x，将整数转换成十六进制表示，并将其格式化到指定位置
    d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
    e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
    E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
    f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
    F，同上
    g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
    G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
    %，当字符串中存在格式化标志时，需要用 %%表示一个百分号
    '''
    # url = "select %s " % field
    # url = "select %s from %s " % (field, tablename)
    url = "select %s from %s where %s" % (field, tablename, where)
    print(url)


if __name__ == "__main__":
    # 普通操作替换字符串
    # 1、使用 + 拼接
    common_str1 = 'name:' + 'lisi'
    print(common_str1)

    # 2、使用 repalace 替换
    common_str2 = 'name:$name'.replace('$name', 'lisi')
    print(common_str2)

    # 3、使用 % 格式化
    common_str3 = 'name:%s' % 'lisi'
    print(common_str3)

    format_str('user_name', 'data_user', 'where')
