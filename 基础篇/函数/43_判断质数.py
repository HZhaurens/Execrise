# 43_判断质数.py

def is_prime(num):
    """判断一个数是否为质数
    
    质数是只能被1和自身整除的大于1的整数
    
    Args:
        num: 要判断的整数
        
    Returns:
        布尔值，True表示是质数，False表示不是质数
    """
    # 处理特殊情况
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # 使用6k±1优化的算法检查
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

# 测试
try:
    number = int(input("请输入一个整数: "))
    if is_prime(number):
        print(f"{number}是质数")
    else:
        print(f"{number}不是质数")
        
    # 打印小于等于该数的所有质数
    if number > 1:
        print(f"小于等于{number}的所有质数:")
        for i in range(2, number + 1):
            if is_prime(i):
                print(i, end=" ")
        print()
except ValueError:
    print("请输入有效的整数!")