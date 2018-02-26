
import os
import nbformat
import warnings

import datetime as dt

from IPython.display import display, Markdown
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError


def execute(path_nb,
            dated=True,
            timeout=600,
            kernel_name='python3',
            verbose=False):
    """
    """

    folder = os.path.dirname(path_nb)
    filename = os.path.basename(path_nb)

    now = dt.datetime.now().strftime('%Y%m%d_%H%M%S.%f')[:-3]
    if dated:
        save_name = '{}_{}'.format(now, filename)
    else:
        save_name = filename

    # path_output
    path_out = os.path.join(folder, save_name)

    # load nb
    with open(path_nb, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # create ep
    ep = ExecutePreprocessor(timeout=timeout,
                             kernel_name=kernel_name)

    # run catching errors
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            out = ep.preprocess(nb, {'metadata': {'path': '.'}})
    except CellExecutionError:
        out = None
        msg = 'Error executing notebook {}\nSee notebook {} for traceback.'
        msg = msg.format(path_nb, path_out)
        print(msg)
        raise
    finally:
        with open(path_out, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)

    if verbose:
        md = 'Notebook **{}** run and saved as **{}**'
        md = md.format(path_nb, path_out)
        display(Markdown(md))

    return path_out, now
