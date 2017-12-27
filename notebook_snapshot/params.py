
import json

from copy import deepcopy as copy


class Params:
    """
    """

    def __init__(self,
                 verbose=False,
                 **kwargs):
        """
        """
        # attributes
        self.is_ribbon = True
        self.ribbon_color = 'blue'
        self.ribbon_text = 'Draft'
        self.ribbon_position = 'top-right'

        self.hide_code = False

        self.important_border = '3px'
        self.important_color = 'red'
        self.important_background_color = '#f7f7f7'

        for k, v in kwargs.items():
            setattr(self, k, v)
        self.valid = self.check(verbose=verbose)

    def check(self, verbose=False):
        """
        """
        isRibbon = isinstance(self.is_ribbon, bool)
        li_ribbon_color = ['white', 'black', 'grey', 'blue',
                           'green', 'turquoise', 'purple', 'red', 'orange', 'yellow']
        isRibbonColor = self.ribbon_color in li_ribbon_color
        isRibbonText = isinstance(self.ribbon_text, str)
        li_ribbon_pos = ['top-right', 'top-left', 'bottom-right', 'bottom-left']
        isRibbonPosition = self.ribbon_position in li_ribbon_pos

        isHideCode = isinstance(self.hide_code, bool)

        isImportantBorder = isinstance(self.important_border, str)
        isImportantColor = isinstance(self.important_color, str)
        isImportantBackgroundColor = isinstance(
            self.important_background_color, str)

        isParams = all([isRibbon, isRibbonColor, isRibbonText, isRibbonPosition, isHideCode,
                        isImportantBorder, isImportantColor, isImportantBackgroundColor])

        if verbose:
            print('Params: isRibbon=', isRibbon)
            print('Params: isRibbonColor=', isRibbonColor)
            print('Params: isRibbonText=', isRibbonText)
            print('Params: isRibbonPosition=', isRibbonPosition)
            print('Params: isHideCode=', isHideCode)
            print('Params: isImportantBorder=', isImportantBorder)
            print('Params: isImportantColor=', isImportantColor)
            print('Params: isImportantBackgroundColor=', isImportantBackgroundColor)

            print('Params: isParams=', isParams)
        msg = 'Params must contain attributes to fill jinja2 template main.tpl.html'
        assert isParams, msg

        return True

    def to_dict(self):
        """
        """
        d = copy(self.__dict__)
        d = {k: v for k, v in d.items() if v is not None}
        return d

    def pprint(self, indent=2):
        """
        """
        d = json.dumps(self.to_dict(),
                       sort_keys=True,
                       indent=indent)
        print(d)

    def __repr__(self):
        return str(self.to_dict())