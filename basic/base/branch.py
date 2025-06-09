"""
if-elif-else 分支
"""
def if_demo():
    # BMI计算器
    height = float(input('身高(cm)：'))
    weight = float(input('体重(kg)：'))
    bmi = weight / (height / 100) ** 2
    print(f'{bmi = :.1f}')
    if 18.5 <= bmi < 24:
        print('你的身材很棒！')
    elif bmi > 24:
        print(f'你的体重偏重，请务必注意健康！')
    else:
        print('太瘦了！')

# if_demo()

'''
match-case 语法实现
'''
def match_demo():
    status_code = int(input('响应状态码: '))
    match status_code:
        case 400:
            description = 'Bad Request'
        case 401:
            description = 'Unauthorized'
        case 403:
            description = 'Forbidden'
        case 404:
            description = 'Not Found'
        case 405:
            description = 'Method Not Allowed'
        case 418:
            description = 'I am a teapot'
        case 429:
            description = 'Too many requests'
        case _: # 匹配所有
            description = 'Unknown Status Code'
    print('状态码描述:', description)


# match_demo()

def if_demo2():
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print(f'{y = }')

if_demo2()