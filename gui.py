from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from item import *
from file_manager import FileManager

def get_all_groups_in_group(group):
    groups_to_check = [group]
    groups = []
    while len(groups_to_check) > 0:
        g = groups_to_check.pop(0)
        for child in g.children:
            if type(child) is Group:
                groups_to_check.append(child)
                groups.append(child)
    
    return groups

def get_all_groups_in_tree(tree : QTreeWidget):
    
    def nodes_from_tree(tree,nodes=[]):
        if type(tree.obj) is Group:
            nodes.append(tree.obj)
            for i in range(tree.childCount()):
                nodes_from_tree(tree.child(i), nodes)
                
    nodes = []

    for child_index in range(tree.topLevelItemCount()):
        nodes_from_tree(tree.topLevelItem(child_index), nodes)
    
    return nodes

class QTreeWidgetCustomItem(QTreeWidgetItem):

    def __init__(self, strings, stored_object=None):
        super(QTreeWidgetCustomItem, self).__init__(strings)

        self.obj = stored_object

class TaskAddDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.verticalLayout_4 = QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QLabel(self)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.desc_label = QLabel(self)
        self.desc_label.setObjectName("desc_label")
        self.verticalLayout.addWidget(self.desc_label)
        self.state_label = QLabel(self)
        self.state_label.setObjectName("state_label")
        self.verticalLayout.addWidget(self.state_label)
        self.importance_label = QLabel(self)
        self.importance_label.setObjectName("importance_label")
        self.verticalLayout.addWidget(self.importance_label)
        self.difficulty_label = QLabel(self)
        self.difficulty_label.setObjectName("difficulty_label")
        self.verticalLayout.addWidget(self.difficulty_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_lineEdit = QLineEdit(self)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.verticalLayout_2.addWidget(self.name_lineEdit)
        self.desc_lineEdit = QLineEdit(self)
        self.desc_lineEdit.setObjectName("desc_lineEdit")
        self.verticalLayout_2.addWidget(self.desc_lineEdit)
        self.state_comboBox = QComboBox(self)
        self.state_comboBox.setEditable(False)
        self.state_comboBox.setFrame(True)
        self.state_comboBox.setObjectName("state_comboBox")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.state_comboBox)
        self.importance_comboBox = QComboBox(self)
        self.importance_comboBox.setObjectName("importance_comboBox")
        self.importance_comboBox.addItem("")
        self.importance_comboBox.addItem("")
        self.importance_comboBox.addItem("")
        self.importance_comboBox.addItem("")
        self.importance_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.importance_comboBox)
        self.difficulty_comboBox = QComboBox(self)
        self.difficulty_comboBox.setObjectName("difficulty_comboBox")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.difficulty_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line_2 = QFrame(self)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_button = QDialogButtonBox(self)
        self.save_button.setOrientation(Qt.Horizontal)
        self.save_button.setStandardButtons(QDialogButtonBox.Save)
        self.save_button.setCenterButtons(True)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.cancel_button = QDialogButtonBox(self)
        self.cancel_button.setStandardButtons(QDialogButtonBox.Cancel)
        self.cancel_button.setCenterButtons(True)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi()
        self.save_button.accepted.connect(self.accept)
        self.cancel_button.rejected.connect(self.reject)
        self.importance_comboBox.setCurrentIndex(4)
        self.difficulty_comboBox.setCurrentIndex(4)
        self.save_button.setDisabled(True)
        self.name_lineEdit.textChanged.connect(self.disableButton)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Name"))
        self.desc_label.setText(_translate("Dialog", "Description"))
        self.state_label.setText(_translate("Dialog", "State"))
        self.importance_label.setText(_translate("Dialog", "Importance"))
        self.difficulty_label.setText(_translate("Dialog", "Difficulty"))
        self.state_comboBox.setItemText(0, _translate("Dialog", "Not Started"))
        self.state_comboBox.setItemText(1, _translate("Dialog", "In Progress"))
        self.state_comboBox.setItemText(2, _translate("Dialog", "Untested"))
        self.state_comboBox.setItemText(3, _translate("Dialog", "Finished"))
        self.state_comboBox.setItemText(4, _translate("Dialog", "Cancelled"))
        self.state_comboBox.setItemText(5, _translate("Dialog", "Delayed"))
        self.importance_comboBox.setItemText(0, _translate("Dialog", "1"))
        self.importance_comboBox.setItemText(1, _translate("Dialog", "2"))
        self.importance_comboBox.setItemText(2, _translate("Dialog", "3"))
        self.importance_comboBox.setItemText(3, _translate("Dialog", "4"))
        self.importance_comboBox.setItemText(4, _translate("Dialog", "5"))
        self.difficulty_comboBox.setItemText(0, _translate("Dialog", "1"))
        self.difficulty_comboBox.setItemText(1, _translate("Dialog", "2"))
        self.difficulty_comboBox.setItemText(2, _translate("Dialog", "3"))
        self.difficulty_comboBox.setItemText(3, _translate("Dialog", "4"))
        self.difficulty_comboBox.setItemText(4, _translate("Dialog", "5"))

    def disableButton(self):
        if len(self.name_lineEdit.text()) > 0:
            self.save_button.setDisabled(False)
        else:
            self.save_button.setDisabled(True)

class GroupAddDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.verticalLayout_4 = QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QLabel(self)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.desc_label = QLabel(self)
        self.desc_label.setObjectName("desc_label")
        self.verticalLayout.addWidget(self.desc_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_lineEdit = QLineEdit(self)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.verticalLayout_2.addWidget(self.name_lineEdit)
        spacerItem = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.desc_lineEdit = QLineEdit(self)
        self.desc_lineEdit.setObjectName("desc_lineEdit")
        self.verticalLayout_2.addWidget(self.desc_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line_2 = QFrame(self)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_button = QDialogButtonBox(self)
        self.save_button.setEnabled(True)
        self.save_button.setMouseTracking(False)
        self.save_button.setContextMenuPolicy(Qt.NoContextMenu)
        self.save_button.setAcceptDrops(False)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setOrientation(Qt.Horizontal)
        self.save_button.setStandardButtons(QDialogButtonBox.Save)
        self.save_button.setCenterButtons(True)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.cancel_button = QDialogButtonBox(self)
        self.cancel_button.setStandardButtons(QDialogButtonBox.Cancel)
        self.cancel_button.setCenterButtons(True)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi()
        self.save_button.accepted.connect(self.accept)
        self.cancel_button.rejected.connect(self.reject)
        self.save_button.setDisabled(True)
        self.name_lineEdit.textChanged.connect(self.disableButton)
        
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Name"))
        self.desc_label.setText(_translate("Dialog", "Description"))

    def disableButton(self):
        if len(self.name_lineEdit.text()) > 0:
            self.save_button.setDisabled(False)
        else:
            self.save_button.setDisabled(True)

class MoveToDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(400, 81)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.move_to_label = QLabel(self)
        self.move_to_label.setObjectName("move_to_label")
        self.horizontalLayout.addWidget(self.move_to_label)
        self.new_parent_comboBox = QComboBox(self)
        self.new_parent_comboBox.setObjectName("new_parent_comboBox")
        self.horizontalLayout.addWidget(self.new_parent_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.save_button = QDialogButtonBox(self)
        self.save_button.setStandardButtons(QDialogButtonBox.Save)
        self.save_button.setCenterButtons(True)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)

        self.retranslateUi()
        self.save_button.accepted.connect(self.accept)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.move_to_label.setText(_translate("Dialog", "Move To:"))

class Gui(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.filepath = None

        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.app.setStyleSheet(stream.readAll())
        self.dark_theme_enabled = True

        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.main_group = Group("Top Level Item")
        self.tree = QTreeWidget()
        self.tree.setColumnCount(5)
        
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.createContextMenu)
        self.tree.setSortingEnabled(True)
        self.tree.setHeaderLabels(["Name", "State", "Importance", "Difficulty", "Description"])

        header = self.tree.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        bar = self.menuBar()
        file = bar.addMenu("File")
            
        save_as_action = QAction("Save as",self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_as_tree)
        
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_tree)

        open_action = QAction("Open",self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_tree)

        new_action = QAction("New",self)
        new_action.setShortcut("Ctrl+D")
        new_action.triggered.connect(self.new_tree)
        
        file.addAction(save_action)
        file.addAction(save_as_action)
        file.addAction(open_action)
        file.addAction(new_action)

        options = bar.addMenu("Options")
        
        dark_theme_action = QAction('   Use dark theme', self, checkable=True)
        dark_theme_action.setChecked(True)
        dark_theme_action.triggered.connect(self.dark_theme_toggle)
        
        options.addAction(dark_theme_action)

        self.exit_shortcut = QShortcut(QKeySequence("Ctrl+E"), self)
        self.exit_shortcut.activated.connect(self.close_app)
        
        self.layout.addWidget(self.tree)
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.update_display()

    def dark_theme_toggle(self, state):

        if state:
            file = QFile(":/dark.qss")
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            self.app.setStyleSheet(stream.readAll())
        else:
            file = QFile(":/light.qss")
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            self.app.setStyleSheet(stream.readAll())
            
    def close_app(self):
        
        def popup_clicked(i):
            if i.text().lower() == "&yes":
                self.close()
                self.update_display()

                if self.filepath:
                    self.save_tree()

        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("Would you like to close the program?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(popup_clicked)
        msg.exec_()

    def createContextMenu(self, point):

        index = self.tree.indexAt(point)
        menu = QMenu()
        item = None
        
        if index.isValid(): #If right click on an item
            item = self.tree.itemAt(point)
            parent = item.parent().obj if item.parent() is not None else self.main_group

            if type(item.obj) is Group:
                add_group_action = QAction("Add Group", self)
                add_group_action.triggered.connect(lambda: self.add_group(item.obj))
                menu.addAction(add_group_action)

                add_task_action = QAction("Add Task", self)
                add_task_action.triggered.connect(lambda: self.add_task(item.obj))
                menu.addAction(add_task_action)

                menu.addSeparator()

                edit_group_action = QAction("Edit Group", self)
                edit_group_action.triggered.connect(lambda: self.edit_group(item.obj))
                menu.addAction(edit_group_action)

                remove_group_action = QAction("Remove Group", self)
                remove_group_action.triggered.connect(lambda: self.remove_item(parent, item.obj))
                menu.addAction(remove_group_action)
            
            if type(item.obj) is Task:
                edit_task_action = QAction("Edit Task", self)
                edit_task_action.triggered.connect(lambda: self.edit_task(item.obj))
                menu.addAction(edit_task_action)

                remove_task_action = QAction("Remove Task", self)
                remove_task_action.triggered.connect(lambda: self.remove_item(parent, item.obj))
                menu.addAction(remove_task_action)

            move_action = QAction("Move Item", self)
            move_action.triggered.connect(lambda: self.move_item(parent, item.obj))
            menu.addAction(move_action)

            menu.addSeparator()
        else:
            parent = self.main_group

            add_group_action = QAction("Add Group", self)
            add_group_action.triggered.connect(lambda: self.add_group(parent))
            menu.addAction(add_group_action)

            menu.addSeparator()

        #do always
        refresh_action = QAction("Refresh",self)
        refresh_action.triggered.connect(self.update_display)
        menu.addAction(refresh_action)

        menu.exec_(self.tree.mapToGlobal(point))
    
    def update_display(self):
        self.tree.clear()

        items = []
        to_add = []
        for child in self.main_group.children:
            strings = [child.name, None, None, None, child.description]

            if type(child) is Group:
                strings[0] = '\n' + strings[0]
                strings[1] = "\n "
                strings[2] = "\n "
                strings[3] = "\n "

                try:
                    strings[4] = '\n' + strings[4]
                except:
                    strings.append('\n')
            else:
                strings[1] = Task.get_state_short(child.state)
                strings[2] = str(child.importance)
                strings[3] = str(child.difficulty)

            items.append(QTreeWidgetCustomItem(strings, stored_object=child))

            if type(child) is Group:
                to_add.append( (child, items[-1]) )
            
        
        self.tree.insertTopLevelItems(0, items)
        
        for item in items:
            item.setExpanded(True)

        while len(to_add) > 0:
            item = to_add[0]
            items = []
            for child in item[0].children:
                strings = [child.name, None, None, None, child.description]

                if type(child) is Group:
                    strings[0] = '\n' + strings[0]
                    strings[1] = "\n "
                    strings[2] = "\n "
                    strings[3] = "\n "
                    strings[4] = '\n' + strings[4]
                else:
                    strings[1] = Task.get_state_short(child.state)
                    strings[2] = str(child.importance)
                    strings[3] = str(child.difficulty)

                items.append(QTreeWidgetCustomItem(strings, stored_object=child))
                items[-1].setExpanded(True)
                
                if type(child) is Group:
                    to_add.append( (child, items[-1]) )
            
            item[1].addChildren(items)
            for el in items:
                el.setExpanded(True)

            to_add.pop(0)

    def save_tree(self):
        if self.filepath:
            FileManager.save_data(self.main_group, filepath=self.filepath)
        else:
            self.save_as_tree()

    def save_as_tree(self):
        filepath, _ = QFileDialog.getSaveFileName(parent=self, caption="Save To-do List", directory="", filter="Lists (*.pkl);;All Files (*)")
        if filepath:
            FileManager.save_data(self.main_group, filepath=filepath)
            self.filepath = filepath

    def open_tree(self):
        filepath, _ = QFileDialog.getOpenFileName(parent=self, caption="Open To-do List", directory="", filter="Lists (*.pkl);;All Files (*)")
        if filepath:
            self.main_group = FileManager.load_data(filepath=filepath)
            self.update_display()
            self.filepath = filepath

    def new_tree(self):

        if len(self.main_group.children) > 0:
            def popup_clicked(i):
                if i.text().lower() == "&yes":
                    self.save_tree()

            msg = QMessageBox()
            msg.setWindowTitle("Save?")
            msg.setText("Would you like to save the current list?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.buttonClicked.connect(popup_clicked)
            msg.exec_()

        self.main_group = Group("Top Level Item")
        self.update_display()
        self.filepath = None

    def remove_item(self, parent, item_to_remove):
        
        if type(parent) is not Group:
            raise TypeError(f"{repr(parent)} not a Group (Type={type(parent)})")
        if not isinstance(item_to_remove, Item):
            raise TypeError(f"{repr(item_to_remove)} not an Item (Type={type(item_to_remove)})")

        def popup_clicked(i):
            if i.text().lower() == "&yes":
                parent.remove_child(item_to_remove)
                self.update_display()

                if self.filepath:
                    self.save_tree()

        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("Would you like to delete this item?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(popup_clicked)
        msg.exec_()

    def add_group(self, parent):
        if type(parent) is not Group:
            raise TypeError(f"{repr(parent)} not a Group (Type={type(parent)})")

        dialog = GroupAddDialog()
        if dialog.exec_() == QDialog.Accepted:
            new_group = Group(
                name=dialog.name_lineEdit.text(),
                description=dialog.desc_lineEdit.text()
                )

            parent.add_child(new_group)
            self.update_display()

            if self.filepath:
                self.save_tree()

        dialog.deleteLater()
    
    def add_task(self, parent):
        
        if type(parent) is not Group:
            raise TypeError(f"{repr(parent)} not a Group (Type={type(parent)})")

        dialog = TaskAddDialog()
        if dialog.exec_() == QDialog.Accepted:
            new_task = Task(
                name=dialog.name_lineEdit.text(),
                description=dialog.desc_lineEdit.text(),
                state=dialog.state_comboBox.currentIndex(),
                importance=dialog.importance_comboBox.currentIndex() + 1, #index is 0-4 and importance/difficulty is 1-5
                difficulty=dialog.difficulty_comboBox.currentIndex() + 1
                )

            parent.add_child(new_task)
            self.update_display()

            if self.filepath:
                self.save_tree()

        dialog.deleteLater()

    def edit_group(self, group_to_edit):
        if type(group_to_edit) is not Group:
            raise TypeError(f"{repr(group_to_edit)} not a Group (Type={type(group_to_edit)})")

        dialog = GroupAddDialog()
        dialog.name_lineEdit.setText(group_to_edit.name)
        dialog.desc_lineEdit.setText(group_to_edit.description)

        if dialog.exec_() == QDialog.Accepted:
            group_to_edit.name = dialog.name_lineEdit.text()
            group_to_edit.description = dialog.desc_lineEdit.text()

            self.update_display()

            if self.filepath:
                self.save_tree()

        dialog.deleteLater()

    def edit_task(self, task_to_edit):
        if type(task_to_edit) is not Task:
            raise TypeError(f"{repr(task_to_edit)} not a Task (Type={type(task_to_edit)})")

        dialog = TaskAddDialog()
        dialog.name_lineEdit.setText(task_to_edit.name)
        dialog.desc_lineEdit.setText(task_to_edit.description)
        dialog.state_comboBox.setCurrentIndex(task_to_edit.state)
        dialog.importance_comboBox.setCurrentIndex(task_to_edit.importance - 1)
        dialog.difficulty_comboBox.setCurrentIndex(task_to_edit.difficulty - 1)

        if dialog.exec_() == QDialog.Accepted:
            task_to_edit.name = dialog.name_lineEdit.text()
            task_to_edit.description = dialog.desc_lineEdit.text()
            task_to_edit.state = dialog.state_comboBox.currentIndex()
            task_to_edit.importance = dialog.importance_comboBox.currentIndex() + 1
            task_to_edit.difficulty = dialog.difficulty_comboBox.currentIndex() + 1

            self.update_display()

            if self.filepath:
                self.save_tree()

        dialog.deleteLater()

    def move_item(self, parent, item_to_move):
        
        if type(parent) is not Group:
            raise TypeError(f"{repr(parent)} not a Group (Type={type(parent)})")
        if not isinstance(item_to_move, Item):
            raise TypeError(f"{repr(item_to_move)} not an Item (Type={type(item_to_move)})")
        
        dialog = MoveToDialog()
        all_groups = get_all_groups_in_tree(self.tree)

        for group in all_groups:
            dialog.new_parent_comboBox.addItem(group.name)
        
        if type(item_to_move) is Group:
            dialog.new_parent_comboBox.addItem("No parent")

        if parent is self.main_group:
            dialog.new_parent_comboBox.setCurrentIndex(len(all_groups))
        else:
            dialog.new_parent_comboBox.setCurrentIndex(all_groups.index(parent))

        if dialog.exec_() == QDialog.Accepted:
            choice = dialog.new_parent_comboBox.currentText()
            new_parent = None
            if choice == "No parent":
                new_parent = self.main_group
            else:
                for group in all_groups:
                    if group.name == choice:
                        new_parent = group
                        break
            
            parent.remove_child(item_to_move)
            new_parent.add_child(item_to_move)
            self.update_display()

            if self.filepath:
                self.save_tree()
