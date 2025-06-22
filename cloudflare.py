import os
import json
import getpass
from pathlib import Path

class CloudflareCredentialsManager:
    """Manage Cloudflare API credentials securely"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.cloudflare'
        self.config_file = self.config_dir / 'credentials.json'
        self.env_file = Path('.env')
        # Your pre-configured API key
        self.default_api_token = "Your_Key"
        
    def setup_config_directory(self):
        """Create config directory if it doesn't exist"""
        self.config_dir.mkdir(exist_ok=True)
        
    def auto_setup_with_your_key(self):
        """Automatically set up with your provided API key"""
        print("🔐 Setting up with your Cloudflare API Key")
        print("=" * 45)
        
        credentials = {
            'CLOUDFLARE_API_TOKEN': self.default_api_token
        }
        
        # Ask for additional optional credentials
        print(f"✅ API Token: {self.default_api_token[:8]}...{self.default_api_token[-4:]}")
        
        # Account ID
        print("\n📋 Optional: Add your Cloudflare Account ID for better functionality")
        print("   - Found in the right sidebar of your Cloudflare dashboard")
        account_id = input("   Enter your Cloudflare Account ID (press Enter to skip): ").strip()
        if account_id:
            credentials['CLOUDFLARE_ACCOUNT_ID'] = account_id
        
        # Zone ID (for custom domain)
        print("\n🌐 Optional: Add Zone ID for custom domains")
        print("   - Go to your domain in Cloudflare dashboard")
        print("   - Found in the right sidebar under 'API'")
        zone_id = input("   Enter your Cloudflare Zone ID (press Enter to skip): ").strip()
        if zone_id:
            credentials['CLOUDFLARE_ZONE_ID'] = zone_id
        
        # Custom Domain
        print("\n🏠 Optional: Add custom domain")
        print("   - Your domain name for custom subdomains (e.g., 'yourdomain.com')")
        custom_domain = input("   Enter your custom domain (press Enter to skip): ").strip()
        if custom_domain:
            credentials['CUSTOM_DOMAIN'] = custom_domain
        
        return credentials
    
    def input_credentials(self):
        """Prompt user to input Cloudflare credentials"""
        print("🔐 Cloudflare Credentials Setup")
        print("=" * 40)
        
        credentials = {}
        
        # API Token with your key as default
        print("\n1. Cloudflare API Token:")
        print(f"   Default: {self.default_api_token[:8]}...{self.default_api_token[-4:]}")
        use_default = input("   Use your pre-configured API token? (Y/n): ").strip().lower()
        
        if use_default != 'n':
            credentials['CLOUDFLARE_API_TOKEN'] = self.default_api_token
            print("   ✅ Using your pre-configured API token")
        else:
            print("   - Go to https://dash.cloudflare.com/profile/api-tokens")
            print("   - Create a token with 'Cloudflare Pages:Edit' and 'Zone:Read' permissions")
            api_token = getpass.getpass("   Enter your Cloudflare API Token: ").strip()
            if not api_token:
                print("❌ API Token is required!")
                return None
            credentials['CLOUDFLARE_API_TOKEN'] = api_token
        
        # Account ID
        print("\n2. Cloudflare Account ID:")
        print("   - Found in the right sidebar of your Cloudflare dashboard")
        account_id = input("   Enter your Cloudflare Account ID: ").strip()
        if account_id:
            credentials['CLOUDFLARE_ACCOUNT_ID'] = account_id
        
        # Zone ID (for custom domain)
        print("\n3. Cloudflare Zone ID (Optional - for custom domains):")
        print("   - Go to your domain in Cloudflare dashboard")
        print("   - Found in the right sidebar under 'API'")
        zone_id = input("   Enter your Cloudflare Zone ID (press Enter to skip): ").strip()
        if zone_id:
            credentials['CLOUDFLARE_ZONE_ID'] = zone_id
        
        # Custom Domain
        print("\n4. Custom Domain (Optional):")
        print("   - Your domain name for custom subdomains (e.g., 'yourdomain.com')")
        custom_domain = input("   Enter your custom domain (press Enter to skip): ").strip()
        if custom_domain:
            credentials['CUSTOM_DOMAIN'] = custom_domain
        
        return credentials
    
    def quick_setup(self):
        """Quick setup with just your API key"""
        credentials = {
            'CLOUDFLARE_API_TOKEN': self.default_api_token
        }
        
        # Save to both JSON and .env
        self.save_credentials_to_json(credentials)
        self.save_credentials_to_env(credentials)
        
        print("🚀 Quick setup complete!")
        print(f"✅ API Token configured: {self.default_api_token[:8]}...{self.default_api_token[-4:]}")
        
        return credentials
    
    def save_credentials_to_json(self, credentials):
        """Save credentials to JSON file"""
        self.setup_config_directory()
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(credentials, f, indent=2)
            
            # Set restrictive permissions on the file
            os.chmod(self.config_file, 0o600)
            print(f"✅ Credentials saved to {self.config_file}")
            return True
        except Exception as e:
            print(f"❌ Error saving credentials: {e}")
            return False
    
    def save_credentials_to_env(self, credentials):
        """Save credentials to .env file"""
        try:
            env_content = []
            
            # Read existing .env file if it exists
            if self.env_file.exists():
                with open(self.env_file, 'r') as f:
                    env_content = f.readlines()
            
            # Remove existing Cloudflare entries
            env_content = [line for line in env_content 
                          if not any(line.startswith(key) for key in credentials.keys())]
            
            # Add new credentials
            for key, value in credentials.items():
                env_content.append(f"{key}={value}\n")
            
            # Write back to .env file
            with open(self.env_file, 'w') as f:
                f.writelines(env_content)
            
            print(f"✅ Credentials saved to {self.env_file}")
            return True
        except Exception as e:
            print(f"❌ Error saving to .env file: {e}")
            return False
    
    def load_credentials_from_json(self):
        """Load credentials from JSON file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"❌ Error loading credentials: {e}")
            return None
    
    def load_credentials_from_env(self):
        """Load credentials from environment variables"""
        credentials = {}
        env_vars = ['CLOUDFLARE_API_TOKEN', 'CLOUDFLARE_ACCOUNT_ID', 
                   'CLOUDFLARE_ZONE_ID', 'CUSTOM_DOMAIN']
        
        for var in env_vars:
            value = os.getenv(var)
            if value:
                credentials[var] = value
        
        return credentials if credentials else None
    
    def display_credentials(self, credentials):
        """Display credentials (masked for security)"""
        print("\n📋 Current Credentials:")
        print("=" * 30)
        
        for key, value in credentials.items():
            if 'TOKEN' in key:
                # Mask the token for security
                masked_value = value[:8] + '*' * (len(value) - 12) + value[-4:] if len(value) > 12 else '*' * len(value)
                print(f"   {key}: {masked_value}")
            else:
                print(f"   {key}: {value}")
    
    def test_credentials(self, credentials):
        """Test if credentials work with Cloudflare API"""
        try:
            import requests
            
            api_token = credentials.get('CLOUDFLARE_API_TOKEN')
            if not api_token:
                return False, "No API token provided"
            
            headers = {
                'Authorization': f'Bearer {api_token}',
                'Content-Type': 'application/json'
            }
            
            # Test API token by getting user info
            response = requests.get('https://api.cloudflare.com/client/v4/user', headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    user_email = data.get('result', {}).get('email', 'Unknown')
                    return True, f"✅ API token valid for user: {user_email}"
                else:
                    return False, f"❌ API returned error: {data.get('errors', 'Unknown error')}"
            else:
                return False, f"❌ HTTP {response.status_code}: {response.text}"
                
        except ImportError:
            return None, "⚠️ 'requests' library not installed. Run: pip install requests"
        except Exception as e:
            return False, f"❌ Error testing credentials: {e}"
    
    def set_environment_variables(self):
        """Set environment variables for current session"""
        credentials = self.load_credentials_from_json()
        if not credentials:
            credentials = {'CLOUDFLARE_API_TOKEN': self.default_api_token}
        
        for key, value in credentials.items():
            os.environ[key] = value
            print(f"✅ Set {key}")
        
        print("🌟 Environment variables set for current session!")
        return credentials

def main():
    """Main function to handle credential management"""
    manager = CloudflareCredentialsManager()
    
    # Check if credentials already exist
    existing_creds = manager.load_credentials_from_json()
    if not existing_creds:
        existing_creds = manager.load_credentials_from_env()
    
    if not existing_creds:
        print("🎉 Welcome! No existing credentials found.")
        print("Let's set up your Cloudflare credentials quickly!")
        quick_setup = input("\nDo quick setup with your API key? (Y/n): ").strip().lower()
        if quick_setup != 'n':
            manager.quick_setup()
            print("\n🎯 Setup complete! You can now use the deployment script.")
            return
    
    while True:
        print("\n🌐 Cloudflare Credentials Manager")
        print("=" * 35)
        print("1. Quick setup (use your API key)")
        print("2. Full setup (add Account ID, Zone ID, etc.)")
        print("3. View current credentials")
        print("4. Test credentials")
        print("5. Set environment variables")
        print("6. Delete credentials")
        print("7. Export commands")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == '1':
            # Quick setup
            manager.quick_setup()
        
        elif choice == '2':
            # Full setup
            credentials = manager.auto_setup_with_your_key()
            if credentials:
                print("\nSave credentials to:")
                print("1. JSON file (recommended)")
                print("2. .env file")
                print("3. Both")
                
                save_choice = input("Select option (1-3): ").strip()
                
                if save_choice in ['1', '3']:
                    manager.save_credentials_to_json(credentials)
                
                if save_choice in ['2', '3']:
                    manager.save_credentials_to_env(credentials)
        
        elif choice == '3':
            # View current credentials
            credentials = manager.load_credentials_from_json()
            if not credentials:
                credentials = manager.load_credentials_from_env()
            
            if credentials:
                manager.display_credentials(credentials)
            else:
                print("ℹ️ No credentials found")
        
        elif choice == '4':
            # Test credentials
            credentials = manager.load_credentials_from_json()
            if not credentials:
                credentials = manager.load_credentials_from_env()
            
            if credentials:
                print("\n🧪 Testing credentials...")
                success, message = manager.test_credentials(credentials)
                print(message)
            else:
                print("❌ No credentials found to test")
        
        elif choice == '5':
            # Set environment variables
            manager.set_environment_variables()
        
        elif choice == '6':
            # Delete credentials
            confirm = input("Are you sure you want to delete all credentials? (y/N): ").strip().lower()
            if confirm == 'y':
                manager.delete_credentials()
        
        elif choice == '7':
            # Export to environment variables
            credentials = manager.load_credentials_from_json()
            if not credentials:
                credentials = manager.load_credentials_from_env()
            
            if credentials:
                print("\n📤 Export commands:")
                print("Copy and paste these commands in your terminal:")
                print("-" * 50)
                for key, value in credentials.items():
                    print(f"export {key}='{value}'")
                print("-" * 50)
            else:
                print("❌ No credentials found to export")
        
        elif choice == '8':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-8.")

if __name__ == "__main__":
    main()
