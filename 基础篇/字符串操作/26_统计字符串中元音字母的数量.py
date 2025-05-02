# 26_统计字符串中元音字母的数量.py

def count_vowels(string):
    """统计字符串中元音字母的数量
    
    Args:
        string: 输入的字符串
        
    Returns:
        元音字母的数量
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# 测试
text = input("请输入一个字符串: ")
result = count_vowels(text)
print(f"元音字母的数量: {result}")