
import sys
import subprocess as sp


def snapshot(path_nb,
             path_template=None,
             embed_img=True,
             ):
    """
    """
    if embed_img:
        exporter = 'notebook_snapshot.html_embed_img'
    else:
        exporter = 'html'

    cmd = 'jupyter nbconvert --to {} --template {} {}'
    cmd = cmd.format(exporter, path_template, path_nb)
    print(cmd)
    args = cmd.split()
    # os.system(cmd)

    with sp.Popen(args, stdout=sp.PIPE, stderr=sp.PIPE) as process:
        # Read stdout character by character, as it includes real-time progress updates
        for c in iter(lambda: process.stdout.read(1), b''):
            sys.stdout.write(c.decode(sys.stdout.encoding))
        # Read stderr line by line, because real-time does not matter
        for line in iter(process.stderr.readline, b''):
            sys.stderr.write(line.decode(sys.stderr.encoding))
