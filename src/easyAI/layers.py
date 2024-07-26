"""Module representing the layers API."""

from collections.abc import Callable
from easyAI.core.objects import Layer, Neuron, Node

class Dense(Layer):
    """Class representing a fully connected layer."""

    def __init__(self, n: int, *, activation="relu", name="Fully Connected Layer") -> None:
        super().__init__(n, activation=activation, name=name)

class Input(Layer):
    """Class representing a node layer."""

    def __init__(self, n: int, *, name="Input layer") -> None:
        super().__init__(n, activation="step", name=name)

        self._structure = [Node() for _ in range(self.n)]

        del self._activation

        super()._set_indexes()

class Conv(Layer):
    """Class representing a convolutional network layer."""

    def __init__(self, n: int, activation="relu", name="layer") -> None:
        raise NotImplemented
        super().__init__(n, activation=activation, name=name)

class Rec(Layer):
    """Class representing a recurrent network layer."""

    def __init__(self, n: int, activation="relu", name="layer") -> None:
        raise NotImplemented
        super().__init__(n, activation=activation, name=name)

