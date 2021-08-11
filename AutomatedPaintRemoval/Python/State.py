from __future__ import annotations
from abc import ABC, abstractmethod
import RobotVisionModule as rvm
import RobotController as rc
from Image import ImageConverter
import numpy as np


class ProcessContext:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """A reference to the current state of the Context."""

    def __init__(self, state: ProcessState) -> None:
        self.transition_to(state)

    def transition_to(self, state: ProcessState):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def run(self, mainwindow):
        self._state.run(mainwindow)

    def stop(self, mainwindow):
        self._state.stop(mainwindow)


class ProcessState(ABC):
    """Abstract state class"""

    @property
    def context(self) -> ProcessContext:
        return self._context

    @context.setter
    def context(self, context: ProcessContext) -> None:
        self._context = context

    @abstractmethod
    def run(self, mainwindow) -> None:
        pass

    @abstractmethod
    def stop(self, mainwindow) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class IdleProcessState(ProcessState):
    def __init__(self):
        self.IsRunning = False

    def run(self, mainwindow) -> None:
        print("IdleProcessState handles run.")
        mainwindow.ui.StateLineEdit.setText("Idle state")
        mainwindow.capture()

        mainwindow.ui.stopbtn.setText(u"RETAKE")
        mainwindow.ui.startbtn.setText(u"USE")
        mainwindow.ui.stopbtn.setEnabled(True)

        self.context.transition_to(DetectingProcessState())

    def stop(self, mainwindow) -> None:
        print("IdleProcessState cannot stop.")


class DetectingProcessState(ProcessState):
    def __init__(self):
        self.IsRunning = False

    def run(self, mainwindow) -> None:
        print("DetectingProcessState handles run.")
        if not self.IsRunning:
            self.IsRunning = True
            mainwindow.ui.StateLineEdit.setText("Detecting state")

            points, image = rvm.run_procedure(mainwindow.image.pixel_array)
            mainwindow.showProcessedImage(ImageConverter.to_QImage(image))

            mainwindow.image = image
            mainwindow.points = points

            mainwindow.ui.stopbtn.setText(u"STOP")
            mainwindow.ui.startbtn.setText(u"RUN")

            self.context.transition_to(SandingProcessState())

    def stop(self, mainwindow) -> None:
        mainwindow.ui.stopbtn.setEnabled(False)
        mainwindow.ui.stopbtn.setText("")
        mainwindow.ui.startbtn.setText(u"CAPTURE")

        self.context.transition_to(IdleProcessState())
        print("DetectingProcessState handles stop.")
        # self.context.transition_to(ConcreteStateA())


class StandbyProcessState(ProcessState):
    def __init__(self):
        self.IsRunning = False

    def run(self, mainwindow) -> None:
        print("StandbyProcessState handles run.")

    def stop(self, mainwindow) -> None:
        print("StandbyProcessState handles stop.")


class SandingProcessState(ProcessState):
    def __init__(self):
        self.IsRunning = False

    def run(self, mainwindow) -> None:
        print("SandingProcessState handles run.")
        mainwindow.ui.StateLineEdit.setText("Sanding state")
        rc.run_procedure(mainwindow.points)

        mainwindow.ui.stopbtn.setEnabled(False)
        mainwindow.ui.stopbtn.setText("")
        mainwindow.ui.startbtn.setText(u"CAPTURE")

        self.context.transition_to(IdleProcessState())

    def stop(self, mainwindow) -> None:
        print("SandingProcessState handles stop.")

        mainwindow.ui.stopbtn.setEnabled(False)
        mainwindow.ui.stopbtn.setText("")
        mainwindow.ui.startbtn.setText(u"CAPTURE")

        self.context.transition_to(IdleProcessState())


class PausedProcessState(ProcessState):
    def __init__(self):
        self.IsRunning = False

    def run(self, mainwindow) -> None:
        print("PausedProcessState handles run.")
        mainwindow.ui.StateLineEdit.setText("Paused state")
        self.context.transition_to(IdleProcessState())

    def stop(self, mainwindow) -> None:
        print("PausedProcessState handles stop.")
        # self.context.transition_to(ConcreteStateA())
