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
import file_manager

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
    【岗位职责】
    1.参与音视频类APP开发；
    2.负责IOS 客户端主要功能模块日常开发及维护；
    【任职要求】
    1.计算机及相关专业，本科及以上学历，热爱计算机科学和互联网技术；
    2.3年以上IOS应用开发经验,有完整的上线项目开发经验，具备独立开发App能力；
    3.熟练掌握Objective-C，Swift语言；
    4.对IOS的UI系统、动画效果、内存管理等有深入实践；
    5.熟悉常用开源框架的使用，了解过开源框架实现机制；
    7.具备良好的分析解决问题能力，能独立承担任务并控制开发进度；
    8.对音视频、流媒体知识，有一定了解；
    【加分项】
    1.音视频实战经验者优先；
    3.有性能调优实战经验者优先。
    """

    context = """
    您好，周女士，我叫程宗鑫，我对您发布的职位非常感兴趣，我有丰富的开发经验，尤其擅长iOS、前端、uni跨平台、微信小程序、鸿蒙等项目开发。也熟悉Flutter、iOS底层原理、逆向工程和后端技术。我热衷于钻研技术、分析和解决难题，特别是在团队增效技术方面有深入研究。曾在土巴兔公司工作，参与了多个大规模项目，使用了许多前沿技术，覆盖了市面上的大部分功能点。方便的话，我可以发简历给您看看。
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

    file_manager.write(langchain_prompt_template + "\n\n\n\n" + letter)

    return letter


generate_letter()