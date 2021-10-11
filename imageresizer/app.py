import sys
import os
from PyQt4 import QtGui

from python.resize_images_in_folder import ResizeImage
import python.ui.uiImageResizer as iResize


class MainDialog(QtGui.QDialog):

    def __init__(self):
        super(MainDialog, self).__init__()

        self.ui = iResize.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.browse_btn.clicked.connect(self.browse_folder)
        self.ui.resize_btn.clicked.connect(self.validate_params)

    def browse_folder(self):

        fname_dialog = QtGui.QFileDialog(self, "Open file", __file__)
        fname_dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        if fname_dialog.exec_() == QtGui.QDialog.Accepted:
            self.ui.source_path.setText(fname_dialog.selectedFiles()[0])

    def validate_params(self):

        errors = ""
        # source folder selected
        source_path = str(self.ui.source_path.text())
        if not source_path or not os.path.isdir(source_path) or not os.path.exists(source_path):
            errors = 'Selected source path is not a valid folder.\n'

        # new sizes
        width_size = str(self.ui.width_size.text())
        height_size = str(self.ui.height_size.text())

        values_are_digits = width_size.isdigit() and height_size.isdigit()
        grater_than_zero = int(width_size) > 0 and int(height_size) > 0

        if not values_are_digits or not grater_than_zero:
            errors = errors + 'Width and Height must be numbers grather than Zero.\n'

        if errors:
            result = QtGui.QMessageBox.critical(
                None,
                'ERROR: Resize aborted',
                errors,
                QtGui.QMessageBox.Abort
            )
            return

        self.resize_images(source_path, width_size, height_size)

    def resize_images(self, src_path, w_size, h_size):

        processImages = ResizeImage(src_path, w_size, h_size)
        # execute new resize
        resized_images = processImages.execute()
        result_msg = "{} Images resized".format(resized_images)

        QtGui.QMessageBox.information(None, "Resize finished", result_msg)

        self.close()


def loadUI():
    app = QtGui.QApplication(sys.argv)
    window = MainDialog()
    window.show()
    sys.exit(app.exec_())


print __name__
if __name__ == "__main__" or __name__ == "main":
    loadUI()