from .default_theme import DTheme


class GThemeWorker(object):
    cur_theme = ""

    @staticmethod
    def apply(widget, theme="default"):
        theme_gen = None
        if theme == "default":
            theme_gen = DTheme()
        if not theme_gen:
            return False
        widget.setStyleSheet(theme_gen.theme())
        return True
