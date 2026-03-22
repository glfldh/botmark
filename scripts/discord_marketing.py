#!/usr/bin/env python3
"""
BotMark Discord Marketing Automation
自动发送营销内容到 Discord 服务器

Usage:
  export DISCORD_BOT_TOKEN="your-token"
  export DISCORD_CHANNEL_ID="your-channel-id"
  python discord_marketing.py
"""

import requests
import os
import sys

# Configuration from environment
BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.environ.get('DISCORD_CHANNEL_ID')
BASE_URL = "https://discord.com/api/v10"

# Marketing content templates
CONTENT_TEMPLATES = {
    "morning": {
        "content": """🌅 Good morning, benchmarkers! 

📊 **Today's Challenge**: Test your agent's **EQ** (Emotional Intelligence)

What's your bot's MBTI type? Share your results! 👇

👉 Start testing: https://botmark.cc"""
    },
    "leaderboard": {
        "content": """🏆 **Live Leaderboard Update**

Top 3 Agents This Week:
🥇 GPT-4 - 916 pts
🥈 Claude - 920 pts  
🥉 Kimi - 760 pts

Think your bot can beat them?
👉 https://botmark.cc/leaderboard"""
    },
    "insight": {
        "content": """💡 **Daily AI Insight**

Did you know?
Agents scoring high on **SQ** (Self-Evolution) improve 23% faster on user tasks.

Test your agent's learning capability:
👉 https://botmark.cc

#AIFacts #Benchmark"""
    },
    "question": {
        "content": """🤔 **Question of the Day**

What's more important for your use case:
• High **IQ** (reasoning/coding)?
• High **EQ** (empathy/personality)?
• Balanced across all **5 dimensions**?

Share your thoughts! 💬"""
    },
    "weekly": {
        "content": """📊 **BotMark Weekly Report**

🎯 **Highlights:**
• 50+ new agents tested this week
• Average IQ score: 85%
• Average EQ score: 68%
• Most tested dimension: IQ

🏆 **Top Movers:**
1. GPT-4 ↑ 12 points
2. Claude ↑ 8 points
3. Kimi ↑ 15 points

📈 **Trend**: More developers testing TQ (Tool Intelligence)

Ready to test your agent?
👉 https://botmark.cc"""
    }
}

def send_message(channel_id, content):
    """Send message to Discord channel"""
    url = f"{BASE_URL}/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"content": content}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"✅ Message sent successfully")
        return True
    else:
        print(f"❌ Failed to send message: {response.status_code}")
        print(response.text)
        return False

def main():
    """Main marketing automation"""
    if not BOT_TOKEN or not CHANNEL_ID:
        print("❌ Error: Set DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID environment variables")
        sys.exit(1)
    
    print("🚀 BotMark Discord Marketing Automation")
    print("=" * 50)
    
    # Get message type from argument or default to morning
    msg_type = sys.argv[1] if len(sys.argv) > 1 else "morning"
    
    if msg_type not in CONTENT_TEMPLATES:
        print(f"❌ Unknown message type: {msg_type}")
        print(f"Available types: {', '.join(CONTENT_TEMPLATES.keys())}")
        sys.exit(1)
    
    content = CONTENT_TEMPLATES[msg_type]["content"]
    
    print(f"\n📤 Sending '{msg_type}' message to channel {CHANNEL_ID}...")
    
    if send_message(CHANNEL_ID, content):
        print("\n✅ Done!")
    else:
        print("\n❌ Failed to send message")
        sys.exit(1)

if __name__ == "__main__":
    main()
