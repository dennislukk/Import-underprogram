from tqdm import tqdm as prosentvis
import time

for i in prosentvis(range(10000), desc="Fortnie update"):
    time.sleep(0.01)


