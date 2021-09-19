import sys
import os
from typing import Callable, Union

from PyQt5 import QtCore
from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMessageBox

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from .itawui import Ui_Itaw

UNSAVED_ITEM_COLOR = (130, 130, 130)  # rgb
SAVED_ITEM_COLOR = (0, 0, 0)  # rgb


class ItaWidget(QMainWindow, Ui_Itaw):
    """The main application window."""

    def __init__(self, get_trace: Callable, title: str = '',
                 parent: Union[QWidget, None] = None):
        """Initiates a class instance.

        Args:
            get_trace: A function that supplies traces.
            title: Window title.
            parent: Parent window.
        """
        super().__init__(parent=parent)
        self.setupUi(self)

        self.get_trace = get_trace

        if not title:
            try:
                # Finds out the class name of the object that get_trace
                # is attached to.
                cls = get_trace.__self__.__class__.__name__

                # Adds the class to the window title.
                title = f'Itaw ({cls})'
            except AttributeError:
                # get_trace is not a method.
                title = 'Itaw'

        self.setWindowTitle(title)

        self._clear_window()
        self._create_figure()
        self._connect_signal_slots()

        # Sets the tooltip of the read trace button to the get_trace docstring.
        doc = self.get_trace.__doc__
        tooltip = f'Docsting:\n\n{doc}'
        self.readTraceButton.setToolTip(tooltip)

        # Displays the current directory.
        dir = os.path.abspath('.')
        self.dirLineEdit.setText(dir)

    def _clear_window(self):
        """Removes dummy elements and text from the window."""
        self.traceListWidget.clear()

    def _create_figure(self):
        """Creates a matplotlib figure in the window and set its style."""

        style_file = os.path.join(os.path.dirname(__file__), 'itaw.mplstyle')
        plt.style.use(style_file)

        self.canvas = FigureCanvas(Figure(figsize=(10, 6)))
        self.axes = self.canvas.figure.subplots()
        self.toolbar = ItawNavigationToolbar(self.canvas, self,
                                             coordinates=True)

        self.mplVBox.addWidget(self.toolbar)
        self.mplVBox.addWidget(self.canvas)

        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.minorticks_on()

        # linestyle format: (offset, (on_off_seq)).
        self.axes.grid(b=True, which='major', linestyle=(0, ()))
        self.axes.grid(b=True, which='minor', linestyle=(0, (1, 1)))

    def _connect_signal_slots(self):
        self.readTraceButton.clicked.connect(self._on_get_trace)
        self.saveTraceButton.clicked.connect(self._on_save_trace)
        self.openDirButton.clicked.connect(self._on_open_directory)

        self.tightLayoutAction.triggered.connect(self.update_plot)

        self.resetColorOrderAction.triggered.connect(
            lambda: self.axes.set_prop_cycle(None)
        )

        self.traceListWidget.model().rowsMoved.connect(self._on_row_moved)

        self.traceListWidget.itemChanged.connect(self._on_list_item_changed)

        self.traceListWidget.currentItemChanged.connect(
            self._on_current_trace_changed
        )

    def update_plot(self):
        self.canvas.draw()
        self.canvas.figure.tight_layout()
        # TODO (2021-09-13): go over the tree items and update their icons to match the line color

    def create_path(self, file_name: str) -> str:
        """Creates a path using the directory from the GUI and the supplied file 
        name, and, if a file at the path already exists, asks the user if it 
        should be overwritten.

        Args:
            file_name: 
                The desired file name relative to the directory in the GUI.

        Returns:
            A path if there is no existing file or if the user has confirmed 
            that the existing file can be overwritten. An empty string if a file
            at the generated path already exists and should not be overwritten.
        """

        dir_name = self.dirLineEdit.text()
        full_name = os.path.join(dir_name, file_name)

        # Adds an extension to the file name if it does not have it already.
        _, ext = os.path.splitext(full_name)
        if not ext:
            full_name = full_name + '.txt'

        if os.path.isfile(full_name):

            # Asks the user if the file should be overwritten.

            resp = QMessageBox.question(
                self,
                'Overwrite dialog',
                'File already exists. Would you like to overwrite?',
                buttons=(QMessageBox.Yes | QMessageBox.No),
                defaultButton=QMessageBox.No
            )

            if resp == QMessageBox.Yes:
                print(f'Overwriting file {full_name}')
            else:
                print(f'Keeping exiting file {full_name}.')

                # An empty string will be returned in this case.
                full_name = ''

        return full_name

    def add_trace(self, tr, name: str = '') -> None:
        """Adds a new item to the trace list widget and stores the trace 
        in a dictionary under its user data.

        Args:
            tr: The trace to be stored.
            name: The name of the trace.
        """

        # Creates a new list item.
        item = QListWidgetItem(name)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                      | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled)
        # Flags:
        # ItemIsEnabled - enables user interaction
        # ItemIsEditable - allows to edit the text
        # ItemIsDragEnabled - allows to rearrange items by dragging them

        qcolor = QtGui.QColor(*UNSAVED_ITEM_COLOR)
        item.setForeground(qcolor)

        # Plots the new data in the axes.
        lines = self.axes.plot(tr['x'], tr['y'])

        try:
            self.axes.set_xlabel(tr['xlabel'])
        except (TypeError, LookupError):
            pass

        try:
            self.axes.set_ylabel(tr['ylabel'])
        except (TypeError, LookupError):
            pass

        self.canvas.draw()
        self.canvas.figure.tight_layout()

        if lines:
            line = lines[0]
            line.set_label(name)
            icon_color = line.get_color()
        else:
            line = None
            icon_color = (255, 255, 255, 0)  # rgba transparent white

        # Adds an icon to the trace that has the same color as the line.
        item.setIcon(QtGui.QIcon(_draw_trace_icon(icon_color)))

        # TODO (2021-09-12): remove icon_color ot implement a syncronization
        # between the line color and and icon (e.g. for situations when the
        # line color is changed from outside). Right now icon_color key is unused.
        trace_data = {'trace': tr, 'line': line, 'icon_color': icon_color}
        item.setData(QtCore.Qt.UserRole, trace_data)

        # The item is added to the list only after we are done with editing it 
        # to prevent useless firings of itemChanged signal by the list widget.
        self.traceListWidget.addItem(item)

    # UI interaction functions

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        """Defines what happens when the user presses a key. Overloads 
        a base class method.
        """

        if event.key() == QtCore.Qt.Key_Delete:

            # Deletes the currently selected trace and updates the plot.
            ind = self.traceListWidget.selectedIndexes()

            if ind:
                r = ind[0].row()
                item = self.traceListWidget.takeItem(r)

                trace_data = item.data(QtCore.Qt.UserRole)
                self.axes.lines.remove(trace_data['line'])

                self.canvas.draw()

        elif event.modifiers() == QtCore.Qt.ControlModifier:

            if event.key() == QtCore.Qt.Key_S:
                # Ctrl+s - saves the current trace
                self._on_save_trace()
            elif event.key() == QtCore.Qt.Key_X:
                # Ctrl+x - toggles the visibility of the current trace

                ind = self.traceListWidget.selectedIndexes()

                if ind:
                    r = ind[0].row()
                    item = self.traceListWidget.item(r)

                    trace_data = item.data(QtCore.Qt.UserRole)
                    line = trace_data['line']

                    v = not line.get_visible()
                    line.set_visible(v)
                    self.canvas.draw()

                    # Toggles the trace icon.
                    if v:
                        icon = _draw_trace_icon(line.get_color())
                    else:
                        color = (255, 255, 255, 0)  # rgba transparent
                        icon = _draw_trace_icon(color, border=False)

                    item.setIcon(QtGui.QIcon(icon))

        event.accept()

    def _on_row_moved(self, src, start_row: int, sr2: int, dst, end_row: int):
        """Called when the entries in traceListWidget are reorders."""

        del src, dst  # Irrelevant because the movement is within one widget.
        del sr2  # Irrelevant because only one item is moved at a time.

        if end_row > start_row:
            # Originally, the end row is counted as if the moved item was still
            # present at its old place. This leads to miscounting by one if
            # the new index is higher than the old one.
            end_row = end_row - 1

        # Reorders the axes lines in the same way as the list items
        line = self.axes.lines.pop(start_row)
        self.axes.lines.insert(end_row, line)

        self.canvas.draw()

    def _on_list_item_changed(self, item: QListWidgetItem):
        """Called when a trace list entry is changed in any way. Used to 
        push to line labels the changes introduced in item names. Changes to 
        all other item attributes (like the icon or the data) also trigger
        the execution of this function and have to be ignored.
        """

        trace_data = item.data(QtCore.Qt.UserRole)

        # It can be called before user data is added to the list item. Such
        # calls are ignored.
        if trace_data:
            lbl = trace_data['line'].get_label()
            text = item.text()

            if lbl != text:
                trace_data['line'].set_label(text)

    def _on_save_trace(self):
        """Saves the currently selected trace."""
        ind = self.traceListWidget.selectedIndexes()

        if ind:
            r = ind[0].row()
            item = self.traceListWidget.item(r)
            trace_data = item.data(QtCore.Qt.UserRole)

            fname = self.create_path(item.text())

            if fname:
                try:
                    save_trace(fname, trace_data['trace'])
                    qcolor = QtGui.QColor(*SAVED_ITEM_COLOR)
                    item.setForeground(qcolor)
                except Exception as e:
                    QMessageBox.warning(self, 'Exception', e)
                # Errors are suppressed at this point, so that if something 
                # goes wrong during saving the data (e.g. the directory is not
                # accessible, or the file name contains an invalid character),
                # the exception is displayed, but the app is not shut down which
                # would result in loosing data.

    def _on_get_trace(self):
        argstr = self.argsLineEdit.text()

        # Getting a new trace is hedged to prevent shutting down the GUI due to
        # errors in supplied arguments.
        try:
            # Get a new trace from the instrument using the list of arguments.
            tr = eval(f'self.get_trace({argstr})')
        except Exception as e:
            QMessageBox.warning(self, 'Exception during getting a new trace', str(e))
            return

        # Generates a name for the trace and adds the trace to the list.
        n = self.traceListWidget.count()
        trace_name = f'Trace {n+1}'
        self.add_trace(tr, trace_name)


    def _on_current_trace_changed(self):
        # TODO (2021-09-12): Updates the plot labels and displays the trace save status.
        ind = self.traceListWidget.selectedItems()
        ind = self.traceListWidget.selectedIndexes()

    def _on_open_directory(self):
        """Creates a dialog to select the base directory."""

        dir = QFileDialog.getExistingDirectory(self, caption="Base directory")

        if dir:
            dir = os.path.abspath(dir)  # Normalizes the path format
            self.dirLineEdit.setText(dir)


