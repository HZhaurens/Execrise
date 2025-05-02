'''
题目：计算1到100的和

描述：编写一个Python程序，计算从1到100的所有整数的和。
'''

# 解决方案
def sum_from_1_to_n(n):
    """
    计算从1到n的整数和
    
    参数:
        n (int): 上限值
    
    返回:
        int: 从1到n的整数和
    """
    # 方法一：使用循环
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_from_1_to_n_formula(n):
    """
    使用数学公式计算从1到n的整数和
    公式: sum = n * (n + 1) / 2
    
    参数:
        n (int): 上限值
    
    返回:
        int: 从1到n的整数和
    """
    # 方法二：使用数学公式
    return n * (n + 1) // 2

# 示例输出
if __name__ == "__main__":
    n = 100
    
    # 使用循环计算
    loop_sum = sum_from_1_to_n(n)
    print(f"使用循环计算1到{n}的和: {loop_sum}")
    
    # 使用公式计算
    formula_sum = sum_from_1_to_n_formula(n)
    print(f"使用公式计算1到{n}的和: {formula_sum}")