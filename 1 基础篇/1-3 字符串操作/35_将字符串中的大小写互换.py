# 35_将字符串中的大小写互换.py

def swap_case(string):
    """将字符串中的大小写互换
    
    Args:
        string: 输入的字符串
        
    Returns:
        处理后的字符串
    """
    return string.swapcase()

# 测试
text = input("请输入一个包含大小写字母的字符串: ")
result = swap_case(text)
print(f"处理后的结果: {result}")