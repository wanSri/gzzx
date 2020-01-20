import re


def parse(content, template):
    """解析配置文件
    :param content: 输入的解析文件
    :param template:  输入的匹配规则
    :return: 要返回的字段列表，以及数据
    """
    content = re.sub("[\f\r\t\v]*", "", content)
    # 以！或则#分段，生成数组
    pattern = re.compile('^[!#]', re.M)
    group = re.split(pattern, content)

    # 去除包含特殊字符的特定段
    special = ['shutdown']

    for l in group[:]:
        for s in special:
            if l.find(s) >= 0:
                group.remove(l)
                continue
        # 定义匹配模式
    tu1 = {
        '1': r'\\w+',  # 数字字母下划线
        '2': "[0-9a-zA-z/.:]+",  # 数字，字母斜杠.
        '3': "[0-9a-zA-z-/. =]+",  # 加空格
        '4': "[0-9]+",  # 数字
    }

    # 替换模板并提取内容
    pattern = re.compile(r'{.+?}')
    list1 = re.findall(pattern, template)
    new_list = []
    for l in list1:
        w = l.replace('{', '')
        w = w.replace('}', '')
        ll = w.split(',')
        if ll.__len__() == 1:
            template = template.replace(l, str("(?:" + ll[0] + ")"))

            continue

        if ll[1] in tu1.keys():
            ll[1] = tu1[ll[1]]
        new_list.append(ll)
    nn = list(map(lambda x: x[0], new_list))

    for s in new_list:
        template = re.sub("{" + s[0] + ".+?}", str("(" + s[1] + ")"), template)
    tem_list = template.split('\n')
    results = []
    for lis in group:
        result = []
        h = 0
        for tem in tem_list:
            lenth = re.findall(re.compile(r'(\((?!\?:).+?\))'), tem).__len__()
            n = re.findall(tem, lis, re.M)
            if h == 0 and n.__len__() == 0:
                break
            h += 1
            if len(n) == 0 and lenth == 1:
                result.append('')
            elif len(n) == 0 and lenth > 1:
                for i in range(lenth):
                    result.append('')
            elif type(n[0]) == tuple:
                li = []
                for i in range(n[0].__len__()):
                    li.append([])
                for i in range(n.__len__()):
                    for j in range(n[0].__len__()):
                        li[j].append(n[i][j])
                li_str = list(map(lambda x: ','.join(list(map(lambda y: str(y), x))), li))
                result.extend(li_str)
            else:
                result.append(','.join(list(map(lambda x: str(x), n))))

        if result.__len__() != 0:
            results.append(result)

    return nn, results
