"""
This module contains the MainWindow class which constructs
the GUI that you see when you start the application

The GUI uses PySide2 a python wrapper for the qt c++ library.
This GUI is construct from 3 files, MainWindow.py, MainWindow.ui
and MainWindowUI.py

MainWindow.ui is the design file that can be opened with qt designer
MainWindowUI.py is compiled version of MainWindow.ui in python.
MainWindow.py runs the MainWindowUI.py file and handles event construction
"""

# pyside2-uic [name of file].ui -o [name of py file].py  <- for generating .py file from .ui  (use without square brackets)
# pyside2-rcc [name of file].rc -o [name of py file].py  <- for generating .py file from .qrc (use without square brackets)

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QSize
from PySide2.QtMultimedia import QCamera, QCameraImageCapture, QVideoFrame, QImageEncoderSettings, QCameraInfo
from PySide2.QtGui import QPixmap, QImage
from MainWindowUI import Ui_MainWindow
from Image import ImageConverter, Image, EImageType
import numpy as np
import cv2 as cv
from State import ProcessContext, IdleProcessState, DetectingProcessState


class MainWindow(QMainWindow):
    """
    The MainWindow of the system
    """
    def __init__(self, parent=None):
        """
        Constructs the main GUI.

        :param None parent: This variable should always be none since the MainWindow
        Should never have a parent.
        """

        """calls QMainWindow object"""
        super(MainWindow, self).__init__(parent)

        """Construct MainWindowUI object and run the function to
        setup the environment"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """Here events get bound to certain functions.
        Set the signals of certain buttons to certain functions"""
        self.ui.homebtn.clicked.connect(self.on_homebtn_clicked)
        self.ui.simbtn.clicked.connect(self.on_simbtn_clicked)

        self.ui.manualbtn.clicked.connect(self.on_manualbtn_clicked)

        self.ui.startbtn.clicked.connect(self.on_startbtn_clicked)
        self.ui.stopbtn.clicked.connect(self.on_stopbtn_clicked)

        self.ui.exitui.triggered.connect(self.on_window_closed)

        self.ui.capturebtn.clicked.connect(self.on_capturebtn_clicked)
        self.ui.sinorcon.stateChanged.connect(self.on_sinorcon_stateChanged)
        self.ui.capturesstopbtn.clicked.connect(self.on_capturesstopbtn_clicked)

        self.ui.cameraviewbtn.clicked.connect(self.on_imageview_changed)
        self.ui.procesviewbtn.clicked.connect(self.on_imageview_changed)

        """set the initial state of the pushbuttons"""
        self.ui.cameraviewbtn.setDown(True)
        self.ui.procesviewbtn.setDown(False)

        """set image acquisition booleans"""
        self.stop = False
        self.continuousRun = False

        """Constructs camera object """
        self.camera = QCamera()

        """Create image capture object from camera and
        connect the imageCaptured event to NewImageFromWebcam method"""
        self.imageCapture = QCameraImageCapture(self.camera)
        self.imageCapture.imageCaptured.connect(self.newImageFromWebcam)

        """Set the image setting of the image capture"""
        image_settings = QImageEncoderSettings()
        image_settings.setCodec("jpeg")
        image_settings.setResolution(1920, 1080)

        self.imageCapture.setEncodingSettings(image_settings)

        """Set buffer format and set capture mode to video.
        start the camera."""
        self.imageCapture.setBufferFormat(QVideoFrame.Format_RGB32)
        self.camera.setCaptureMode(QCamera.CaptureVideo)
        self.camera.start()

        """Setting some initial values"""
        self.ui.StateLineEdit.setText("Unknown state")

        self.points = []
        self.image = None

        self.context = ProcessContext(IdleProcessState())

    def on_Primebtn_Clicked(self):
        """
        Dummy function
        :return:
        """
        print("yes")

    def on_homebtn_clicked(self):
        """
        Set current index of stackedwidget to the home scene.
        :return:
        """
        print("Home")
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_simbtn_clicked(self):
        """
        Set current index of stackedwidget to the simulation scene.
        :return:
        """
        print("Sim")
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_manualbtn_clicked(self):
        """
        Set current index of stackedwidget to the simulation scene.
        :return:
        """
        print("Manual")
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_startbtn_clicked(self):
        """
        This method gets triggered when the start button has been pressed.

        Starts the system by calling the context run function
        :return:
        """
        self.context.run(self)

    def on_stopbtn_clicked(self):
        """
        This method gets triggered when the stop button has been pressed.

        Stops the system by calling the context stop function
        :return:
        """
        self.context.stop(self)

    def on_capturebtn_clicked(self):
        """
        This method gets triggered when the capture button has been pressed.

        Checks whether or not the single or continuous run checkbox is
        checked and runs either the continuous function or the single function
        :return:
        """
        print("Capture buttonPressed")
        if self.ui.sinorcon.checkState() is Qt.Unchecked:
            self.runSingle()
        elif self.ui.sinorcon.checkState() is Qt.Checked:
            if self.continuousRun is False:
                self.continuousRun = True
                self.runContinous()

    def on_sinorcon_stateChanged(self, state):
        """
        This method gets triggered when the checkbox state changes

        Enalbes or disables stop button
        :param state: contains the changed to state of the checkbox
        :return: nothing
        """
        if state is 0:
            self.ui.capturesstopbtn.setEnabled(False)
        elif state is 2:
            self.ui.capturesstopbtn.setEnabled(True)

    def on_capturesstopbtn_clicked(self):
        """
        This method gets triggered when the capturesstopbutton has
        been pressed.

        :return: nothing
        """
        self.stop = True

    def on_imageview_changed(self):
        """
        This method gets triggered when the imageviewstack has changed.

        changes the imageviewstack to the correct view
        :return:
        """

        if self.ui.cameraviewbtn.isChecked() is True:
            self.ui.imageviewstack.setCurrentIndex(0)
        else:
            self.ui.imageviewstack.setCurrentIndex(1)

    def capture(self):
        """
        This method gets called when the system is running.
        This method differs from runSingle in that it is not called
        By the debug buttons.

        :return:
        """
        if self.imageCapture.isReadyForCapture():
            self.imageCapture.capture('E:/Code/PyCharmProjects/AutomatedPaintRemoval/capture.jpeg')

    def runSingle(self):
        """
        This method is called by the image debug buttons and runs ones

        :return:
        """
        if self.imageCapture.isReadyForCapture():
            self.imageCapture.capture('E:/Code/PyCharmProjects/AutomatedPaintRemoval/capture.jpeg')

    def runContinous(self):
        """
        This method is called by the image debug buttons and runs
        continuously until the stop button has been pressed.

        :return:
        """
        while not self.stop and self.ui.sinorcon.checkState() == Qt.Checked:
            if self.imageCapture.isReadyForCapture():
                self.imageCapture.capture('E:/Code/PyCharmProjects/AutomatedPaintRemoval/capture.jpeg')

            self.delay_ms(10)
        self.stop = False
        self.continuousRun = False

    def newImageFromWebcam(self, id, image: QImage):
        """
        This method is triggered when a new image has been captured by the
        camera.

        :param id: id of the image
        :param QImage image: the image itself
        :return: nothing
        """
        if image.isNull():
            return

        image = image.convertToFormat(QImage.Format_RGB888)
        self.showPreProcessedImage(image)

        self.image = Image.construct_from_QImage(image)

    def on_window_closed(self):
        """
        This method is called by the on window close button (x)

        :return: nothing
        """
        self.imageCapture.cancelCapture()
        self.stop = True
        self.delay_ms(200)
        self.camera.stop()
        self.camera.unload()

        self.close()

    def delay_ms(self, ms: int):
        """
        This method is used as a non eventblocking pause to give the camera
        extra time to acquire the image.

        :param int ms: time the system needs to wait.
        :return:
        """

        delta = QTime.currentTime().addMSecs(ms)
        while QTime.currentTime() < delta:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 10)

    def showPreProcessedImage(self, image: QImage):
        """
        Sets the image acquired from the camera into the image
        view.

        :param QImage image: The image to be set
        :return: nothing
        """

        width = self.ui.imageview.width()
        height = self.ui.imageview.height()

        self.ui.imageview.setPixmap(QPixmap.fromImage(image).scaled(width, height, Qt.KeepAspectRatio))

        if not self.ui.cameraviewbtn.isDown():
            self.ui.cameraviewbtn.click()

    def showProcessedImage(self, image: QImage):
        """
        Sets the image into the processedimageview.

        :param QImage image: The image to be set
        :return:
        """

        width = self.ui.imageviewprocessed.width()
        height = self.ui.imageviewprocessed.height()

        self.ui.imageviewprocessed.setPixmap(QPixmap.fromImage(image).scaled(width, height, Qt.KeepAspectRatio))

        if not self.ui.procesviewbtn.isDown():
            self.ui.procesviewbtn.click()
