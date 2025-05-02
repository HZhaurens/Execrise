# 44_计算约数.py

def find_divisors(num):
    """计算一个数的所有约数
    
    Args:
        num: 要计算约数的正整数
        
    Returns:
        包含所有约数的列表
    """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

# 测试
try:
    number = int(input("请输入一个正整数: "))
    if number <= 0:
        print("请输入正整数!")
    else:
        result = find_divisors(number)
        print(f"{number}的所有约数: {result}")
        print(f"{number}共有{len(result)}个约数")
        
        # 判断是否为完全数（所有真约数之和等于本身）
        # 真约数是除了数本身以外的所有约数
        true_divisors_sum = sum(result) - number
        if true_divisors_sum == number:
            print(f"{number}是完全数")
        else:
            print(f"{number}不是完全数")
except ValueError:
    print("请输入有效的整数!")