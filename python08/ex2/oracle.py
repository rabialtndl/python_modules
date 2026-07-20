import os
import sys

try:
    from dotenv import load_dotenv 
except ImportError:
    print("Error: python-dotenv is not installed.")
    sys.exit(1)

def get_configuration() -> dict[str, str]:
    load_dotenv()

    matrix_mode: str | None = os.getenv("MATRIX_MODE")
    
    if not matrix_mode:
        return{
            "Mode" : matrix_mode,
            "Database" : os.getenv("DATABASE_URL", "Disconnected"),
            "API Access" : os.getenv("API_KEY", ""),
            "Log Level" : os.getenv("LOG_LEVEL", "INFO"),
            "Zion Network" : os.getenv("ZION_ENDPOINT", "OFFLINE")
        }     
        

def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        
    print("\nORACLE STATUS: Reading the Matrix...")
    config: dict | None = get_configuration()
    

if __name__ == "__main__":
    main()
