from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QAbstractItemView


class MemoryWidget(QAbstractItemView):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumSize(200, 20)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor("GREEN"))
        qp.drawRect(0, 0, self.width(), self.height())
        qp.end()
