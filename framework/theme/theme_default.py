from collections import OrderedDict


class Gss(object):
    def __init__(self, name: str):
        self.name = name
        self.attr = OrderedDict()

    def setv(self, v: str, k="", end_suffix=True):
        if end_suffix and not v.endswith(";"):
            v += ";"
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


class GDefaultTheme(object):
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
        self.widget = Gss("QWidget")
        self.widget.setv(f"background-color: {GDefaultTheme.g_bg_color}")
        self.widget.setv(f"color: {GDefaultTheme.g_color}")

        self.button = Gss("QPushButton")
        self.button.setv("border: none")
        self.button.setv("border-radius: none")
        self.button.setv(f"background-color: {GDefaultTheme.g_bg_color}")
        self.button.setv("padding: 0")
        self.button.setv(
            f"background-color: {GDefaultTheme.g_hover_bg_color}", k="hover"
        )
        self.button.setv(
            f"background-color: {GDefaultTheme.g_hover_bg_color}", k="pressed"
        )

        self.btn1 = Gss("GTitleButton")
        self.btn1.setv("background-color: transparent")

        self.btn2 = Gss("GTMinButton")
        self.btn2.setv("background-color: transparent")
        self.btn2.setv(f"color: {GDefaultTheme.g_min_color}", k="hover")
        self.btn2.setv(f"background-color: {GDefaultTheme.g_min_color}", k="hover")
        self.btn2.setv(f"color: {GDefaultTheme.g_min_color}", k="pressed")
        self.btn2.setv(f"background-color: {GDefaultTheme.g_min_color}", k="pressed")

        self.btn3 = Gss("GTMaxButton")
        self.btn3.setv("background-color: transparent")
        self.btn3.setv(f"color: {GDefaultTheme.g_max_color}", k="hover")
        self.btn3.setv(f"background-color: {GDefaultTheme.g_max_color}", k="hover")
        self.btn3.setv(f"color: {GDefaultTheme.g_max_color}", k="pressed")
        self.btn3.setv(f"background-color: {GDefaultTheme.g_max_color}", k="pressed")

        self.btn4 = Gss("GTOffButton")
        self.btn4.setv("background-color: transparent")
        self.btn4.setv(f"color: {GDefaultTheme.g_off_color}", k="hover")
        self.btn4.setv(f"background-color: {GDefaultTheme.g_off_color}", k="hover")
        self.btn4.setv(f"color: {GDefaultTheme.g_off_d_color}", k="pressed")
        self.btn4.setv(f"background-color: {GDefaultTheme.g_off_d_color}", k="pressed")

        self.btn5 = Gss("GOKButton")
        self.btn5.setv("border: none")
        self.btn5.setv(f"background-color: {GDefaultTheme.g_ok_color}")
        self.btn5.setv("border-radius: 4px")

        self.btn6 = Gss("GNOButton")
        self.btn6.setv("border: none")
        self.btn6.setv(f"background-color: {GDefaultTheme.g_no_color}")
        self.btn6.setv("border-radius: 4px")

        self.btn7 = Gss("GCheckButton")
        self.btn7.setv("border: none")
        self.btn7.setv("background-color: transparent")
        # self.btn7.setv("image: url(:/res/icon/common/checkbox.svg)")
        self.btn7.setv("border-radius: 4px")
        self.btn7.setv("border: none", k="checked")
        self.btn7.setv("background-color: transparent", k="checked")
        # self.btn7.setv("image: url(:/res/icon/common/checkbox_yes.svg)", k="checked")
        self.btn7.setv("background-color: transparent", k="hover")

        self.btn8 = Gss("GGridLabelButton")
        self.btn8.setv(f"border: 1px solid {GDefaultTheme.g_color}")
        self.btn8.setv(f"background-color: {GDefaultTheme.g_bg_color}")
        self.btn8.setv(f"background-color: {GDefaultTheme.g_bg_d_color}", k="hover")
        self.btn8.setv(f"border: 1px solid {GDefaultTheme.g_border_color}", k="hover")
        self.btn8.setv(f"background-color: {GDefaultTheme.g_max_color}", k="pressed")
        self.btn8.setv(f"border: 1px solid {GDefaultTheme.g_border_color}", k="pressed")

        self.btn9 = Gss("GOffButton")
        self.btn9.setv(f"background-color: {GDefaultTheme.g_off_color}")
        self.btn9.setv(f"color: {GDefaultTheme.g_off_color}", k="hover")
        self.btn9.setv(f"background-color: {GDefaultTheme.g_off_color}", k="hover")
        self.btn9.setv(f"color: {GDefaultTheme.g_off_d_color}", k="pressed")
        self.btn9.setv(f"background-color: {GDefaultTheme.g_off_d_color}", k="pressed")

        self.combox = Gss("QComboBox")
        self.combox.setv("background: transparent")
        self.combox.setv("height: 42px")
        self.combox.setv("border: none")
        self.combox.setv(f"color: {GDefaultTheme.g_color}")
        self.combox.setv("font-size: 12px")
        self.combox.setv("padding-left: 8px")
        self.combox.setv("padding-right: 8px")
        # 用于控制 qcombobox 的显示方式，包含 0 和 1
        self.combox.setv("combobox-popup: 0")
        self.combox.setv("border-radius: 0")
        self.combox.setv("background: transparent")
        # combox 悬浮样式
        self.combox.setv("background: transparent", k="hover")
        self.combox.setv("border: none", k="hover")
        # combox 获取焦点样式
        self.combox.setv("border: none", k="focus")
        self.combox.setv(f"background: {GDefaultTheme.g_bg_color}", k="focus")
        # combox 点击样式
        self.combox.setv("background: transparent", k="on")
        self.combox.setv("border: none", k="on")
        self.combox.setv("padding-left: 8px", k="on")
        self.combox.setv("border: none", k="drop-down")
        # 下拉箭头样式
        self.combox.setv(
            "image: url(:/res/icon/common/icon_arrow_down.svg)", k="drop-arrow"
        )
        self.combox.setv("padding-right: 8px", k="drop-arrow")
        # self.comb.setv("image: url(:/res/icon/common/icon_arrow_down.svg)", k="drop-arrow:on")
        self.combox.setv("padding-right: 8px", k="drop-arrow:on")
        # 下拉框的样式
        self.combox_ab_view = Gss("QComboBox QAbstractItemView")
        self.combox_ab_view.setv("border: none")
        self.combox_ab_view.setv("border-top: none")
        self.combox_ab_view.setv("outline: none")
        # 下拉项的样式
        self.combox_ab_item = Gss("QComboBox QAbstractItemView::item")
        self.combox_ab_item.setv("min-width: 110px")
        self.combox_ab_item.setv("min-height: 32px")
        self.combox_ab_item.setv("font-size: 16px")
        self.combox_ab_item.setv(f"color: {GDefaultTheme.g_color}")
        self.combox_ab_item.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.combox_ab_item.setv("padding-left: 4px")
        self.combox_ab_item.setv("padding-right: 0px")
        self.combox_ab_item.setv(
            f"background: {GDefaultTheme.g_bg_color}", k="hover:!selected"
        )
        self.combox_ab_item.setv("padding-left: 4px", k="hover:!selected")
        self.combox_ab_item.setv(
            f"border-left: 2px solid {GDefaultTheme.g_color}", k="hover:!selected"
        )
        self.combox_ab_item.setv(
            f"background: {GDefaultTheme.g_select_bg_color}", k="selected"
        )
        self.combox_ab_item.setv(f"padding-left: 4px", k="selected")

        self.checkbox = Gss("QCheckBox")
        self.checkbox.setv(f"color: {GDefaultTheme.g_color}")

        self.file_dialog = Gss("QFileDialog")
        self.file_dialog.setv(f"background-color:{GDefaultTheme.g_bg_color}")

        self.header_view = Gss("QHeaderView")
        self.header_view.setv(f"color:{GDefaultTheme.g_color}")
        self.header_view.setv(f"background-color:{GDefaultTheme.g_bg_color}")
        self.header_view.setv(f"selection-color:{GDefaultTheme.g_color}")
        self.header_view.setv(f"selection-background-color:{GDefaultTheme.g_bg_color}")

        self.header_view_section = Gss("QHeaderView::section")
        self.header_view_section.setv(f"border: none")
        self.header_view_section.setv(f"color:{GDefaultTheme.g_color}")
        self.header_view_section.setv(f"background-color:{GDefaultTheme.g_bg_color}")

        self.lab1 = Gss("GNumberLabel")
        self.lab1.setv(f"color:{GDefaultTheme.g_color}")
        self.lab1.setv(f"background:{GDefaultTheme.g_bg_color}")

        self.list_widget = Gss("QListWidget")
        self.list_widget.setv(f"color:{GDefaultTheme.g_color}")
        self.list_widget.setv(f"background:{GDefaultTheme.g_bg_color}")
        self.list_widget.setv(f"border: none")
        self.list_widget.setv(f"outline: none")

        self.list_widget_item = Gss("QListWidget::item")
        self.list_widget_item.setv(
            f"border-left: 3px solid {GDefaultTheme.g_color}", k="focus"
        )
        self.list_widget_item.setv(
            f"background: {GDefaultTheme.g_hover_bg_color}", k="hover"
        )
        self.list_widget_item.setv(
            f"background: {GDefaultTheme.g_select_bg_color}", k="selected"
        )
        self.list_widget_item.setv(
            f"border-left: 3px solid {GDefaultTheme.g_left_select_color}", k="selected"
        )

        self.list_view = Gss("QListView")
        self.list_view.setv(f"color: {GDefaultTheme.g_color}")
        self.list_view.setv(f"background: {GDefaultTheme.g_bg_color}")

        self.list_view_item = Gss("QListView::item")
        self.list_view_item.setv(f"color: {GDefaultTheme.g_color}")
        self.list_view_item.setv(f"background: {GDefaultTheme.g_bg_color}")

        self.line_edit = Gss("QLineEdit")
        self.line_edit.setv(f"color: {GDefaultTheme.g_color}")
        self.line_edit.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.line_edit.setv("outline: none")
        self.line_edit.setv(f"border: 1px solid {GDefaultTheme.g_bg_d_color}")
        self.line_edit.setv(f"border: 1px solid {GDefaultTheme.g_bg_d_color}")
        self.line_edit.setv(f'font-family: "SF Mono SC"')
        self.line_edit.setv(f"font-size: 12pt")

        # 选中文本的背景色
        self.line_edit.setv(f"selection-background-color: {GDefaultTheme.g_bg_s_color}")
        self.line_edit.setv(f"selection-color: {GDefaultTheme.g_color}")
        # 只读状态
        self.line_edit.setv(f"color: {GDefaultTheme.g_color}", k="read-only")
        self.line_edit.setv(
            f"background-color: {GDefaultTheme.g_bg_d_color}", k="read-only"
        )
        # 禁用状态
        self.line_edit.setv(f"color: {GDefaultTheme.g_color}", k="disabled")
        self.line_edit.setv(
            f"background-color: {GDefaultTheme.g_bg_d_color}", k="disabled"
        )

        self.scroll_area = Gss("QScrollArea")
        self.scroll_area.setv("border: none")

        self.scroll_bar = Gss("QScrollBar")
        # vertical
        self.scroll_bar.setv("border: none", k="vertical")
        self.scroll_bar.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="vertical"
        )
        self.scroll_bar.setv("width: 10px", k="vertical")
        self.scroll_bar.setv("margin: 0px 0px 0px 0px", k="vertical")
        # horizontal
        self.scroll_bar.setv("border: none", k="horizontal")
        self.scroll_bar.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )
        self.scroll_bar.setv("width: 10px", k="horizontal")
        self.scroll_bar.setv("margin: 0px 0px 0px 0px", k="horizontal")

        self.scroll_bar_handle = Gss("QScrollBar::handle")
        # vertical
        self.scroll_bar_handle.setv("border: none", k="vertical")
        self.scroll_bar_handle.setv(
            f"background-color: {GDefaultTheme.g_bg_d_color}", k="vertical"
        )
        self.scroll_bar.setv("min-width: 8px", k="vertical")
        # horizontal
        self.scroll_bar_handle.setv("border: none", k="horizontal")
        self.scroll_bar_handle.setv(
            f"background-color: {GDefaultTheme.g_bg_d_color}", k="horizontal"
        )
        self.scroll_bar.setv("min-width: 8px", k="horizontal")
        # sub-page
        self.scroll_bar_subpage = Gss("QScrollBar::sub-page")
        self.scroll_bar_subpage.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="vertical"
        )
        self.scroll_bar_subpage.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )
        # add-page
        self.scroll_bar_addpage = Gss("QScrollBar::add-page")
        self.scroll_bar_addpage.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="vertical"
        )
        self.scroll_bar_addpage.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )
        # sub-line
        self.scroll_bar_subline = Gss("QScrollBar::sub-line")
        self.scroll_bar_subline.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="vertical"
        )
        self.scroll_bar_subline.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )
        # add-line
        self.scroll_bar_addline = Gss("QScrollBar::add-line")
        self.scroll_bar_addline.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="vertical"
        )
        self.scroll_bar_addline.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )

        self.slide_groove = Gss("QSlider::groove")
        self.slide_groove.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="horizontal"
        )
        self.slide_groove.setv("height: 10px", k="horizontal")
        self.slide_groove.setv("left: 0px", k="horizontal")
        self.slide_groove.setv("right: 0px", k="horizontal")
        self.slide_groove.setv("border: none", k="horizontal")
        self.slide_groove.setv(
            f"background: {GDefaultTheme.g_bg_color}", k="horizontal"
        )

        self.slide_handle = Gss("QSlider::handle")
        self.slide_handle.setv("width: 10px", k="horizontal")
        self.slide_handle.setv("height: 10px", k="horizontal")
        self.slide_handle.setv("border-image: none", k="horizontal")

        self.slide_subpage = Gss("QSlider::sub-page")
        self.slide_subpage.setv(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00dbde, stop:1 #f902ff);;}",
            k="horizontal",
        )

        self.tree_view = Gss("QTreeView")
        self.tree_view.setv(f"color: {GDefaultTheme.g_color}")
        self.tree_view.setv(f"background: {GDefaultTheme.g_bg_color}")

        self.tooltip = Gss("QToolTip")
        self.tooltip.setv(f"color: {GDefaultTheme.g_color}")
        self.tooltip.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.tooltip.setv(f"border: 1px solid {GDefaultTheme.g_border_color}")
        self.tooltip.setv(f"border-radius: 5px")
        self.tooltip.setv(f"padding: 0px 4px 0px 4px")
        self.tooltip.setv(f"margin: 0px")
        self.tooltip.setv("min-width:140")

        self.menu_bar = Gss("QMenuBar")
        self.menu_bar.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.menu_bar.setv(f"color: {GDefaultTheme.g_color}")
        self.menu_bar.setv("border: none")

        self.menu_bar_item = Gss("QMenuBar::item")
        self.menu_bar_item.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.menu_bar_item.setv(f"color: {GDefaultTheme.g_color}")
        self.menu_bar_item.setv(f"background: {GDefaultTheme.g_bg_color}", k="selected")
        self.menu_bar_item.setv(f"color: {GDefaultTheme.g_color}", k="selected")
        self.menu_bar_item.setv(f"color: {GDefaultTheme.g_color}", k="!selected")

        self.menu = Gss("QMenu")
        self.menu.setv(f"background: {GDefaultTheme.g_bg_color}")
        self.menu.setv(f"border: 1px solid {GDefaultTheme.g_border_color}")
        self.menu.setv(f"color: {GDefaultTheme.g_color}")

        self.menu_icon = Gss("QMenu::icon")
        self.menu_icon.setv("padding: 0px 4px 0px 4px")

        self.menu_item = Gss("QMenu::item")
        self.menu_item.setv("padding: 4px 12px 4px 8px")
        self.menu_item.setv("margin-left: 0px")
        self.menu_item.setv(
            f"background-color: {GDefaultTheme.g_bg_color}", k="selected"
        )
        self.menu_item.setv(f"color: {GDefaultTheme.g_color}", k="selected")
        self.menu_item.setv("margin-left: 0px", k="selected")
        self.menu_item.setv(
            f"selection-background-color: {GDefaultTheme.g_select_bg_color}",
            k="selected",
        )
        self.menu_item.setv(f"background: {GDefaultTheme.g_bg_color}", k="disabled")
        self.menu_item.setv(f"color: {GDefaultTheme.g_color}", k="disabled")

        self.menu_separator = Gss("QMenu::separator")
        self.menu_separator.setv("margin-top: 2px")
        self.menu_separator.setv("margin-bottom: 2px")
        self.menu_separator.setv("margin: 0px")
        self.menu_separator.setv(
            f"border-top: 2px solid {GDefaultTheme.g_border_color}"
        )

        self.menu_indicator = Gss("QMenu::indicator")
        self.menu_indicator.setv("background-repeat: None", k="checked")
        self.menu_indicator.setv("padding: 2px 2px 2px 2px", k="checked")
        self.menu_indicator.setv("height: 12px", k="checked")
        self.menu_indicator.setv("width: 12px", k="checked")

    def theme(self):
        content = ""
        for value in self.__dict__.values():
            content += f"{str(value)}\n"
        return content


if __name__ == "__main__":
    b = GDefaultTheme()
    print(b.theme())
