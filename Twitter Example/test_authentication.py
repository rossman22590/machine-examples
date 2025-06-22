#!/usr/bin/env python3
"""
Twitter Bot Authentication Test
This script tests the Twitter API authentication without posting any tweets
"""

from twitter_bot import TwitterBot

def main():
    """Test Twitter API authentication"""
    print("🔐 Twitter API Authentication Test")
    print("=" * 45)
    
    try:
        # Initialize the bot
        print("🔄 Initializing Twitter Bot...")
        bot = TwitterBot()
        
        # Test authentication
        print("\n🔍 Testing authentication...")
        if bot.test_authentication():
            print("\n✅ SUCCESS: Authentication is working perfectly!")
            print("🚀 Your Twitter bot is ready to post tweets.")
            print("\nNext steps:")
            print("   • Run 'python simple_tweet_example.py' for text tweets")
            print("   • Run 'python image_tweet_example.py' for image tweets")
            print("   • Use the TwitterBot class in your own scripts")
        else:
            print("\n❌ FAILED: Authentication is not working.")
            print("Please check your API credentials in twitter_bot.py")
            
    except Exception as e:
        print(f"\n💥 ERROR: {e}")
        print("Please check your API credentials and internet connection.")

if __name__ == "__main__":
    main()