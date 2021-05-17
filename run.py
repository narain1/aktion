import os
import subprocess
from sklearn.model_selection import KFold
from tqdm.auto import tqdm

for file in tqdm(os.listdir(os.getcwd())):
    if file.endswith('.ipynb'):
        p = os.path.join(os.getcwd(), file)
        subprocess.run("jupyter nbconvert --to notebook --execute {file} --output {file}".split())
