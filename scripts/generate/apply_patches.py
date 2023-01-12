import glob
import subprocess

def apply_patches():
    print('⏳ Applying patches...')
    for patch in glob.glob('patches/*.patch'):
        print('⏳ Applying patch %s' % patch)
        subprocess.call(['patch', '-p1', '-i', patch])
    print('✅ Done applying patches.')