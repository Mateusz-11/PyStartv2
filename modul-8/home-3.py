from os import walk
from pathlib import Path

statistics = {}
for _, _, files in walk('source'):
    for file in files:
        path = Path(file)
        extension = path.suffix.replace('.', '')
        statistics.update({extension: statistics.get(extension)})

print(statistics)
