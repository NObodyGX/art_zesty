from collections import OrderedDict


class Gss(object):
    def __init__(self, name: str):
        self.name = name
        self.attr = OrderedDict()

    def setv(self, v: str, k=""):
        if k not in self.attr:
            self.attr[k] = []
        self.attr[k].append(v)

    def __str__(self) -> str:
        a = []
        for k, v in self.attr.items():
            key = f"{self.name}"
            if k:
                key = f"{self.name}:{k}"
            a.append(f"{key}{{")
            for vv in v:
                a.append(f"  {vv}")
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
        self.wi = Gss("QWidget")
        self.wi.setv(f"background-color: {DTheme.g_bg_color};")
        self.wi.setv(f"color: {DTheme.g_color};")

        self.btn = Gss("QPushButton")
        self.btn.setv("border: none;")
        self.btn.setv("border-radius: none;")
        self.btn.setv(f"background-color: {DTheme.g_bg_color};")
        self.btn.setv("padding: 0;")
        self.btn.setv(f"background-color: {DTheme.g_hover_bg_color};", k="hover")
        self.btn.setv(f"background-color: {DTheme.g_hover_bg_color};", k="pressed")

        self.btn1 = Gss("GTitleButton")
        self.btn1.setv("background-color: transparent;")
        self.btn2 = Gss("GTMinButton")
        self.btn2.setv("background-color: transparent;")
        self.btn2.setv(f"color: {DTheme.g_min_color};", k="hover")
        self.btn2.setv(f"background-color: {DTheme.g_min_color};", k="hover")
        self.btn2.setv(f"color: {DTheme.g_min_color};", k="pressed")
        self.btn2.setv(f"background-color: {DTheme.g_min_color};", k="pressed")

        self.btn3 = Gss("GTMaxButton")
        self.btn3.setv("background-color: transparent;")
        self.btn3.setv(f"color: {DTheme.g_max_color};", k="hover")
        self.btn3.setv(f"background-color: {DTheme.g_max_color};", k="hover")
        self.btn3.setv(f"color: {DTheme.g_max_color};", k="pressed")
        self.btn3.setv(f"background-color: {DTheme.g_max_color};", k="pressed")

        self.btn4 = Gss("GTOffButton")
        self.btn4.setv("background-color: transparent;")
        self.btn4.setv(f"color: {DTheme.g_off_color};", k="hover")
        self.btn4.setv(f"background-color: {DTheme.g_off_color};", k="hover")
        self.btn4.setv(f"color: {DTheme.g_off_d_color};", k="pressed")
        self.btn4.setv(f"background-color: {DTheme.g_off_d_color};", k="pressed")

        self.btn5 = Gss("GOKButton")
        self.btn5.setv("border: none;")
        self.btn5.setv(f"background-color: {DTheme.g_ok_color};")
        self.btn5.setv("border-radius: 4px;")

        self.btn6 = Gss("GNOButton")
        self.btn6.setv("border: none;")
        self.btn6.setv(f"background-color: {DTheme.g_no_color};")
        self.btn6.setv("border-radius: 4px;")

        self.btn7 = Gss("GCheckButton")
        self.btn7.setv("border: none;")
        self.btn7.setv("background-color: transparent;")
        # self.btn7.setv("image: url(:/res/icon/common/checkbox.svg);")
        self.btn7.setv("border-radius: 4px;")
        self.btn7.setv("border: none;", k="checked")
        self.btn7.setv("background-color: transparent;", k="checked")
        # self.btn7.setv("image: url(:/res/icon/common/checkbox_yes.svg);", k="checked")
        self.btn7.setv("background-color: transparent;", k="hover")

        self.btn8 = Gss("GGridLabelButton")
        self.btn8.setv(f"border: 1px solid {DTheme.g_color};")
        self.btn8.setv(f"background-color: {DTheme.g_bg_color};")
        self.btn8.setv(f"background-color: {DTheme.g_bg_d_color};", k="hover")
        self.btn8.setv(f"border: 1px solid {DTheme.g_border_color};", k="hover")
        self.btn8.setv(f"background-color: {DTheme.g_max_color};", k="pressed")
        self.btn8.setv(f"border: 1px solid {DTheme.g_border_color};", k="pressed")

        self.btn9 = Gss("GOffButton")
        self.btn9.setv(f"background-color: {DTheme.g_off_color};")
        self.btn9.setv(f"color: {DTheme.g_off_color};", k="hover")
        self.btn9.setv(f"background-color: {DTheme.g_off_color};", k="hover")
        self.btn9.setv(f"color: {DTheme.g_off_d_color};", k="pressed")
        self.btn9.setv(f"background-color: {DTheme.g_off_d_color};", k="pressed")

        # self.combobox = [
        #     "QComboBox {",
        #     "  height: 42px;",
        #     "  border: none;",
        #     f"  color: {DTheme.g_color};",
        #     "  font-size: 12px;",
        #     "  padding-left: 8px;",
        #     "  padding-right: 8px;",
        #     "  /*** 用于控制 qcombobox 的显示方式，包含 0 和 1 ***/",
        #     "  combobox-popup: 0;",
        #     "  border-radius: 0;",
        #     "  background: transparent;",
        #     "}",
        #     "QComboBox:hover {",
        #     "  background: transparent;",
        #     "  border: none;",
        #     "}",
        #     "QComboBox:focus {",
        #     "  border: none;",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        #     "/*** combox 点击样式 ***/",
        #     "QComboBox:on {",
        #     "  border: none;",
        #     "  background: transparent;",
        #     "  padding-left: 8px;",
        #     "}",
        #     "QComboBox::drop-down {",
        #     "  border: 0px;",
        #     "}",
        #     "/*** 下拉箭头样式 ***/",
        #     "QComboBox::down-arrow {",
        #     # "  image: url(:/res/icon/common/icon_arrow_down.svg);",
        #     "  padding-right: 8px;",
        #     "}",
        #     "QComboBox::down-arrow:on {",
        #     # "  image: url(:/res/icon/common/icon_arrow_down.svg);",
        #     "  padding-right: 8px;",
        #     "}",
        #     "/*** 下拉框的样式 ***/",
        #     "QComboBox QAbstractItemView {",
        #     "  border: none;",
        #     "  border-top: none;",
        #     "  outline: none;",
        #     "}",
        #     "/*** 下拉后下拉项的样式 ***/",
        #     "QComboBox QAbstractItemView::item {",
        #     "  min-width: 110px;",
        #     "  min-height: 32px;",
        #     "  font-size: 16px;",
        #     f"  color: {DTheme.g_color};",
        #     f"  background: {DTheme.g_bg_color};",
        #     "  padding-left: 4px;",
        #     "  padding-right: 0px;",
        #     "}",
        #     "QComboBox QAbstractItemView::item:hover:!selected {",
        #     f"  background: {DTheme.g_bg_color};",
        #     "  padding-left: 4px;",
        #     f"  border-left: 2px solid {DTheme.g_color};",
        #     "}",
        #     "QComboBox QAbstractItemView::item:selected {",
        #     f"  background: {DTheme.g_select_bg_color};",
        #     "  padding-left: 4px;",
        #     "}",
        # ]
        # self.checkbox = [
        #     "QCheckBox {",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        # ]

        # self.label = []
        # self.label_ext = [
        #     "GNumberLabel {",
        #     f"  color: {DTheme.g_color};",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        # ]

        # self.list_widget = [
        #     "QListWidget {",
        #     f"  background: {DTheme.g_bg_color};",
        #     "  border: none;",
        #     "  outline: none;",
        #     "}",
        # ]
        # self.list_widget_item = [
        #     "QListWidget::item {",
        #     "}",
        #     "QListWidget::item:focus {",
        #     f"  border-left: 3px solid {DTheme.g_color};",
        #     "}",
        #     "QListWidget::item:hover {",
        #     f"  background: {DTheme.g_hover_bg_color};",
        #     "}",
        #     "QListWidget::item::selected {",
        #     f"  background: {DTheme.g_select_bg_color};",
        #     f"  border-left: 3px solid {DTheme.g_left_select_color};",
        #     "}",
        # ]

        # self.line_edit = [
        #     "QLineEdit {",
        #     "  background: transparent;",
        #     "}",
        # ]

        # self.scroll_area = [
        #     "QScrollArea {",
        #     "  border: none;",
        #     "}",
        # ]

        # self.scroll_bar = [
        #     "QScrollBar:vertical {",
        #     "  border: none;",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "  width: 10px;",
        #     "  margin: 0px 0px 0px 0px;",
        #     "}",
        #     "QScrollBar::handle:vertical {",
        #     "  border: none;",
        #     f"  background-color: {DTheme.g_bg_d_color};",
        #     "  min-width: 8px;",
        #     "QScrollBar::sub-page:vertical,",
        #     "QScrollBar::add-page:vertical {",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        #     "QScrollBar::sub-line:vertical,",
        #     "QScrollBar::add-line:vertical {",
        #     f"  height: 0px;",
        #     "}",
        #     "QScrollBar:horizontal {",
        #     "  border: none;",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "  width: 10px;",
        #     "  margin: 0px 0px 0px 0px;",
        #     "}",
        #     "QScrollBar::handle:horizontal {",
        #     "  border: none;",
        #     f"  background-color: {DTheme.g_bg_d_color};",
        #     "  min-width: 8px;",
        #     "QScrollBar::sub-page:horizontal,",
        #     "QScrollBar::add-page:horizontal {",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        #     "QScrollBar::sub-line:horizontal,",
        #     "QScrollBar::add-line:horizontal {",
        #     f"  height: 0px;",
        #     "}",
        # ]

        # self.slider = [
        #     "QSlider::groove:horizontal{ ",
        #     "  height: 10px;",
        #     "  left: 0px;",
        #     "  right: 0px;",
        #     "  border: none;",
        #     f"  background: {DTheme.g_bg_color};",
        #     "}",
        #     "QSlider::handle:horizontal{ ",
        #     "  width:  10px;",
        #     "  height: 10px;",
        #     "  border-image: none;",
        #     "QSlider::sub-page:horizontal{",
        #     "  background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00dbde, stop:1 #f902ff);;}",
        #     "}",
        # ]

        # self.tooltip = [
        #     "QToolTip {",
        #     "  min-width:140;",
        #     f"  border: 1px solid {DTheme.g_border_color};"
        #     "  margin: 0px;"
        #     "  padding: 0px 4px 0px 4px;"
        #     f"  color: {DTheme.g_color};",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "}",
        # ]

        # self.menu_bar = [
        #     "QMenuBar {",
        #     f"  color: {DTheme.g_color};",
        #     "  border: none;",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "}",
        #     "QMenuBar::item {",
        #     f"  color: {DTheme.g_color};",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "}",
        #     "QMenuBar::item::selected {",
        #     f"  color: {DTheme.g_color};",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "}",
        #     "QMenuBar::item::!selected {",
        #     f"  color: {DTheme.g_color};",
        #     "}",
        # ]
        # self.menu = [
        #     "QMenu {",
        #     f"  border: 1px solid {DTheme.g_border_color};",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     f"  color: {DTheme.g_color};",
        #     "}",
        #     "QMenu::icon {",
        #     "  padding: 0px 4px 0px 4px;",
        #     "}",
        #     "QMenu::item {",
        #     "  padding: 4px 12px 4px 8px;",
        #     "  margin-left: 0px;",
        #     "}",
        #     "QMenu::item::selected {",
        #     f"  color: {DTheme.g_color}",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "  margin-left: 0px;",
        #     f"  selection-background-color: {DTheme.g_select_bg_color};",
        #     "}",
        #     "QMenu::indicator:checked {",
        #     "  background-repeat: None;",
        #     "  padding: 2px 2px 2px 2px;",
        #     "  width: 12px;",
        #     "  height: 12px;",
        #     "}",
        #     "QMenu::item::disabled {",
        #     f"  color: {DTheme.g_color};",
        #     f"  background-color: {DTheme.g_bg_color};",
        #     "}",
        #     "QMenu::separator {",
        #     "  margin-top: 2px;",
        #     "  margin-bottom: 2px;",
        #     f"  border-top: 2px solid {DTheme.g_border_color};",
        #     "  margin: 0px;",
        #     "}",
        # ]

    def theme(self):
        content = ""
        for value in self.__dict__.values():
            content += f"{str(value)}\n"
        return content


if __name__ == "__main__":
    b = DTheme()
    print(b.theme())
