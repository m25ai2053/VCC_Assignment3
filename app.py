import math
import time

def heavy_computation():
    print("Sample App: Starting heavy mathematical processing...")
    # This will keep the CPU busy to trigger the 75% threshold
    while True:
        [math.sqrt(i) for i in range(10000)]

if __name__ == "__main__":
    heavy_computation()
