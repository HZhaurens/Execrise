'''
题目：统计字符串中某个字符出现的次数

描述：编写一个Python程序，接收用户输入的字符串和一个字符，统计该字符在字符串中出现的次数。
'''

# 解决方案
def count_character(string, char):
    """
    统计字符在字符串中出现的次数
    
    参数:
        string (str): 需要检查的字符串
        char (str): 需要统计的字符
    
    返回:
        int: 字符在字符串中出现的次数
    """
    # 方法一：使用循环
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def count_character_builtin(string, char):
    """
    使用内置方法统计字符在字符串中出现的次数
    
    参数:
        string (str): 需要检查的字符串
        char (str): 需要统计的字符
    
    返回:
        int: 字符在字符串中出现的次数
    """
    # 方法二：使用内置的count方法
    return string.count(char)

# 示例输出
if __name__ == "__main__":
    # 从用户获取输入
    input_string = input("请输入一个字符串: ")
    input_char = input("请输入要统计的字符: ")
    
    # 检查输入的字符长度
    if len(input_char) != 1:
        print("请输入单个字符!")
    else:
        # 使用循环方法统计
        count = count_character(input_string, input_char)
        print(f"使用循环方法统计: 字符 '{input_char}' 在字符串中出现了 {count} 次")
        
        # 使用内置方法统计
        count_builtin = count_character_builtin(input_string, input_char)
        print(f"使用内置方法统计: 字符 '{input_char}' 在字符串中出现了 {count_builtin} 次")
        
        # 区分大小写的说明
        if input_char.isalpha():
            print("\n注意: 统计区分大小写")
            # 转换为小写再统计
            count_lower = count_character(input_string.lower(), input_char.lower())
            print(f"不区分大小写统计: 字符 '{input_char.lower()}' 在字符串中出现了 {count_lower} 次")