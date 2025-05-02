'''
题目：反转字符串

描述：编写一个Python程序，接收用户输入的字符串，并将其反转后输出。
'''

# 解决方案
def reverse_string_slice(string):
    """
    使用切片操作反转字符串
    
    参数:
        string (str): 需要反转的字符串
    
    返回:
        str: 反转后的字符串
    """
    return string[::-1]

def reverse_string_loop(string):
    """
    使用循环反转字符串
    
    参数:
        string (str): 需要反转的字符串
    
    返回:
        str: 反转后的字符串
    """
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_recursion(string):
    """
    使用递归反转字符串
    
    参数:
        string (str): 需要反转的字符串
    
    返回:
        str: 反转后的字符串
    """
    # 基本情况：空字符串或只有一个字符
    if len(string) <= 1:
        return string
    
    # 递归情况：第一个字符放到最后，递归处理剩余部分
    return reverse_string_recursion(string[1:]) + string[0]

# 示例输出
if __name__ == "__main__":
    # 从用户获取输入
    input_string = input("请输入一个字符串: ")
    
    # 使用切片方法反转
    reversed_slice = reverse_string_slice(input_string)
    print(f"使用切片反转: {reversed_slice}")
    
    # 使用循环方法反转
    reversed_loop = reverse_string_loop(input_string)
    print(f"使用循环反转: {reversed_loop}")
    
    # 使用递归方法反转
    reversed_recursion = reverse_string_recursion(input_string)
    print(f"使用递归反转: {reversed_recursion}")