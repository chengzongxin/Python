from datetime import datetime
import os

# current_time = datetime.now()
# formatted_time = current_time.strftime("%Y-%m-%d-%H-%M-%S")
# file_name = f'./send_record/record_{formatted_time}.txt'
# # 创建目录（如果不存在）
# os.makedirs(os.path.dirname(file_name), exist_ok=True)
# # 将内容写入文件
# with open(file_name, "w", encoding="utf-8") as file:
#     file.write("letter")

# print(f"内容已成功写入文件：{file_name}")


# 从环境变量中读取值
openai_base_url = os.getenv('OPENAI_BASE_URL')
openai_api_key = os.getenv('OPENAI_API_KEY')

# 打印读取的值
print(f"OPENAI_BASE_URL: {openai_base_url}")
print(f"OPENAI_API_KEY: {openai_api_key}")