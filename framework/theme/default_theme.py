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
    g_bg_d_color = "#3b414d"  # bg_board
    g_bg_s_color = "#3e4451"  # bg_select
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
        self.all0 = Gss("QWidget")
        self.all0.setv(f"background-color: {DTheme.g_bg_color};")
        self.all0.setv(f"color: {DTheme.g_color};")

        self.btn0 = Gss("QPushButton")
        self.btn0.setv("border: none;")
        self.btn0.setv("border-radius: none;")
        self.btn0.setv(f"background-color: {DTheme.g_bg_color};")
        self.btn0.setv("padding: 0;")
        self.btn0.setv(f"background-color: {DTheme.g_hover_bg_color};", k="hover")
        self.btn0.setv(f"background-color: {DTheme.g_hover_bg_color};", k="pressed")

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

        self.fdig = Gss("QFileDialog")
        self.fdig.setv(f"background-color:{DTheme.g_bg_color};")

        self.hdv0 = Gss("QHeaderView")
        self.hdv0.setv(f"color:{DTheme.g_color};")
        self.hdv0.setv(f"background-color:{DTheme.g_bg_color};")
        self.hdv0.setv(f"selection-color:{DTheme.g_color};")
        self.hdv0.setv(f"selection-background-color:{DTheme.g_bg_color};")

        self.hdvs = Gss("QHeaderView::section")
        self.hdvs.setv(f"border: none;")
        self.hdvs.setv(f"color:{DTheme.g_color};")
        self.hdvs.setv(f"background-color:{DTheme.g_bg_color};")

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
        self.liv = Gss("QListView")
        self.liv.setv(f"color: {DTheme.g_color};")
        self.liv.setv(f"background: {DTheme.g_bg_color};")

        self.lit = Gss("QListView::item")
        self.lit.setv(f"color: {DTheme.g_color};")
        self.lit.setv(f"background: {DTheme.g_bg_color};")

        self.let = Gss("QLineEdit")
        self.let.setv(f"color: {DTheme.g_color};")
        self.let.setv(f"background: {DTheme.g_bg_color};")
        self.let.setv("outline: none;")
        self.let.setv(f"border: 1px solid {DTheme.g_bg_d_color};")
        self.let.setv(f"border: 1px solid {DTheme.g_bg_d_color};")
        self.let.setv(f'font-family: "SF Mono SC";')
        self.let.setv(f"font-size: 12pt;")

        # 选中文本的背景色
        self.let.setv(f"selection-background-color: {DTheme.g_bg_s_color};")
        self.let.setv(f"selection-color: {DTheme.g_color};")
        # 只读状态
        self.let.setv(f"color: {DTheme.g_color};", k="read-only")
        self.let.setv(f"background-color: {DTheme.g_bg_d_color};", k="read-only")
        # 禁用状态
        self.let.setv(f"color: {DTheme.g_color};", k="disabled")
        self.let.setv(f"background-color: {DTheme.g_bg_d_color};", k="disabled")

        self.scla = Gss("QScrollArea")
        self.scla.setv("border: none;")

        self.sclb = Gss("QScrollBar")
        # vertical
        self.sclb.setv("border: none;", k="vertical")
        self.sclb.setv(f"background-color: {DTheme.g_bg_color};", k="vertical")
        self.sclb.setv("width: 10px;", k="vertical")
        self.sclb.setv("margin: 0px 0px 0px 0px;", k="vertical")
        # horizontal
        self.sclb.setv("border: none;", k="horizontal")
        self.sclb.setv(f"background-color: {DTheme.g_bg_color};", k="horizontal")
        self.sclb.setv("width: 10px;", k="horizontal")
        self.sclb.setv("margin: 0px 0px 0px 0px;", k="horizontal")

        self.sclh = Gss("QScrollBar::handle")
        # vertical
        self.sclh.setv("border: none;", k="vertical")
        self.sclh.setv(f"background-color: {DTheme.g_bg_d_color};", k="vertical")
        self.sclb.setv("min-width: 8px;", k="vertical")
        # horizontal
        self.sclh.setv("border: none;", k="horizontal")
        self.sclh.setv(f"background-color: {DTheme.g_bg_d_color};", k="horizontal")
        self.sclb.setv("min-width: 8px;", k="horizontal")
        # sub-page
        self.scl1 = Gss("QScrollBar::sub-page")
        self.scl1.setv(f"background-color: {DTheme.g_bg_color};", k="vertical")
        self.scl1.setv(f"background-color: {DTheme.g_bg_color};", k="horizontal")
        self.scl2 = Gss("QScrollBar::add-page")
        # add-page
        self.scl2.setv(f"background-color: {DTheme.g_bg_color};", k="vertical")
        self.scl2.setv(f"background-color: {DTheme.g_bg_color};", k="horizontal")
        # sub-line
        self.scl3 = Gss("QScrollBar::sub-line")
        self.scl3.setv(f"background-color: {DTheme.g_bg_color};", k="vertical")
        self.scl3.setv(f"background-color: {DTheme.g_bg_color};", k="horizontal")
        # add-line
        self.scl4 = Gss("QScrollBar::add-line")
        self.scl4.setv(f"background-color: {DTheme.g_bg_color};", k="vertical")
        self.scl4.setv(f"background-color: {DTheme.g_bg_color};", k="horizontal")

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

        self.trvv = Gss("QTreeView")
        self.trvv.setv(f"color: {DTheme.g_color};")
        self.trvv.setv(f"background: {DTheme.g_bg_color};")

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
