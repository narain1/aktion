import os
import subprocess
from sklearn.model_selection import KFold
from tqdm.auto import tqdm

os.makedirs('exp', exist_ok=True)

for file in tqdm(os.listdir(os.getcwd())):
    if file.endswith('.ipynb'):
        subprocess.run(f"jupyter nbconvert --to notebook --execute {file} --output {file} --output-dir nbs".split())
