from .lib import *
import  socket
class HomeWidget(QWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = QWebEngineView(self)


        self.webSettings = self.browser.settings()
        self.webSettings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webSettings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.webSettings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
        self.webSettings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.webSettings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webSettings.setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript, True)


        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)


        ## Launch Main brower 
        
        #self.browser.load(QUrl("https://github.com/stephene369/"))
        self.port=self.find_free_port() 
        self.launchWorker = LauncherWorker(port=self.port , browser=self)

        self.launchWorker.server.Handler.parent = parent

        self.launchWorker.finished.connect(self.launchWorkerFinished)
        self.launchWorker.start()
        self.browser.load(QUrl(f"http://localhost:{self.port}" )) 




        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.on_downloadRequested)
        


        handler = PrintHandler()
        handler.setPage(self.browser.page())

        printPreviewShortCut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_P), self.browser)
        printShortCut = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_P), self.browser)

        printPreviewShortCut.activated.connect(handler.printPreview)
        printShortCut.activated.connect(handler.print)










    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]

    def launchWorkerFinished(self, success):
        print(success)
        if success["link"] == False: 
            print("Le lien ne marche pas")
        else: 
            self.link = success["link"]
            self.browser.load(QUrl(self.link))
            print("Server en cours")

    def on_downloadRequested(self, download):
        downloadPath = QFileDialog.getSaveFileName(self, "Save File", download.path())[0]
        if downloadPath:
            download.setPath(downloadPath)
            download.accept()


    def printPage(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A4)
        printer.setFullPage(True)

        # Open print dialog
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            # Print the content
            self.browser.page().print(printer, lambda success: print("Printed successfully" if success else "Print failed"))




class PrintHandler(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.m_page = None
        self.m_inPrintPreview = False

    def setPage(self, page):
        assert not self.m_page
        self.m_page = page
        self.m_page.printRequested.connect(self.printPreview)

    @pyqtSlot()
    def print(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self.m_page.view())
        if dialog.exec_() != QDialog.Accepted:
            return
        self.printDocument(printer)

    @pyqtSlot()
    def printPreview(self):
        if not self.m_page:
            return
        if self.m_inPrintPreview:
            return
        self.m_inPrintPreview = True
        printer = QPrinter()
        preview = QPrintPreviewDialog(printer, self.m_page.view())
        preview.paintRequested.connect(self.printDocument)
        preview.exec()
        self.m_inPrintPreview = False

    @pyqtSlot(QPrinter)
    def printDocument(self, printer):
        loop = QEventLoop()
        result = False

        def printPreview(success):
            nonlocal result
            result = success
            loop.quit()
        progressbar = QProgressDialog(self.m_page.view())
        progressbar.findChild(QProgressBar).setTextVisible(False)
        progressbar.setLabelText("Wait please...")
        progressbar.setRange(0, 0)
        progressbar.show()
        progressbar.canceled.connect(loop.quit)
        self.m_page.print(printer, printPreview)
        loop.exec_()
        progressbar.close()
        if not result:
            painter = QPainter()
            if painter.begin(printer):
                font = painter.font()
                font.setPixelSize(20)
                painter.setFont(font)
                painter.drawText(QPointF(10, 25), "Could not generate print preview.")
                painter.end()





class LauncherWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self , port , browser):
        super().__init__()
        self.server = Launcher(browser=browser)
        self.port = port
        print("Launcher Worker Initializ")


    def run(self):
        try : 
            self.link = self.server.launch(port=self.port)
            self.finished.emit({
            "link":f"http://localhost:{self.port}"
            })

        except Exception as e : 
            self.finished.emit({
                "link":False
            })
