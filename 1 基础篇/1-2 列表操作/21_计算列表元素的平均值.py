'''
题目：计算列表元素的平均值

描述：编写一个Python程序，计算列表中所有元素的平均值。使用多种方法实现。
'''

# 解决方案
def calculate_average_loop(numbers):
    """
    使用循环计算列表元素的平均值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        float: 列表元素的平均值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    return total / count

def calculate_average_builtin(numbers):
    """
    使用内置函数计算列表元素的平均值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        float: 列表元素的平均值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    return sum(numbers) / len(numbers)

def calculate_average_numpy(numbers):
    """
    使用NumPy库计算列表元素的平均值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        float: 列表元素的平均值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    try:
        import numpy as np
        return np.mean(numbers)
    except ImportError:
        # 如果NumPy库不可用，则使用内置函数方法
        return sum(numbers) / len(numbers)

def calculate_average_statistics(numbers):
    """
    使用statistics库计算列表元素的平均值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        float: 列表元素的平均值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    try:
        import statistics
        return statistics.mean(numbers)
    except ImportError:
        # 如果statistics库不可用，则使用内置函数方法
        return sum(numbers) / len(numbers)

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [10, 20, 30, 40, 50]
    empty_list = []
    
    print(f"列表: {numbers}")
    
    # 使用循环方法
    avg_loop = calculate_average_loop(numbers)
    print(f"\n使用循环方法计算的平均值: {avg_loop}")
    
    # 使用内置函数方法
    avg_builtin = calculate_average_builtin(numbers)
    print(f"使用内置函数方法计算的平均值: {avg_builtin}")
    
    # 使用NumPy库方法
    avg_numpy = calculate_average_numpy(numbers)
    print(f"使用NumPy库方法计算的平均值: {avg_numpy}")
    
    # 使用statistics库方法
    avg_statistics = calculate_average_statistics(numbers)
    print(f"使用statistics库方法计算的平均值: {avg_statistics}")
    
    # 测试空列表
    print(f"\n空列表测试:")
    print(f"循环方法: {calculate_average_loop(empty_list)}")
    print(f"内置函数方法: {calculate_average_builtin(empty_list)}")
    print(f"NumPy库方法: {calculate_average_numpy(empty_list)}")
    print(f"statistics库方法: {calculate_average_statistics(empty_list)}")