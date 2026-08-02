import os

files = {
    'vs 3M전 1Q.html': 'vs-3M-1Q.html',
    'vs 3M전 3Q.html': 'vs-3M-3Q.html',
    'vs 3M전 1Q MP4.html': 'vs-3M-1Q-MP4.html',
    'vs 3M전 3Q MP4.html': 'vs-3M-3Q-MP4.html'
}

for old_name, new_name in files.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")