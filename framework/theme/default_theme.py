class ButtonCss(object):
    def __init__(self, name: str):
        self.name = name
        self.attr = []

    def setv(self, attr: str, v: str):
        self.attr.append((attr, v))

    def __str__(self):
        a = []
        for k, v in self.attr:
            key = f"{self.name}"
            if key:
                key = f"{self.name}:{k}"
            a.append(f"{key}{{")
            a.append(v)
            a.append("}")
        return "\n".join(a)


class DTheme(object):
    g_color = "#ededed"
    g_bg_color = "#21252b"
    g_bg_d_color = "#3b414d"
    g_hover_bg_color = "#262a31"
    g_left_select_color = "#528bff"
    g_border_color = "#ecdbba"
    g_select_bg_color = "#2c313a"
    g_min_color = "#fcd53f"
    g_max_color = "#00d26a"
    g_off_color = "#f92f60"
    g_off_d_color = "#9a1c29"
    g_ok_color = "#00d26a"
    g_no_color = "#f92f60"

    def __init__(self):
        self.widget = [
            "QWidget {",
            f"  background-color: {DTheme.g_bg_color};",
            f"  color: {DTheme.g_color};",
            "}",
        ]
        self.button = [
            "GBaseButton{",
            "  border: none;",
            "  border-radius: none;",
            f"  background-color: {DTheme.g_bg_color};",
            "  padding: 0;",
            "}",
            "GBaseButton:hover {",
            f"  background-color: {DTheme.g_hover_bg_color};",
            "}",
            "GBaseButton:pressed {",
            f"  background-color: {DTheme.g_hover_bg_color};",
            "}",
        ]
        self.button_ext = [
            "GTitleButton,",
            "GTCheckButton,",
            "GTMinButton,",
            "GTMaxButton,",
            "GTOffButton {",
            "  background-color: transparent;",
            "}",
        ]
        self.button_min = [
            "GTMinButton:hover,",
            "GTMinButton:pressed {",
            f"  color: {DTheme.g_min_color};",
            f"  background-color: {DTheme.g_min_color};",
            "}",
        ]
        self.button_max = [
            "GTMaxButton:hover,",
            "GTMaxButton:pressed {",
            f"  color: {DTheme.g_max_color};",
            f"  background-color: {DTheme.g_max_color};",
            "}",
        ]
        self.button_off = [
            "GTOffButton:hover {",
            f"  color: {DTheme.g_off_color};",
            f"  background-color: {DTheme.g_off_color};",
            "}",
            "GTOffButton:pressed {",
            f"  color: {DTheme.g_off_d_color};",
            f"  background-color: {DTheme.g_off_d_color};",
            "}",
        ]
        self.button_ok = [
            "GOKButton {",
            "  border: none;",
            f"  background-color: {DTheme.g_ok_color};",
            "  border-radius: 4px;",
            "}",
        ]
        self.button_no = [
            "GNOButton {",
            "  border: none;",
            f"  background-color: {DTheme.g_no_color};",
            "  border-radius: 4px;",
            "}",
        ]
        self.button_check = [
            "GCheckButton {",
            "  border: none;",
            "  background-color: transparent;",
            # "  image: url(:/res/icon/common/checkbox.svg);"
            "}",
            "GCheckButton:checked {",
            "  border: none;",
            "  background-color: transparent;",
            # "  image: url(:/res/icon/common/checkbox_yes.svg);"
            "}",
            "GCheckButton:hover {",
            "  background-color: transparent;",
            "}",
        ]
        self.button_grid = [
            "GGridLabelButton {",
            f"  border: 1px solid {DTheme.g_color};",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
            "GGridLabelButton:hover {",
            f"  border: 1px solid {DTheme.g_left_select_color};",
            "  background-color: transparent;",
            "}",
            "GGridLabelButton:pressed {",
            f"  border: 1px solid {DTheme.g_border_color};",
            "  background-color: transparent;",
            "}",
        ]

        self.combobox = [
            "QComboBox {",
            "  height: 42px;",
            "  border: none;",
            f"  color: {DTheme.g_color};",
            "  font-size: 12px;",
            "  padding-left: 8px;",
            "  padding-right: 8px;",
            "  /*** 用于控制 qcombobox 的显示方式，包含 0 和 1 ***/",
            "  combobox-popup: 0;",
            "  border-radius: 0;",
            "  background: transparent;",
            "}",
            "QComboBox:hover {",
            "  background: transparent;",
            "  border: none;",
            "}",
            "QComboBox:focus {",
            "  border: none;",
            f"  background: {DTheme.g_bg_color};",
            "}",
            "/*** combox 点击样式 ***/",
            "QComboBox:on {",
            "  border: none;",
            "  background: transparent;",
            "  padding-left: 8px;",
            "}",
            "QComboBox::drop-down {",
            "  border: 0px;",
            "}",
            "/*** 下拉箭头样式 ***/",
            "QComboBox::down-arrow {",
            # "  image: url(:/res/icon/common/icon_arrow_down.svg);",
            "  padding-right: 8px;",
            "}",
            "QComboBox::down-arrow:on {",
            # "  image: url(:/res/icon/common/icon_arrow_down.svg);",
            "  padding-right: 8px;",
            "}",
            "/*** 下拉框的样式 ***/",
            "QComboBox QAbstractItemView {",
            "  border: none;",
            "  border-top: none;",
            "  outline: none;",
            "}",
            "/*** 下拉后下拉项的样式 ***/",
            "QComboBox QAbstractItemView::item {",
            "  min-width: 110px;",
            "  min-height: 32px;",
            "  font-size: 16px;",
            f"  color: {DTheme.g_color};",
            f"  background: {DTheme.g_bg_color};",
            "  padding-left: 4px;",
            "  padding-right: 0px;",
            "}",
            "QComboBox QAbstractItemView::item:hover:!selected {",
            f"  background: {DTheme.g_bg_color};",
            "  padding-left: 4px;",
            f"  border-left: 2px solid {DTheme.g_color};",
            "}",
            "QComboBox QAbstractItemView::item:selected {",
            f"  background: {DTheme.g_select_bg_color};",
            "  padding-left: 4px;",
            "}",
        ]
        self.checkbox = [
            "QCheckBox {",
            f"  background: {DTheme.g_bg_color};",
            "}",
        ]

        self.label = []
        self.label_ext = [
            "GNumberLabel {",
            f"  color: {DTheme.g_color};",
            f"  background: {DTheme.g_bg_color};",
            "}",
        ]

        self.list_widget = [
            "QListWidget {",
            f"  background: {DTheme.g_bg_color};",
            "  border: none;",
            "  outline: none;",
            "}",
        ]
        self.list_widget_item = [
            "QListWidget::item {",
            "}",
            "QListWidget::item:focus {",
            f"  border-left: 3px solid {DTheme.g_color};",
            "}",
            "QListWidget::item:hover {",
            f"  background: {DTheme.g_hover_bg_color};",
            "}",
            "QListWidget::item::selected {",
            f"  background: {DTheme.g_select_bg_color};",
            f"  border-left: 3px solid {DTheme.g_left_select_color};",
            "}",
        ]

        self.line_edit = [
            "QLineEdit {",
            "  background: transparent;",
            "}",
        ]

        self.scroll_area = [
            "QScrollArea {",
            "  border: none;",
            "}",
        ]

        self.scroll_bar = [
            "QScrollBar:vertical {",
            "  border: none;",
            f"  background-color: {DTheme.g_bg_color};",
            "  width: 10px;",
            "  margin: 0px 0px 0px 0px;",
            "}",
            "QScrollBar::handle:vertical {",
            "  border: none;",
            f"  background-color: {DTheme.g_bg_d_color};",
            "  min-width: 8px;",
            "QScrollBar::sub-page:vertical,",
            "QScrollBar::add-page:vertical {",
            f"  background: {DTheme.g_bg_color};",
            "}",
            "QScrollBar::sub-line:vertical,",
            "QScrollBar::add-line:vertical {",
            f"  height: 0px;",
            "}",
            "QScrollBar:horizontal {",
            "  border: none;",
            f"  background-color: {DTheme.g_bg_color};",
            "  width: 10px;",
            "  margin: 0px 0px 0px 0px;",
            "}",
            "QScrollBar::handle:horizontal {",
            "  border: none;",
            f"  background-color: {DTheme.g_bg_d_color};",
            "  min-width: 8px;",
            "QScrollBar::sub-page:horizontal,",
            "QScrollBar::add-page:horizontal {",
            f"  background: {DTheme.g_bg_color};",
            "}",
            "QScrollBar::sub-line:horizontal,",
            "QScrollBar::add-line:horizontal {",
            f"  height: 0px;",
            "}",
        ]

        self.slider = [
            "QSlider::groove:horizontal{ ",
            "  height: 10px;",
            "  left: 0px;",
            "  right: 0px;",
            "  border: none;",
            f"  background: {DTheme.g_bg_color};",
            "}",
            "QSlider::handle:horizontal{ ",
            "  width:  10px;",
            "  height: 10px;",
            "  border-image: none;",
            "QSlider::sub-page:horizontal{",
            "  background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00dbde, stop:1 #f902ff);;}",
            "}",
        ]

        self.tooltip = [
            "QToolTip {",
            "  min-width:140;",
            f"  border: 1px solid {DTheme.g_border_color};"
            "  margin: 0px;"
            "  padding: 0px 4px 0px 4px;"
            f"  color: {DTheme.g_color};",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
        ]

        self.menu_bar = [
            "QMenuBar {",
            f"  color: {DTheme.g_color};",
            "  border: none;",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
            "QMenuBar::item {",
            f"  color: {DTheme.g_color};",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
            "QMenuBar::item::selected {",
            f"  color: {DTheme.g_color};",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
            "QMenuBar::item::!selected {",
            f"  color: {DTheme.g_color};",
            "}",
        ]
        self.menu = [
            "QMenu {",
            f"  border: 1px solid {DTheme.g_border_color};",
            f"  background-color: {DTheme.g_bg_color};",
            f"  color: {DTheme.g_color};",
            "}",
            "QMenu::icon {",
            "  padding: 0px 4px 0px 4px;",
            "}",
            "QMenu::item {",
            "  padding: 4px 12px 4px 8px;",
            "  margin-left: 0px;",
            "}",
            "QMenu::item::selected {",
            f"  color: {DTheme.g_color}",
            f"  background-color: {DTheme.g_bg_color};",
            "  margin-left: 0px;",
            f"  selection-background-color: {DTheme.g_select_bg_color};",
            "}",
            "QMenu::indicator:checked {",
            "  background-repeat: None;",
            "  padding: 2px 2px 2px 2px;",
            "  width: 12px;",
            "  height: 12px;",
            "}",
            "QMenu::item::disabled {",
            f"  color: {DTheme.g_color};",
            f"  background-color: {DTheme.g_bg_color};",
            "}",
            "QMenu::separator {",
            "  margin-top: 2px;",
            "  margin-bottom: 2px;",
            f"  border-top: 2px solid {DTheme.g_border_color};",
            "  margin: 0px;",
            "}",
        ]
        self.x = [
            "",
            "",
        ]
        self.x = [
            "",
            "",
        ]

    def theme(self):
        content = ""
        i = 0
        for attr, value in self.__dict__.items():
            if i > 4:
                continue
            i += 1
            if isinstance(value, list):
                content += "\n".join(value)
            content += "\n"
        return content


if __name__ == "__main__":
    b = DTheme()
    print(b.theme())
