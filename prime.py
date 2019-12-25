# 寻找num以内所有质数
def prime_num(num):
    prime_list = []

    # 质数定义:在大于1的自然数中,除了1和它本身以外不再有其他因数的自然数
    if num == 2:
        # print(f'{num}是质数')
        prime_list.append(num)
    for i in range(2,num):
        if i == 2:
            # print(f'{i}是质数')
            prime_list.append(i)
        for j in range(2,i):
            if i % j:
                if i-1 == j:
                    # print(f'{i}是质数')
                    prime_list.append(i)
            else:
                # print(f'{j}是{i}的因数,所以{i}不是质数')
                break
    return prime_list



if __name__ == '__main__':
    print(prime_num(1000))