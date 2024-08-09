from openai import OpenAI
import time
from datetime import datetime

# 导入上层
import sys
import os

# 打印当前工作目录
print(os.getcwd())
# 获取上一层目录的路径
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 将上一层目录添加到 sys.path 中
sys.path.append(parent_dir)

# 现在可以导入 b.py
# import file_manager

# 调用 b 文件中的函数或变量
# file_manager.some_function()
import PyPDF2

import PyPDF2

def get_resume():
    # 打开并读取 PDF 文件
    with open(r'e:\python\start_find\test\resume.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    # 将文本存储到字符串变量
    return text


OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def generate_letter():
    job_desc = """
    岗位职责：
    1. 负责公司iOS应用程序的设计和开发以及对新技术的探索研究
    2. 负责APP架构设计和性能优化
    3. 对旧代码有一定的重构能力，确保软件质量和效率
    4. 协助测试工程师识别并修复发现的问题
    5. 配合团队进行app设计和规划，解决技术问题
    6. 能够独立负责一个项目的开发和维护（熟悉app store发布流程）
    7. 具有良好的表达和沟通能力，有较强的团队合作能力，较强的责任心

    任职要求：
    1. 本科及以上学历
    2. 熟练使用Objective-C或Swift（或两者都会）
    3. 至少有三年的iOS开发经验，有在App Store发布过应用的经验
    4. 对iOS SDK有深入的理解，包括UIKit，Core Data，Core Animation等
    5. 精通iOS的设计原则，模式和最佳实践
    6. 能够理解和执行代码优化，以改进应用程序的性能

    优先考虑：
    1.有导航APP或者物流行业APP开发经验优先；
    2. 有跨平台开发的经验，如React Native 、fluter、uniapp.
    """

    context = """
    您好，我叫程宗鑫，我对您发布的职位非常感兴趣，我有丰富的开发经验，尤其擅长iOS、前端、uni跨平台、微信小程序、鸿蒙等项目开发。也熟悉Flutter、iOS底层原理、逆向工程和后端技术。我热衷于钻研技术、分析和解决难题，特别是在团队增效技术方面有深入研究。曾在土巴兔公司工作，参与了多个大规模项目，使用了许多前沿技术，覆盖了市面上的大部分功能点。方便的话，我可以发简历给您看看。
    """
    
    question = """
    根据工作描述，寻找出简历里最合适的技能都有哪些?求职者的优势是什么?
    这是一份求职消息，
    不要过于客套、不要此致、敬礼等词语
    不要出现gpt相关词汇
    不要让别人以为是AI写的
    不要包含求职内容以外的东西,例如“根据您上传的求职要求和个人简历,我来帮您起草一封求职邮件：”这一类的内容，以便于我直接自动化复制粘贴发送。
    """
    
   # 字数限制
    character_limit = 200

    langchain_prompt_template = f"""
    你将扮演一位求职者的角色,根据上下文里的简历内容以及应聘工作的描述,来直接给HR写一个亲切、礼貌、专业且字数严格限制在{character_limit}以内的求职消息,
    要求能够用专业的语言结合简历中的经历和技能,并结合应聘工作的描述,来阐述自己的优势,尽最大可能打动招聘者。
    始终使用中文来进行消息的编写。

    工作描述
    {job_desc}

    简历内容:
    {context}

    要求:
    {question}
    """
    print('开始施法========================')

    client = OpenAI(api_key=OPENAI_API_KEY,base_url=OPENAI_BASE_URL)
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": langchain_prompt_template}],
        stream=True,
    )

    # print(stream)

    letter = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # print(chunk.choices[0].delta.content, end="")
            letter += chunk.choices[0].delta.content

    
    print('咒语生成========================')

    if len(letter) < 10:
        print("生成失败")
        

    # file_manager.write(langchain_prompt_template + "\n\n\n\n" + letter)
    print(letter)
    return letter


generate_letter()