#!/usr/bin/env python3
"""
Simple Twitter Bot Example - Text Only Tweets
This script demonstrates how to post simple text tweets using the TwitterBot class
"""

from twitter_bot import TwitterBot
from datetime import datetime

def main():
    """Example of posting text-only tweets"""
    print("🐦 Simple Tweet Example")
    print("=" * 40)
    
    # Initialize the bot
    bot = TwitterBot()
    
    # Test authentication first
    if not bot.test_authentication():
        print("❌ Authentication failed. Exiting.")
        return
    
    print("\n📝 Posting example tweets...")
    
    # Example 1: Simple greeting
    tweet1 = "Hello Twitter! 👋 This is a test tweet from my Python bot using Tweepy! #Python #TwitterBot"
    print(f"\n1️⃣ Posting: {tweet1}")
    response1 = bot.post_text_tweet(tweet1)
    
    # Example 2: Tweet with current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tweet2 = f"🤖 Bot is active at {current_time}! Automated posting works perfectly. #Automation"
    print(f"\n2️⃣ Posting: {tweet2}")
    response2 = bot.post_text_tweet(tweet2)
    
    # Example 3: Motivational quote
    tweet3 = "💡 'The best time to plant a tree was 20 years ago. The second best time is now.' - Chinese Proverb #Motivation #Wisdom"
    print(f"\n3️⃣ Posting: {tweet3}")
    response3 = bot.post_text_tweet(tweet3)
    
    print("\n✅ All example tweets posted successfully!")
    print("Check your Twitter account to see the results.")

if __name__ == "__main__":
    main()