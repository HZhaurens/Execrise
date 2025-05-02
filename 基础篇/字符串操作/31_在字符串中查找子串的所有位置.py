# 31_在字符串中查找子串的所有位置.py

def find_all_occurrences(string, substring):
    """在字符串中查找子串的所有位置
    
    Args:
        string: 输入的字符串
        substring: 要查找的子串
        
    Returns:
        包含所有匹配位置的列表
    """
    positions = []
    pos = string.find(substring)
    
    while pos != -1:
        positions.append(pos)
        # 从找到的位置之后继续查找
        pos = string.find(substring, pos + 1)
    
    return positions

# 测试
text = input("请输入一个字符串: ")
sub = input("请输入要查找的子串: ")
result = find_all_occurrences(text, sub)

if result:
    print(f"子串'{sub}'在字符串中的位置: {result}")
else:
    print(f"未找到子串'{sub}'")