import os
import subprocess
from tqdm.auto import tqdm

for file in tqdm(os.listdir(os.cwd())):
    if file.endswith('.ipynb'): subprocess.run("jupyter nbconvert --to notebook --execute {file} --output {file}")

