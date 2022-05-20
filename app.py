import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets
from PyQt5.QtCore import QThread

PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)

try:
    # Отображает иконку на панели задач
    from PyQt5.QtWinExtras import QtWin
    app_version = u'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(app_version)
except ImportError:
    print('[ERROR] The icon cannot be displayed')


class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


class TrainSchedule(QMainWindow):
    def __init__(self):
        super(TrainSchedule, self).__init__()

        self.setWindowTitle('Train Schedule')
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.resize(1200, 800)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(800)


def app_run(application):
    app = QApplication(sys.argv)
    window = TrainSchedule()

    webapp = FlaskThread(application)
    webapp.start()

    app.aboutToQuit.connect(webapp.terminate)

    view = QtWebEngineWidgets.QWebEngineView()
    view.load(QtCore.QUrl(ROOT_URL))
    window.setCentralWidget(view)

    window.show()

    return app.exec_()


if __name__ == '__main__':
    from send_data import app
    sys.exit(app_run(app))
