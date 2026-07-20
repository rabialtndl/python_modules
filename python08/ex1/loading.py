import sys
import importlib


def package_control(package_name: str) -> str:
    try:
        module = importlib.import_module(package_name)
        return getattr(module, "__version__", "unknown")
    except ImportError:
        return ""


def dependency_control() -> bool:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    pandas_version = package_control("pandas")
    numpy_version = package_control("numpy")
    matplotlib_version = package_control("matplotlib")
    requests_version = package_control("requests")
    is_ready: bool = True

    if pandas_version:
        print(f"[OK] Pandas ({pandas_version}) - Data manipulation ready")
    else:
        print("[MISSING] Pandas is not installed.")
        is_ready = False

    if numpy_version:
        print(f"[OK] Numpy ({numpy_version}) - Numerical computation ready")
    else:
        print("[MISSING] Numpy is not installed.")
        is_ready = False

    if requests_version:
        print(f"[OK] Request ({requests_version}) - Network access ready")
    else:
        print("[MISSING] Request is not installed.")
        is_ready = False

    if matplotlib_version:
        print(f"[OK] Matplotlib ({matplotlib_version}) - Visualization ready")
    else:
        print("[MISSING] Matplotlib is not installed.")
        is_ready = False

    if not is_ready:
        print(
            "\n# Should show missing dependencies "
            "and installation instructions for pip and Poetry"
            )
        print("Using pip: pip install -r requirements.txt")
        print("Using poetry: poetry install")
        return False

    return True


def analyze_matrix() -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    data = np.random.uniform(0, 100, 1000)
    df = pd.DataFrame(data, columns=["values"])

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))

    plt.hist(df["values"], bins=100, color="green", edgecolor="black")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Percentile Ranges")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


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
    if not dependency_control():
        sys.exit(1)
    analyze_matrix()


if __name__ == "__main__":
    main()
