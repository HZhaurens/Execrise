'''
题目：交换两个变量的值

描述：编写一个Python程序，交换两个变量的值。
展示使用临时变量和不使用临时变量（Python特有方式）两种方法。
'''

# 解决方案
def swap_with_temp(a, b):
    """
    使用临时变量交换两个变量的值
    
    参数:
        a: 第一个变量
        b: 第二个变量
    
    返回:
        tuple: 交换后的两个变量值
    """
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b):
    """
    不使用临时变量交换两个变量的值（Python特有方式）
    
    参数:
        a: 第一个变量
        b: 第二个变量
    
    返回:
        tuple: 交换后的两个变量值
    """
    a, b = b, a
    return a, b

# 示例输出
if __name__ == "__main__":
    # 初始值
    x = 5
    y = 10
    
    print(f"初始值: x = {x}, y = {y}")
    
    # 使用临时变量交换
    x_temp, y_temp = swap_with_temp(x, y)
    print(f"使用临时变量交换后: x = {x_temp}, y = {y_temp}")
    
    # 重置初始值
    x = 5
    y = 10
    
    # 不使用临时变量交换
    x_no_temp, y_no_temp = swap_without_temp(x, y)
    print(f"不使用临时变量交换后: x = {x_no_temp}, y = {y_no_temp}")