# 42_计算最大公约数.py

def gcd(a, b):
    """计算两个数的最大公约数
    
    使用欧几里得算法（辗转相除法）
    
    Args:
        a: 第一个整数
        b: 第二个整数
        
    Returns:
        a和b的最大公约数
    """
    # 确保a和b为正整数
    a, b = abs(a), abs(b)
    
    # 欧几里得算法
    while b:
        a, b = b, a % b
    
    return a

# 测试
try:
    num1 = int(input("请输入第一个整数: "))
    num2 = int(input("请输入第二个整数: "))
    
    result = gcd(num1, num2)
    print(f"{num1}和{num2}的最大公约数是: {result}")
    
    # 计算最小公倍数
    lcm = abs(num1 * num2) // result
    print(f"{num1}和{num2}的最小公倍数是: {lcm}")
except ValueError:
    print("请输入有效的整数!")