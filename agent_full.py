# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
import time
import random
import hmac
import hashlib
base64
from openai import OpenAI

# ============================
# 配置区（你已经全部填好啦）
# ============================
APP_KEY = "69-18-35-35-88"
APP_SECRET = "TW152bmbMs09YRHfuEuKyC3K86dpv1Ys"
CIRCLE_ID = "2001009660925334090"

KIMI_API_KEY = "sk-vnbuuPI5AEh13PmTSip2P1i3C0rURRa9WW0ekKZRChNJJSwh"
KIMI_BASE_URL = "https://api.moonshot.cn/v1"

# ============================
# 🔥 你唯一的核心人设（超棒）
# ============================
AI_PERSONA = """
你是一位心思细腻、三观端正、通透清醒的故事洞察解读创作者。
说话直爽不拐弯，逻辑条理极强，坚决反恋爱脑、不圣母、不纵容拎不清的扭曲三观；
擅长捕捉故事里的细微伏笔、人性细节与逻辑漏洞，点评一针见血、理性克制。
自带温润深沉的人文情怀，体恤人间百态与普通人的无奈与苦衷，观点犀利但不刻薄，通透却不冷漠；
保有理性判事的清醒底线，又藏温柔共情的内心底色。
同时想象力丰富、脑洞开阔，能跳出常规剧情视角，做另类解读、反向剖析、平行结局与创意构想。
输出贴合知乎生活化口吻，不矫情、不灌廉价鸡汤，观点利落有棱角、有温度、有辨识度，
兼具理性深度、逻辑洞察、创意脑洞与人文温情。
"""

# ============================
# 👇 下面是 4 大智能功能
# ============================

# 1. 故事深度解读（核心功能）
def analyze_story(story_content):
    client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
    prompt = f"""
{AI_PERSONA}
请你对这篇故事做深度洞察解读：分析人物、伏笔、三观、逻辑，风格保持清醒通透。
故事内容：
{story_content}
"""
    try:
        res = client.chat.completions.create(model="moonshot-v1-8k", messages=[{"role":"user","content":prompt}])
        return res.choices[0].message.content
    except:
        return "分析失败"

# 2. 温柔回复评论（互动功能）
def reply_comment(comment_content):
    client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
    prompt = f"""
{AI_PERSONA}
用户评论：{comment_content}
请你温和、真诚、有温度地回复，保持你的通透与共情，不要尖锐。
"""
    try:
        res = client.chat.completions.create(model="moonshot-v1-8k", messages=[{"role":"user","content":prompt}])
        return res.choices[0].message.content
    except:
        return "回复失败"

# 3. 创意脑洞改写（创作功能）
def rewrite_story(story_snippet):
    client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
    prompt = f"""
{AI_PERSONA}
请你用创意脑洞，把这段故事片段改写得更有张力、更有反转感，保持知乎风格。
原文：
{story_snippet}
"""
    try:
        res = client.chat.completions.create(model="moonshot-v1-8k", messages=[{"role":"user","content":prompt}])
        return res.choices[0].message.content
    except:
        return "改写失败"

# 4. 聊天问答（智能助理）
def chat_answer(question):
    client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
    prompt = f"""
{AI_PERSONA}
用户问题：{question}
请你理性、通透、温柔地回答。
"""
    try:
        res = client.chat.completions.create(model="moonshot-v1-8k", messages=[{"role":"user","content":prompt}])
        return res.choices[0].message.content
    except:
        return "回答失败"

# ============================
# 知乎工具函数（不变）
# ============================
def get_timestamp(): return str(int(time.time()))
def get_log_id(): return str(random.randint(10000000000000000000, 99999999999999999999))
def generate_sign(timestamp, log_id):
    sign_str = f"APP_KEY={APP_KEY}&TIMESTAMP={timestamp}&LOG_ID={log_id}"
    hmac_obj = hmac.new(APP_SECRET.encode(), sign_str.encode(), hashlib.sha256)
    return base64.b64encode(hmac_obj.digest()).decode()

def get_zhihu_story_list():
    try:
        headers = {"X-App-Key":APP_KEY,"X-Timestamp":get_timestamp(),"X-Log-Id":get_log_id(),"X-Sign":generate_sign(get_timestamp(),get_log_id())}
        resp = requests.get("https://www.zhihu.com/ring/molibook/api/community/story_list", headers=headers, timeout=15)
        return resp.json()
    except:
        return {}

def post_idea(content):
    try:
        headers = {"X-App-Key":APP_KEY,"X-Timestamp":get_timestamp(),"X-Log-Id":get_log_id(),"X-Sign":generate_sign(get_timestamp(),get_log_id()),"Content-Type":"application/json"}
        data = {"circle_id":CIRCLE_ID,"content":content}
        resp = requests.post("https://api.zhihu.com/openclaw/post_idea", headers=headers, json=data, timeout=10)
        return resp.json()
    except:
        return {}

# ============================
# 测试：一键跑通所有功能
# ============================
if __name__ == "__main__":
    print("✅ 你的超级Agent已启动：单一人设 × 4大智能功能")
    
    # 测试1：故事解读
    print("\n【功能1：故事深度解读】")
    test_story = "我和男友在一起三年，他总说忙，却在朋友圈给别的女生点赞。"
    print(analyze_story(test_story))

    # 测试2：回复评论
    print("\n【功能2：温柔回复评论】")
    print(reply_comment("你说得好有道理，我突然清醒了！"))

    # 测试3：创意改写
    print("\n【功能3：创意脑洞改写】")
    print(rewrite_story("他推开家门，身上带着陌生的香水味。"))

    # 测试4：聊天问答
    print("\n【功能4：智能聊天问答】")
    print(chat_answer("为什么恋爱中不要过度付出？"))