import os
import subprocess
from sklearn.model_selection import KFold
from tqdm.auto import tqdm

for file in tqdm(os.listdir(os.getcwd())):
    if file.endswith('.ipynb'): subprocess.run("jupyter nbconvert --to notebook --execute {file} --output {file}")

