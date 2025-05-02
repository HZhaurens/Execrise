'''
题目：找出列表中的最大值

描述：编写一个Python程序，找出列表中的最大值。使用多种方法实现。
'''

# 解决方案
def find_max_builtin(numbers):
    """
    使用内置函数找出列表中的最大值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最大值
    """
    if not numbers:  # 检查列表是否为空
        return None
    return max(numbers)

def find_max_loop(numbers):
    """
    使用循环比较找出列表中的最大值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最大值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    max_value = numbers[0]  # 假设第一个元素是最大值
    for num in numbers[1:]:  # 从第二个元素开始遍历
        if num > max_value:
            max_value = num  # 如果找到更大的值，则更新最大值
    
    return max_value

def find_max_sort(numbers):
    """
    使用排序方法找出列表中的最大值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最大值，如果列表为空则返回None
    """
    if not numbers:  # 检查列表是否为空
        return None
    
    # 创建列表的副本并排序
    sorted_numbers = sorted(numbers)
    # 返回排序后列表的最后一个元素（最大值）
    return sorted_numbers[-1]

def find_max_reduce(numbers):
    """
    使用functools.reduce函数找出列表中的最大值
    
    参数:
        numbers (list): 包含数字的列表
    
    返回:
        number: 列表中的最大值，如果列表为空则返回None
    """
    from functools import reduce
    
    if not numbers:  # 检查列表是否为空
        return None
    
    # 使用reduce函数和lambda表达式比较两个数的大小
    return reduce(lambda x, y: x if x > y else y, numbers)

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [42, 17, 8, 94, 23, 61, 12, 59, 7]
    empty_list = []
    
    print(f"列表: {numbers}")
    
    # 使用内置函数方法
    max_builtin = find_max_builtin(numbers)
    print(f"\n使用内置函数方法找到的最大值: {max_builtin}")
    
    # 使用循环比较方法
    max_loop = find_max_loop(numbers)
    print(f"使用循环比较方法找到的最大值: {max_loop}")
    
    # 使用排序方法
    max_sort = find_max_sort(numbers)
    print(f"使用排序方法找到的最大值: {max_sort}")
    
    # 使用reduce方法
    max_reduce = find_max_reduce(numbers)
    print(f"使用reduce方法找到的最大值: {max_reduce}")
    
    # 测试空列表
    print(f"\n空列表测试:")
    print(f"内置函数方法: {find_max_builtin(empty_list)}")
    print(f"循环比较方法: {find_max_loop(empty_list)}")
    print(f"排序方法: {find_max_sort(empty_list)}")
    print(f"reduce方法: {find_max_reduce(empty_list)}")