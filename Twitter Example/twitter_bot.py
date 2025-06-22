#!/usr/bin/env python3
"""
Twitter Bot Script using Tweepy
This script provides functionality to post tweets with text and images using Twitter API v2
"""

import tweepy
import os
from datetime import datetime

class TwitterBot:
    def __init__(self):
        """Initialize the Twitter bot with API credentials"""
        # Twitter API credentials
        self.API_KEY = ''
        self.API_KEY_SECRET = ''
        self.ACCESS_TOKEN = ''
        self.ACCESS_TOKEN_SECRET = ''
        self.BEARER_TOKEN = ''
        
        # Initialize API clients
        self._setup_clients()
    
    def _setup_clients(self):
        """Set up both API v1.1 and v2 clients"""
        try:
            # OAuth 1.0a for API v1.1 (needed for media upload)
            auth = tweepy.OAuth1UserHandler(
                self.API_KEY, 
                self.API_KEY_SECRET, 
                self.ACCESS_TOKEN, 
                self.ACCESS_TOKEN_SECRET
            )
            self.api_v1 = tweepy.API(auth)
            
            # OAuth 2.0 Bearer Token for API v2 (for posting tweets)
            self.client = tweepy.Client(
                bearer_token=self.BEARER_TOKEN,
                consumer_key=self.API_KEY,
                consumer_secret=self.API_KEY_SECRET,
                access_token=self.ACCESS_TOKEN,
                access_token_secret=self.ACCESS_TOKEN_SECRET
            )
            
            print("✅ Twitter API clients initialized successfully!")
            
        except Exception as e:
            print(f"❌ Error initializing Twitter API clients: {e}")
            raise
    
    def test_authentication(self):
        """Test if the authentication is working"""
        try:
            # Test API v2 authentication
            me = self.client.get_me()
            print(f"✅ Authentication successful!")
            print(f"📱 Connected as: @{me.data.username}")
            print(f"👤 Display name: {me.data.name}")
            return True
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def post_text_tweet(self, text):
        """Post a text-only tweet"""
        try:
            if len(text) > 280:
                print(f"⚠️  Warning: Tweet is {len(text)} characters (max 280)")
                text = text[:277] + "..."
            
            response = self.client.create_tweet(text=text)
            tweet_id = response.data['id']
            
            print(f"✅ Tweet posted successfully!")
            print(f"🔗 Tweet ID: {tweet_id}")
            print(f"📝 Content: {text}")
            print(f"🌐 URL: https://twitter.com/i/web/status/{tweet_id}")
            
            return response
            
        except Exception as e:
            print(f"❌ Error posting tweet: {e}")
            return None
    
    def post_tweet_with_image(self, text, image_path):
        """Post a tweet with an image"""
        try:
            # Check if image file exists
            if not os.path.exists(image_path):
                print(f"❌ Image file not found: {image_path}")
                return None
            
            # Upload the image using API v1.1
            print(f"📤 Uploading image: {image_path}")
            media = self.api_v1.media_upload(image_path)
            media_id = media.media_id
            
            # Post tweet with image using API v2
            if len(text) > 280:
                print(f"⚠️  Warning: Tweet is {len(text)} characters (max 280)")
                text = text[:277] + "..."
            
            response = self.client.create_tweet(text=text, media_ids=[media_id])
            tweet_id = response.data['id']
            
            print(f"✅ Tweet with image posted successfully!")
            print(f"🔗 Tweet ID: {tweet_id}")
            print(f"📝 Content: {text}")
            print(f"🖼️  Image: {image_path}")
            print(f"🌐 URL: https://twitter.com/i/web/status/{tweet_id}")
            
            return response
            
        except Exception as e:
            print(f"❌ Error posting tweet with image: {e}")
            return None
    
    def post_tweet_with_multiple_images(self, text, image_paths):
        """Post a tweet with multiple images (up to 4)"""
        try:
            if len(image_paths) > 4:
                print("⚠️  Warning: Twitter allows maximum 4 images per tweet")
                image_paths = image_paths[:4]
            
            media_ids = []
            
            # Upload all images
            for image_path in image_paths:
                if not os.path.exists(image_path):
                    print(f"❌ Image file not found: {image_path}")
                    continue
                
                print(f"📤 Uploading image: {image_path}")
                media = self.api_v1.media_upload(image_path)
                media_ids.append(media.media_id)
            
            if not media_ids:
                print("❌ No valid images to upload")
                return None
            
            # Post tweet with images
            if len(text) > 280:
                print(f"⚠️  Warning: Tweet is {len(text)} characters (max 280)")
                text = text[:277] + "..."
            
            response = self.client.create_tweet(text=text, media_ids=media_ids)
            tweet_id = response.data['id']
            
            print(f"✅ Tweet with {len(media_ids)} images posted successfully!")
            print(f"🔗 Tweet ID: {tweet_id}")
            print(f"📝 Content: {text}")
            print(f"🖼️  Images: {', '.join(image_paths[:len(media_ids)])}")
            print(f"🌐 URL: https://twitter.com/i/web/status/{tweet_id}")
            
            return response
            
        except Exception as e:
            print(f"❌ Error posting tweet with multiple images: {e}")
            return None


def main():
    """Main function to demonstrate the Twitter bot functionality"""
    print("🐦 Twitter Bot Starting...")
    print("=" * 50)
    
    # Initialize the bot
    bot = TwitterBot()
    
    # Test authentication
    if not bot.test_authentication():
        print("❌ Authentication failed. Please check your credentials.")
        return
    
    print("\n" + "=" * 50)
    print("🚀 Bot is ready! You can now use the following methods:")
    print("   • bot.post_text_tweet('Your message here')")
    print("   • bot.post_tweet_with_image('Your message', 'path/to/image.jpg')")
    print("   • bot.post_tweet_with_multiple_images('Your message', ['img1.jpg', 'img2.jpg'])")
    print("=" * 50)
    
    return bot


if __name__ == "__main__":
    bot = main()