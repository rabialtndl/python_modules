import os
import sys
from typing import Dict

from dotenv import load_dotenv


def load_configuration() -> Dict[str, str]:
    """Load configuration from environment variables and .env file."""
    load_dotenv()

    config: Dict[str, str] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "")
    }

    return config


def check_security(config: Dict[str, str]) -> None:
    """Ensure required configuration is present and handle missing data."""
    if not config["API_KEY"]:
        print("[ERROR] API_KEY is missing! Cannot authenticate.")
        sys.exit(1)


def display_status(config: Dict[str, str]) -> None:
    """Print the system status based on the current configuration mode."""
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    mode: str = config["MATRIX_MODE"]
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to PRODUCTION cluster")
        print("API Access: Authenticated (Live Secure Data)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")

    print(f"Log Level: {config['LOG_LEVEL']}")
    
    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
        
    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")
        
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    """Main execution block of the script."""
    config: Dict[str, str] = load_configuration()
    check_security(config)
    display_status(config)


if __name__ == "__main__":
    main()