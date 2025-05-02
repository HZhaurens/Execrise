# 37_检查闰年.py

def is_leap_year(year):
    """检查是否为闰年
    
    闰年规则：
    1. 能被4整除但不能被100整除
    2. 能被400整除
    
    Args:
        year: 年份
        
    Returns:
        布尔值，True表示是闰年，False表示不是闰年
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 测试
year = int(input("请输入年份: "))
if is_leap_year(year):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")