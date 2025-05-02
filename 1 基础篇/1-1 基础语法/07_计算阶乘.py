'''
题目：计算一个数的阶乘

描述：编写一个Python程序，计算用户输入的一个非负整数的阶乘。
阶乘的定义：n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1
特殊情况：0! = 1
'''

# 解决方案
def factorial_iterative(n):
    """
    使用迭代方式计算阶乘
    
    参数:
        n (int): 需要计算阶乘的非负整数
    
    返回:
        int: n的阶乘
    """
    # 处理特殊情况
    if n < 0:
        return "阶乘不能用于负数"
    
    # 0的阶乘为1
    if n == 0:
        return 1
    
    # 计算阶乘
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

def factorial_recursive(n):
    """
    使用递归方式计算阶乘
    
    参数:
        n (int): 需要计算阶乘的非负整数
    
    返回:
        int: n的阶乘
    """
    # 处理特殊情况
    if n < 0:
        return "阶乘不能用于负数"
    
    # 基本情况：0的阶乘为1
    if n == 0 or n == 1:
        return 1
    
    # 递归计算
    return n * factorial_recursive(n - 1)

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        num = int(input("请输入一个非负整数: "))
        
        # 检查输入是否为非负整数
        if num < 0:
            print("请输入非负整数!")
        else:
            # 使用迭代方式计算
            iterative_result = factorial_iterative(num)
            print(f"{num}的阶乘(迭代方式): {iterative_result}")
            
            # 使用递归方式计算
            recursive_result = factorial_recursive(num)
            print(f"{num}的阶乘(递归方式): {recursive_result}")
    except ValueError:
        print("请输入有效的整数!")