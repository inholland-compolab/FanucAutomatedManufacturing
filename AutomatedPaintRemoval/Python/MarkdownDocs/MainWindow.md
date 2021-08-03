# MainWindow.py - MainWindow.ui - MainWindowUI.py
## Description
This collection of MainWindow files are used for the user interface that the user interacts with to control the system.
MainWindow.ui is the file created from Qtdesigner, MainWindowUI.py is the .ui file build to python and MainWindow.py is
the file which contains the MainWindow class that is called by the main routine when the program starts.

## MainWindow.ui
As stated before, the .ui file is a file that is created from Qt designer. With Qt designer u can create the overall 
look of your UI. Different labels can be added to your window or buttons to control parts of your system. It is
possible to directly code all the buttons and labels into Python, but this makes it designing slightly easier. 
installing Qt designer can be done from [here.][qt designer link]


![This is what it looks like][qt]

## MainWindowUI.py
This is the python code that is build from the MainWindow.ui file. To build this file you need to

1. Open a command prompt inside the folder where your .ui file is in.
2. typ in the following command:
   
        pyside2-uic [name of file].ui -o [name of py file].py (use without square brackets)

If u don't already have a name for or .py file, use the same name as your .ui file but with UI after the name.
Make sure that PySide2 is installed on your system or else this command will not work.

## MainWindow.py
This file contains the actual class that gets called by the main routine to start the ui.

    app = QtWidgets.QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    app.exec_()

This class is responsible for loading the MainWindowUI.py file, creating callbacks for certain events to function, and
some more specific changes to the ui that can only be done in the actual code. This user interface also handles the
acquiring of images. 

For more detailed information about how PySide2 works you can refer to the PySide2 [documentation.][documentation]

## resources
This program makes use of a resource file. A resource file is a file that can store different kinds of resources like
text files and image files that can be added to the user interface. A resource can be added to a resource file by using
qt designer.

1. On the right bottom side, click the resource browser tab. \
![dd][Resource tab]
2. Click in the pencil icon. \
![dd][Pencil]
3. Choose the file you want to add a resource to.
4. click on "Add files" \
![][add files]
   
Now you can use resources inside Qt designer. I cannot explain exactly how you need to use these files, because
it is very dependent on what type of widget you want to use it.

Just like the .ui file, you need to also build the resource file. the resource file extension is .qrc. To build this
file you need to paste the following command into a command prompt.

    pyside2-rcc [name of file].rc -o [name of py file].py (use without square brackets)

This file should be automatically added into the MainWindowUI.py file.

[documentation]: https://doc.qt.io/qtforpython-5/contents.html
[qt designer link]: https://build-system.fman.io/qt-designer-download
[qt]: Capture.PNG
[Resource tab]: resource%20browser.PNG
[Pencil]: pencil.PNG
[add files]: Add%20file.PNG