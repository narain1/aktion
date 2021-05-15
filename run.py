import os
import subprocess
from sklearn.model_selection import KFold

for file in os.listdir(os.cwd()):
    if file.endswith('.ipynb'): subprocess.run("jupyter nbconvert --to notebook --execute {file} --output {file}")

