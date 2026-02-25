import requests
import os

def send_pushplus_message(token, title, content):
    """
    发送PushPlus消息到微信
    
    Args:
        token (str): PushPlus的token
        title (str): 消息标题
        content (str): 消息内容
    """
    url = "http://www.pushplus.plus/send"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "token": token,
        "title": title,
        "content": content,
        "template": "txt"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == 200:
            print(f"✅ {title} 推送成功")
        else:
            print(f"❌ {title} 推送失败: {result.get('msg', '未知错误')}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 推送请求异常: {e}")
    except Exception as e:
        print(f"❌ 推送过程中发生未知错误: {e}")
