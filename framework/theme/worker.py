from enum import Enum

from .theme_default import GDefaultTheme
from .theme_light import GLightTheme


class GThemeWorker(object):

    class GThemeEnum(Enum):
        default = "default"
        light = "light"

    cur_theme = GThemeEnum.default

    @staticmethod
    def apply(widget, theme=GThemeEnum.default):
        match theme:
            case GThemeWorker.GThemeEnum.default:
                theme_gen = GDefaultTheme()
            case GThemeWorker.GThemeEnum.light:
                theme_gen = GLightTheme()
            case _:
                theme_gen = None
        if not theme_gen:
            print("[error] unsupport theme")
            return False
        GThemeWorker.cur_theme = theme
        widget.setStyleSheet(theme_gen.theme())
        return True