def itaw(get_trace: Callable, title: str = '') -> Union[ItaWidget, None]:
    """Creates a widget to interactive acquire traces using get_trace. 

    Args:
        get_trace: 
            A function or method that returns an object (obj) containing two 
            numeric arrays that can be accessed as obj['x'] and obj['y'].
        title:
            Window title.

    Returns:
        A window instance if called from an IPython console or None if called 
        from a regular console. Nothing is returned in the second case because
        the console is blocked by the running Qt app until the window is closed.
    """

    # Determines if the app has been run from an IPython console.
    try:
        from IPython import get_ipython
        ip = get_ipython()

        if ip and ip.has_trait('kernel'):
            is_ipython = True

            ip.magic('gui qt')
        else:
            is_ipython = False

    except ModuleNotFoundError:
        is_ipython = False

    # Not than one instance of QApplication is not allowed.
    app = QtCore.QCoreApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    win = ItaWidget(get_trace, title)

    win.show()

    # Sets the window to be the currently active window
    # (brings it to the foreground).
    win.activateWindow() 

    win.canvas.draw()
    win.canvas.figure.tight_layout()

    if is_ipython:
        # The window has already been embedded into the IPython event loop
        # by running gui qt magic.
        return win
    else:
        # Executes the app event loop.
        sys.exit(app.exec())


