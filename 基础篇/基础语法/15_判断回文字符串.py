'''
题目：判断字符串是否为回文

描述：编写一个Python程序，判断用户输入的字符串是否为回文。
回文是指正着读和倒着读都一样的字符串，例如 "radar" 或 "level"。
'''

# 解决方案
def is_palindrome(string):
    """
    判断字符串是否为回文
    
    参数:
        string (str): 需要判断的字符串
    
    返回:
        bool: 如果是回文返回True，否则返回False
    """
    # 将字符串转换为小写并移除所有空格
    # 这样可以判断像 "A man a plan a canal Panama" 这样的回文句子
    cleaned_string = "".join(string.lower().split())
    
    # 方法一：使用切片反转字符串并比较
    return cleaned_string == cleaned_string[::-1]

def is_palindrome_two_pointer(string):
    """
    使用双指针方法判断字符串是否为回文
    
    参数:
        string (str): 需要判断的字符串
    
    返回:
        bool: 如果是回文返回True，否则返回False
    """
    # 将字符串转换为小写并移除所有空格
    cleaned_string = "".join(string.lower().split())
    
    # 方法二：使用双指针
    left, right = 0, len(cleaned_string) - 1
    
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    
    return True

# 示例输出
if __name__ == "__main__":
    # 从用户获取输入
    input_string = input("请输入一个字符串: ")
    
    # 使用切片方法判断
    if is_palindrome(input_string):
        print(f"'{input_string}' 是回文")
    else:
        print(f"'{input_string}' 不是回文")
    
    # 使用双指针方法判断
    if is_palindrome_two_pointer(input_string):
        print(f"使用双指针方法判断: '{input_string}' 是回文")
    else:
        print(f"使用双指针方法判断: '{input_string}' 不是回文")
    
    # 一些回文示例
    print("\n回文示例:")
    examples = ["radar", "level", "A man a plan a canal Panama", "race car", "hello"]
    for example in examples:
        if is_palindrome(example):
            print(f"'{example}' 是回文")
        else:
            print(f"'{example}' 不是回文")