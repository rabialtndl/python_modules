import sys
import os
import site


def is_env_virtual() -> bool:
    if sys.prefix != sys.base_prefix:
        result = True
    else:
        result = False
    return result


def get_env_name() -> str | None:
    if is_env_virtual():
        return os.path.basename(sys.prefix)
    return None


def get_package_path() -> str:
    packages = site.getsitepackages()
    if packages:
        return packages[0]
    else:
        return " "


def main() -> None:
    result_of_venv = is_env_virtual()
    current_situation = sys.executable

    if not result_of_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {current_situation}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")

    else:
        env_name = get_env_name()
        env_path = sys.prefix
        package_path = get_package_path()
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {current_situation}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print(f"\nPackage installation path: \n {package_path}")


if __name__ == "__main__":
    main()
