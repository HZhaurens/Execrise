'''
题目：找出列表中的最小值

描述：编写一个Python程序，找出列表中的最小值。使用多种方法实现。
'''

# 解决方案
def find_min_builtin(numbers):
    """
    使用内置函数找出列表中的最小值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最小值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    return min(numbers)

def find_min_loop(numbers):
    """
    使用循环比较找出列表中的最小值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最小值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    min_value = numbers[0]  # 假设第一个元素是最小值
    for num in numbers[1:]:  # 从第二个元素开始遍历
        if num < min_value:
            min_value = num  # 如果找到更小的值，则更新最小值
    
    return min_value

def find_min_sort(numbers):
    """
    使用排序方法找出列表中的最小值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最小值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    # 创建列表的副本并排序
    sorted_numbers = sorted(numbers)
    # 返回排序后列表的第一个元素（最小值）
    return sorted_numbers[0]

def find_min_reduce(numbers):
    """
    使用functools.reduce函数找出列表中的最小值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最小值，如果列表为空则返回None
    """
    from functools import reduce
    
    if not numbers:  # 检查列表是否为空
        return None
    
    # 使用reduce函数和lambda表达式比较两个数的大小
    return reduce(lambda x, y: x if x < y else y, numbers)

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [42, 17, 8, 94, 23, 61, 12, 59, 7]
    empty_list = []
    
    print(f"列表: {numbers}")
    
    # 使用内置函数方法
    min_builtin = find_min_builtin(numbers)
    print(f"\n使用内置函数方法找到的最小值: {min_builtin}")
    
    # 使用循环比较方法
    min_loop = find_min_loop(numbers)
    print(f"使用循环比较方法找到的最小值: {min_loop}")
    
    # 使用排序方法
    min_sort = find_min_sort(numbers)
    print(f"使用排序方法找到的最小值: {min_sort}")
    
    # 使用reduce方法
    min_reduce = find_min_reduce(numbers)
    print(f"使用reduce方法找到的最小值: {min_reduce}")
    
    # 测试空列表
    print(f"\n空列表测试:")
    print(f"内置函数方法: {find_min_builtin(empty_list)}")
    print(f"循环比较方法: {find_min_loop(empty_list)}")
    print(f"排序方法: {find_min_sort(empty_list)}")
    print(f"reduce方法: {find_min_reduce(empty_list)}")