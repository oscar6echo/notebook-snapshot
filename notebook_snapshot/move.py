
import os
import glob
import shutil


def move(tag,
         folder='store',
         verbose=False):
    """
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    filenames = glob.glob('{}*.ipynb'.format(tag)) + \
                glob.glob('{}*.html'.format(tag))
    for f in filenames:
        shutil.move(f, folder)

    if verbose:
        msg = 'Moved the files below to folder {}'
        msg =msg.format(folder)
        print(msg)
        print('\n'.join(filenames))
