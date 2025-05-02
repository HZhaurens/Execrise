# 40_计算阶乘递归.py

def factorial(n):
    """使用递归计算阶乘
    
    Args:
        n: 要计算阶乘的非负整数
        
    Returns:
        n的阶乘
    """
    # 基本情况：0的阶乘为1
    if n == 0 or n == 1:
        return 1
    # 递归情况：n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# 测试
try:
    num = int(input("请输入一个非负整数: "))
    if num < 0:
        print("请输入非负整数!")
    else:
        result = factorial(num)
        print(f"{num}的阶乘是: {result}")
except ValueError:
    print("请输入有效的整数!")