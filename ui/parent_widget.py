# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'versionitem_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_ParentWidget(object):
    def setupUi(self, ParentWidget):
        ParentWidget.setObjectName("ParentWidget")
        ParentWidget.resize(327, 98)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParentWidget.sizePolicy().hasHeightForWidth())
        ParentWidget.setSizePolicy(sizePolicy)
        ParentWidget.setMouseTracking(True)
        self.horizontalLayout = QtGui.QHBoxLayout(ParentWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.box = QtGui.QFrame(ParentWidget)
        self.box.setFrameShape(QtGui.QFrame.NoFrame)
        self.box.setFrameShadow(QtGui.QFrame.Raised)
        self.box.setObjectName("box")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.box)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.thumbnail = QtGui.QLabel(self.box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy)
        self.thumbnail.setMinimumSize(QtCore.QSize(84, 40))
        self.thumbnail.setMaximumSize(QtCore.QSize(84, 40))
        self.thumbnail.setStyleSheet("background-color: #FFFFFF;")
        self.thumbnail.setText("")
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout_2.addWidget(self.thumbnail)
        self.detailsLayout = QtGui.QVBoxLayout()
        self.detailsLayout.setSpacing(0)
        self.detailsLayout.setObjectName("detailsLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.detailsLayout.addItem(spacerItem)
        self.itemName = QtGui.QLabel(self.box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy)
        self.itemName.setMaximumSize(QtCore.QSize(16777215, 18))
        self.itemName.setTextFormat(QtCore.Qt.AutoText)
        self.itemName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.itemName.setMargin(2)
        self.itemName.setIndent(1)
        self.itemName.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.itemName.setObjectName("itemName")
        self.detailsLayout.addWidget(self.itemName)
        self.child_list = QtGui.QListView(self.box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.child_list.sizePolicy().hasHeightForWidth())
        self.child_list.setSizePolicy(sizePolicy)
        self.child_list.setMouseTracking(True)
        self.child_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.child_list.setFrameShape(QtGui.QFrame.NoFrame)
        self.child_list.setFrameShadow(QtGui.QFrame.Plain)
        self.child_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.child_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.child_list.setAutoScroll(False)
        self.child_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.child_list.setProperty("showDropIndicator", False)
        self.child_list.setDragEnabled(True)
        self.child_list.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.child_list.setIconSize(QtCore.QSize(50, 20))
        self.child_list.setMovement(QtGui.QListView.Static)
        self.child_list.setFlow(QtGui.QListView.LeftToRight)
        self.child_list.setProperty("isWrapping", False)
        self.child_list.setViewMode(QtGui.QListView.IconMode)
        self.child_list.setSelectionRectVisible(False)
        self.child_list.setObjectName("child_list")
        self.detailsLayout.addWidget(self.child_list)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.detailsLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.detailsLayout)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.box)

        self.retranslateUi(ParentWidget)
        QtCore.QMetaObject.connectSlotsByName(ParentWidget)

    def retranslateUi(self, ParentWidget):
        self.itemName.setText(QtGui.QApplication.translate("ParentWidget", "ItemName", None, QtGui.QApplication.UnicodeUTF8))