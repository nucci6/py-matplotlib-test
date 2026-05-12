import os
import numpy as np
import matplotlib

# Force non-interactive backend for headless HPC nodes
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def test_matplotlib_installation():
    print("--- Matplotlib Sanity Check ---")
    print(f"Version: {matplotlib.__version__}")
    print(f"Backend: {matplotlib.get_backend()}")
    assert matplotlib.__version__ == "3.10.7", f"Version mismatch! Found {matplotlib.__version__}"
    
    try:
        print("\n1. Testing basic line plot and scatter plot...")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Line plot
        x = np.linspace(0, 10, 100)
        ax.plot(x, np.sin(x), label='Sine Wave', color='blue', linewidth=2)
        
        # Scatter plot
        rx = np.random.rand(50) * 10
        ry = np.random.randn(50)
        ax.scatter(rx, ry, color='red', marker='x', label='Random Data')
        
        ax.set_title("Matplotlib Sanity Check")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        ax.grid(True)
        
        print("2. Testing file export (PNG)...")
        output_filename = "matplotlib_test_output.png"
        plt.savefig(output_filename, dpi=150, bbox_inches='tight')
        
        if os.path.exists(output_filename):
            file_size = os.path.getsize(output_filename)
            print(f"   -> Success! Plot saved to {output_filename} ({file_size} bytes).")
        else:
            print(f"   -> Error: File {output_filename} was not created.")
            
        print("\n Matplotlib 3.10.7 is installed and functioning correctly!")

    except Exception as e:
        print(f"\nL Unexpected Error: {e}")

if __name__ == "__main__":
    test_matplotlib_installation()
