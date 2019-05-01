from nine import str
from Qt import QtCore

from PyFlow.UI.Tool.Tool import DockTool


class DockToolTest(DockTool):
    """docstring for AlignBottomTool."""
    def __init__(self, parent=None):
        super(DockToolTest, self).__init__(parent)

    @staticmethod
    def defaultDockArea():
        return QtCore.Qt.TopDockWidgetArea

    @staticmethod
    def showOnStartup():
        return False

    @staticmethod
    def toolTip():
        return "Test dock tool tooltip"

    @staticmethod
    def name():
        return str("Test dock tool")