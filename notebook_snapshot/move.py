
import os
import glob
import shutil

from IPython.display import display, Markdown


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
        md = """
Moved the files below to folder {}
```json
{}
```
""".format(folder, filenames)
        display(Markdown(md))
