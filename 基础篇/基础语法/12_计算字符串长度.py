'''
题目：计算字符串长度(不使用len())

描述：编写一个Python程序，计算用户输入的字符串的长度，但不使用内置的len()函数。
'''

# 解决方案
def calculate_string_length(string):
    """
    计算字符串的长度（不使用len()函数）
    
    参数:
        string (str): 需要计算长度的字符串
    
    返回:
        int: 字符串的长度
    """
    # 初始化计数器
    count = 0
    
    # 遍历字符串中的每个字符
    for _ in string:
        count += 1
    
    return count

def calculate_string_length_enumerate(string):
    """
    使用enumerate计算字符串的长度（不使用len()函数）
    
    参数:
        string (str): 需要计算长度的字符串
    
    返回:
        int: 字符串的长度
    """
    # 使用enumerate函数，获取最后一个字符的索引+1
    for i, _ in enumerate(string):
        pass
    
    # 如果字符串为空，enumerate不会执行，返回0
    # 否则返回最后一个索引+1
    return i + 1 if string else 0

# 示例输出
if __name__ == "__main__":
    # 从用户获取输入
    input_string = input("请输入一个字符串: ")
    
    # 计算并显示结果
    length = calculate_string_length(input_string)
    print(f"字符串 '{input_string}' 的长度是: {length}")
    
    # 使用enumerate方法计算
    length_enum = calculate_string_length_enumerate(input_string)
    print(f"使用enumerate方法计算的长度是: {length_enum}")
    
    # 与内置len()函数比较
    print(f"使用内置len()函数计算的长度是: {len(input_string)}")