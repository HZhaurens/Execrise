# 36_计算幂函数.py

def power(base, exponent):
    """计算幂函数
    
    Args:
        base: 底数
        exponent: 指数
        
    Returns:
        计算结果
    """
    return base ** exponent

# 测试
base = float(input("请输入底数: "))
exponent = float(input("请输入指数: "))
result = power(base, exponent)
print(f"{base}的{exponent}次方等于: {result}")