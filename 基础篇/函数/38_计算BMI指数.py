# 38_计算BMI指数.py

def calculate_bmi(weight, height):
    """计算BMI指数
    
    BMI = 体重(kg) / (身高(m) * 身高(m))
    
    Args:
        weight: 体重，单位为千克
        height: 身高，单位为米
        
    Returns:
        BMI指数
    """
    bmi = weight / (height * height)
    return round(bmi, 2)  # 保留两位小数

def interpret_bmi(bmi):
    """解释BMI指数
    
    Args:
        bmi: BMI指数
        
    Returns:
        BMI指数的解释
    """
    if bmi < 18.5:
        return "体重过轻"
    elif 18.5 <= bmi < 24:
        return "正常范围"
    elif 24 <= bmi < 28:
        return "超重"
    else:
        return "肥胖"

# 测试
weight = float(input("请输入体重(千克): "))
height = float(input("请输入身高(米): "))
bmi = calculate_bmi(weight, height)
result = interpret_bmi(bmi)
print(f"您的BMI指数为: {bmi}")
print(f"健康状况: {result}")