from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QWidget, QPushButton, QFileDialog
import os

from framework.utils.u_worker import UWorker


class DirPathEdit(QLineEdit):
    def __init__(self, parent=None):
        self.p = parent  # type: GDirPathWidget
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setPlaceholderText("请输入目录路径")
        self.textChanged.connect(self.on_text_changed)

    def dragEnterEvent(self, event):
        fullpath = event.mimeData().urls()[0].toLocalFile()
        if not os.path.exists(fullpath):
            return
        text = fullpath
        if os.path.isfile(fullpath):
            text = os.path.dirname(fullpath)
        self.set_text(text)
        event.accept()

    def dropEvent(self, event):
        # 把原有的取消掉
        pass

    def set_text(self, v: str):
        self.setText(v)
        self.on_text_changed(v)

    def on_text_changed(self, v):
        self.p.dir_changed.emit(v)


class GDirPathWidget(QWidget):
    dir_changed = Signal(str)

    def __init__(self, parent: None):
        super().__init__(parent)

        self._setup_ui()
        self._setup_fn()

    def _setup_ui(self):
        self.w_center = DirPathEdit(self)
        self.w_button = QPushButton("📂")

        layout = UWorker.hlayout()
        layout.addWidget(self.w_center)
        layout.addWidget(self.w_button)
        self.setLayout(layout)

    def _setup_fn(self):
        self.w_button.clicked.connect(self._on_dir_clicked)

    def _on_dir_clicked(self):
        cdir = QFileDialog.getExistingDirectory(self, "选择文件路径", ".")
        if not cdir:
            return
        self.w_center.set_text(os.path.normpath(cdir))

    def v(self) -> str:
        cdir = self.w_center.text()
        return os.path.normpath(cdir)
