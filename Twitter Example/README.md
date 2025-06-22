# Twitter Bot with Python and Tweepy

A comprehensive Twitter bot implementation using Python and the Tweepy library for Twitter API v2. This bot can post text tweets, tweets with single images, and tweets with multiple images.

## 🚀 Features

- **Text Tweets**: Post simple text-only tweets
- **Single Image Tweets**: Post tweets with one image
- **Multiple Image Tweets**: Post tweets with up to 4 images
- **Authentication Testing**: Verify API credentials without posting
- **Error Handling**: Robust error handling and user feedback
- **Character Limit**: Automatic handling of Twitter's 280-character limit

## 📋 Prerequisites

- Python 3.6 or higher
- Twitter Developer Account with API credentials
- Tweepy library (automatically installed)

## 🔧 Installation

1. **Install Tweepy**:
   ```bash
   pip install tweepy
   ```

2. **Set up your credentials** in `twitter_bot.py`:
   - API Key
   - API Key Secret
   - Access Token
   - Access Token Secret
   - Bearer Token

## 📁 Project Structure

```
├── twitter_bot.py              # Main TwitterBot class
├── test_authentication.py      # Test API credentials
├── simple_tweet_example.py     # Text-only tweet examples
├── image_tweet_example.py      # Image tweet examples
├── sample_images/              # Sample images for testing
│   ├── sunset_mountains.png
│   ├── robot_mascot.png
│   └── python_code.png
└── README.md                   # This file
```

## 🎯 Quick Start

### 1. Test Authentication
First, verify your API credentials work:
```bash
python test_authentication.py
```

### 2. Post Text Tweets
Run the simple text tweet example:
```bash
python simple_tweet_example.py
```

### 3. Post Image Tweets
Run the image tweet example:
```bash
python image_tweet_example.py
```

## 💻 Usage Examples

### Basic Usage

```python
from twitter_bot import TwitterBot

# Initialize the bot
bot = TwitterBot()

# Test authentication
if bot.test_authentication():
    print("Ready to tweet!")
    
    # Post a text tweet
    bot.post_text_tweet("Hello Twitter! This is my first tweet from Python.")
    
    # Post a tweet with an image
    bot.post_tweet_with_image("Check out this amazing sunset!", "path/to/image.jpg")
    
    # Post a tweet with multiple images
    images = ["image1.jpg", "image2.jpg", "image3.jpg"]
    bot.post_tweet_with_multiple_images("Here are some great photos!", images)
```

### Advanced Usage

```python
from twitter_bot import TwitterBot
from datetime import datetime

bot = TwitterBot()

# Custom tweet with timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tweet_text = f"Good morning! Today is {current_time}"
response = bot.post_text_tweet(tweet_text)

if response:
    tweet_id = response.data['id']
    print(f"Tweet posted successfully! ID: {tweet_id}")
```

## 🔐 Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for production:
   ```python
   import os
   API_KEY = os.getenv('TWITTER_API_KEY')
   ```
3. **Rotate credentials** regularly
4. **Monitor API usage** to avoid rate limits

## 📊 API Rate Limits

Twitter API v2 has the following rate limits:
- **Tweet creation**: 300 tweets per 15-minute window
- **Media upload**: 300 uploads per 15-minute window
- **User lookup**: 300 requests per 15-minute window

## 🛠️ TwitterBot Class Methods

### `__init__()`
Initializes the bot with API credentials and sets up both API v1.1 and v2 clients.

### `test_authentication()`
Tests if the API credentials are valid and returns user information.

### `post_text_tweet(text)`
Posts a text-only tweet. Automatically truncates if over 280 characters.

### `post_tweet_with_image(text, image_path)`
Posts a tweet with a single image. Checks if the image file exists.

### `post_tweet_with_multiple_images(text, image_paths)`
Posts a tweet with multiple images (up to 4). Filters out non-existent images.

## 🎨 Sample Images

The project includes sample images for testing:
- `sunset_mountains.png` - Beautiful landscape
- `robot_mascot.png` - Friendly robot character
- `python_code.png` - Programming screenshot

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify all API credentials are correct
   - Check if your Twitter Developer account is approved
   - Ensure your app has read and write permissions

2. **Image Upload Failed**
   - Check if the image file exists
   - Verify the image format is supported (PNG, JPG, GIF, WEBP)
   - Ensure the image size is under 5MB

3. **Rate Limit Exceeded**
   - Wait for the rate limit window to reset
   - Implement delays between tweets
   - Monitor your API usage

### Error Messages

- `❌ Authentication failed`: Check your API credentials
- `❌ Image file not found`: Verify the image path is correct
- `❌ Error posting tweet`: Check your internet connection and API status

## 📝 Example Outputs

When you run the scripts, you'll see output like:

```
🐦 Twitter Bot Starting...
==================================================
✅ Twitter API clients initialized successfully!
✅ Authentication successful!
📱 Connected as: @your_username
👤 Display name: Your Display Name

==================================================
🚀 Bot is ready! You can now use the following methods:
   • bot.post_text_tweet('Your message here')
   • bot.post_tweet_with_image('Your message', 'path/to/image.jpg')
   • bot.post_tweet_with_multiple_images('Your message', ['img1.jpg', 'img2.jpg'])
==================================================
```

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Useful Links

- [Twitter Developer Portal](https://developer.twitter.com/)
- [Tweepy Documentation](https://docs.tweepy.org/)
- [Twitter API v2 Documentation](https://developer.twitter.com/en/docs/twitter-api)

---

**Happy Tweeting! 🐦✨**