
import sys
import os
import re
import jinja2 as jj

from .params import Params


class Template:
    """
    """

    def __init__(self,
                 template_str=None,
                 params=None
                 ):
        """
        """

        dir_file = os.path.dirname(os.path.abspath(__file__))
        dir_template = os.path.join(dir_file, 'templates')

        loader = jj.FileSystemLoader(dir_template)

        env = jj.Environment(loader=loader,
                             variable_start_string='__$',
                             variable_end_string='$__',
                             block_start_string='{-%',
                             block_end_string='%-}'
                             )

        if not template_str:
            template_name = 'main.tpl.html'
            template = env.get_template(template_name)
        else:
            template = env.from_string(template_str)

        if isinstance(params, Params):
            data = params.to_dict()
        else:
            msg = 'If params is not an instance of Params it must be a dict valid for the template used'
            assert isinstance(params, dict), msg
            data = params

        self.content = template.render(data=data)

    def save(self,
             save_folder=None,
             save_name=None,
             verbose=False):
        """
        """
        if not save_folder:
            save_folder = 'dump'

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        if not save_name:
            save_name = 'my_template.tpl'

        file_path = os.path.join(save_folder, save_name)
        with open(file_path, 'w') as f:
            f.write(self.content)

        if verbose:
            msg = 'template {} created'
            msg = msg.format(file_path)

        self.path = file_path
