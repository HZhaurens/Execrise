'''
题目：判断一个数是否为素数

描述：编写一个Python程序，判断用户输入的一个整数是否为素数。
素数是只能被1和自身整除的大于1的整数。
'''

# 解决方案
def is_prime(number):
    """
    判断一个数是否为素数
    
    参数:
        number (int): 需要判断的整数
    
    返回:
        bool: 如果是素数返回True，否则返回False
    """
    # 处理特殊情况
    if number <= 1:
        return False
    
    # 2是最小的素数
    if number == 2:
        return True
    
    # 偶数（除了2）都不是素数
    if number % 2 == 0:
        return False
    
    # 只需要检查到平方根
    # 如果一个数不是素数，那么它一定有一个因子小于或等于它的平方根
    import math
    sqrt_num = int(math.sqrt(number)) + 1
    
    # 只需要检查奇数因子
    for i in range(3, sqrt_num, 2):
        if number % i == 0:
            return False
    
    return True

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        num = int(input("请输入一个整数: "))
        
        # 判断并显示结果
        if is_prime(num):
            print(f"{num} 是素数")
        else:
            print(f"{num} 不是素数")
            
        # 额外信息：显示小于100的所有素数
        if num < 100:
            print("\n小于100的素数有:")
            primes = [i for i in range(2, 100) if is_prime(i)]
            print(primes)
    except ValueError:
        print("请输入有效的整数!")