def save_trace(fname: str, tr, fmt: str = '%.18g', delimiter: str = ' ',
               newline: str = '\n', comments: str = '# ') -> bool:
    """Saves the trace data with labels in a file, overwriting the file if 
    italready  exists.

    Note: the default format %g removes trailing veros, which can significantly 
    reduce file size for data with few significant digits. 

    Args:
        tr: 
            An object containing two numeric arrays that can be accessed 
            as tr['x'] and tr['y'] and can optionally include 'xlabel' and 
            'ylabel' strings. 
        fname: 
            File name. If it does not have an extension, a default one is added.

    Returns:
        True if the data was saved, False otherwise. 
    """

    with open(fname, 'w') as fd:
        try:
            # Writes the labels.
            hdr = comments + tr['xlabel'] + delimiter + tr['ylabel'] + newline
            fd.write(hdr)
        except (TypeError, LookupError):
            pass

        line_fmt = fmt + delimiter + fmt + newline

        if len(tr['x']) != len(tr['y']):
            print('x and y vectors have unequal lengths. '
                  'Not all elements will be saved.')

        l = min(len(tr['x']), len(tr['y']))
        for i in range(l):
            # Writes the main data.
            fd.write(line_fmt % (tr['x'][i], tr['y'][i]))

        print('A trace is saved at %s' % fname)
        return True


class ItawNavigationToolbar(NavigationToolbar2QT):
    """A custom navigation toolbar in which some of the default matplotlib 
    buttons are removed. See https://stackoverflow.com/questions/12695678/how-to-modify-the-navigation-toolbar-easily-in-a-matplotlib-figure-window
    """
    toolitems = [t for t in NavigationToolbar2QT.toolitems
                 if (set(t) & {'Home', 'Pan', 'Zoom', 'Customize', 'Save'})]


def _draw_trace_icon(color: Union[str, tuple], border=True) -> QtGui.QPixmap:
    """Creates a pixel map circle with transparent background.

    Args:
        color: 
            The circle fill color, defined by a hex code string (e.g. #ff7f0e), 
            an RGB tuple with three elements or an RGBA tuple with four 
            elements. Tuple elements take values between 0 and 255.
    """

    a = 40  # icon size in pixels

    pixmap = QtGui.QPixmap(a, a)
    pixmap.fill(QtGui.QColor(255, 255, 255, 0))  # rgba transparent white

    if border:
        border_qcolor = QtGui.QColor(0, 0, 0)
    else:
        border_qcolor = QtGui.QColor(255, 255, 255, 0)

    painter = QtGui.QPainter(pixmap)
    painter.setPen(QtGui.QColor(border_qcolor))

    if type(color) is str:
        # The color is given as a hex code string.
        qtcolor = QtGui.QColor(color)
    else:
        # Otherwise the color must be given as a tupe.
        qtcolor = QtGui.QColor(*color)

    painter.setBrush(qtcolor)

    r = int(a/2)  # radius
    painter.drawEllipse(int(r/2), int(r/2), r, r)

    return pixmap