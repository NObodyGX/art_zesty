from PySide6.QtWidgets import QWidget


class GBWidget(QWidget):
    def __init__(self, parent: None):
        super().__init__(parent)

        self._setup_ui()
        self._setup_fn()

    def _setup_ui(self):
        pass

    def _setup_fn(self):
        pass
