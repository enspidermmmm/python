# 自定义报错
class NumError(Exception):
    pass

# 万以内中文数字转阿拉伯数字
def num_count(ch_list):
    num = 0
    number_dict = {
        '零':0,
        '一':1,
        '壹':1,
        '二':2,
        '两':2,
        '贰':2,
        '三':3,
        '叁':3,
        '四':4,
        '肆':4,
        '五':5,
        '伍':5,
        '六':6,
        '陆':6,
        '七':7,
        '柒':7,
        '八':8,
        '捌':8,
        '九':9,
        '玖':9
    }
    places_dict = {
        '十':10,
        '拾':10,
        '百':100,
        '佰':100,
        '千':1000,
        '仟':1000
    }
    if ch_list:
        for i in range(len(ch_list)):
            if ch_list[i] in places_dict:
                num += number_dict[ch_list[i-1]] * places_dict[ch_list[i]]
        if ch_list[-1] in number_dict:
            num += number_dict[ch_list[-1]]
        return num
    else:
        return 0

# 万以上亿以内中文数字转阿拉伯数字
def wannum_num(chnum):
    chnum_dict = {}

    if '万' in chnum:
        chnum_dict['Wan'] = list(chnum.split('万')[0])
        chnum_dict['Ge'] = list(chnum.split('万')[1])
    else:
        chnum_dict['Ge'] = list(chnum)

    Wan_num = 0
    Ge_num = 0
    for i,j in chnum_dict.items():
        if i == 'Wan':
            Wan_num = num_count(j) * 10000
        else:
            Ge_num = num_count(j)
    num = Wan_num + Ge_num
    return num

# 最终版中文数字转阿拉伯数字
def CNnum_num(chnum):
    if '亿' in chnum:
        Yi_num = wannum_num(chnum.split('亿')[0]) * 100000000
        num = wannum_num(chnum.split('亿')[1]) + Yi_num
    else:
        num = wannum_num(chnum)
    return num

# 将字符串反向分割成指定长度的字符串列表(反向re.findall(r'.{lenth}',string))(例:string长度为11,lenth为4,分割为长度分别为3、4、4的字符串并组成列表)
def split2(string,lenth):
    string2 = ''
    strlist = []
    for i in range(1,len(string)+1):
        if i % lenth != 0:
            string2 += string[-i]
            if i == len(string):
                strlist.append(string2)
        else:
            string2 += string[-i]
            strlist.append(string2)
            string2 = ''
    strlist.reverse()
    strlist2 = []
    for i in strlist:
        strlist2.append(i[::-1])
    return strlist2

# 4位及以下阿拉伯数字(str格式)转中文数字
def num4_cnnum(num,CNnumtype): #CHnumtype=True时为大写中文数字,反之为小写
    if CNnumtype:
        j = 1
    else:
        j = 0
    number_dict_list = {
        '0':'零',
        '1':['一','壹'],
        '2':['二','贰'],
        '3':['三','叁'],
        '4':['四','肆'],
        '5':['五','伍'],
        '6':['六','陆'],
        '7':['七','柒'],
        '8':['八','捌'],
        '9':['九','玖']
    }
    places_dict_list = {
        -2:['十','拾'],
        -3:['百','佰'],
        -4:['千','仟'],
    }
    num_list = []
    a = 0
    for i in range(1,len(num)+1):
        if num[-i] != '0':
            a = 1
        if a:
            if i == 1:
                num_list.append(number_dict_list[num[-i]][j])
            else:
                if num[-i] == '0':
                    num_list.append(number_dict_list[num[-i]][j])
                else:
                    num_list.append(number_dict_list[num[-i]][j] + places_dict_list[-i][j])
    # print(num_list)

    a = 1
    chnum = ''
    for i in range(1,len(num_list)+1):
        if num_list[-i] == '零':
            if a:
                chnum += num_list[-i]
                a = 0
        else:
            chnum += num_list[-i]
            a = 1
    return chnum

# 12位及以下阿拉伯数字(str格式)转中文数字
def num_cnnum(num,CNnumtype=False):
    if len(num) < 13:
        num_list = split2(num,4)
        num_list.reverse()
        big_places_list = ['','万','亿']
        cnnum_list = []
        for i in range(len(num_list)):
            cnnum_list.append(num4_cnnum(num_list[i],CNnumtype)+big_places_list[i])
        cnnum_list.reverse()
        cnnum = ''.join(cnnum_list)
        return cnnum
    else:
        raise NumError



if __name__ == '__main__':
    print('''主要函数:CNnum_num(chnum):将中文大小写数字转换为阿拉伯数字;
        num_cnnum(num,CNnumtype=False)将阿拉伯数字转换为中文数字,CNnumtype定义大小写,默认小写;
        split2(string,lenth)规定长度反向分割字符串,例:split2('abcdefghijk',4),返回结果:['abc','defg','hijk']''')