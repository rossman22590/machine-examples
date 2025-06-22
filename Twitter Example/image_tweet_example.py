#!/usr/bin/env python3
"""
Twitter Bot Example - Tweets with Images
This script demonstrates how to post tweets with images using the TwitterBot class
"""

from twitter_bot import TwitterBot
import os

def main():
    """Example of posting tweets with images"""
    print("🐦 Image Tweet Example")
    print("=" * 40)
    
    # Initialize the bot
    bot = TwitterBot()
    
    # Test authentication first
    if not bot.test_authentication():
        print("❌ Authentication failed. Exiting.")
        return
    
    print("\n🖼️ Posting example tweets with images...")
    
    # Example 1: Single image tweet
    image1_path = "sample_images/sunset_mountains.png"
    if os.path.exists(image1_path):
        tweet1 = "Beautiful sunset over the mountains! Nature never fails to amaze me with its stunning colors and peaceful vibes."
        print(f"\n1️⃣ Posting with image: {tweet1}")
        response1 = bot.post_tweet_with_image(tweet1, image1_path)
    else:
        print(f"❌ Image not found: {image1_path}")
    
    # Example 2: Another single image tweet
    image2_path = "sample_images/robot_mascot.png"
    if os.path.exists(image2_path):
        tweet2 = "Meet our friendly mascot! This little guy represents the fun side of technology and innovation."
        print(f"\n2️⃣ Posting with image: {tweet2}")
        response2 = bot.post_tweet_with_image(tweet2, image2_path)
    else:
        print(f"❌ Image not found: {image2_path}")
    
    # Example 3: Multiple images tweet
    image_paths = [
        "sample_images/sunset_mountains.png",
        "sample_images/robot_mascot.png",
        "sample_images/python_code.png"
    ]
    
    # Filter out non-existent images
    valid_images = [path for path in image_paths if os.path.exists(path)]
    
    if valid_images:
        tweet3 = "Here's a collection of some amazing visuals! From nature's beauty to tech innovation - diversity makes life interesting."
        print(f"\n3️⃣ Posting with multiple images: {tweet3}")
        response3 = bot.post_tweet_with_multiple_images(tweet3, valid_images)
    else:
        print("❌ No valid images found for multiple image tweet")
    
    # Example 4: Programming-related tweet
    image3_path = "sample_images/python_code.png"
    if os.path.exists(image3_path):
        tweet4 = "Clean code is like a well-written book - easy to read, understand, and maintain. Every developer should strive for clarity."
        print(f"\n4️⃣ Posting with image: {tweet4}")
        response4 = bot.post_tweet_with_image(tweet4, image3_path)
    else:
        print(f"❌ Image not found: {image3_path}")
    
    print("\n✅ All example image tweets posted successfully!")
    print("Check your Twitter account to see the results.")

if __name__ == "__main__":
    main()