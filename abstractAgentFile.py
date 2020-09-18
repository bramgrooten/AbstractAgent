import abc
from abc import ABC


class AbstractAgent(ABC):
   """ Abstract classes inherit from the ABC base class. """

   def __init__(self, *args, **kwargs):
       """ Initialization method for the agent. """
       pass

   def __str__(self):
       """ Internal python method that converts classes to strings. """
       pass

   def __repr__(self):
       """ Echoed when it is evaluated as an object. """
       pass

   @abc.abstractmethod
   def train(self, score):
       """ Abstract method that trains the agent.  """
       pass

   @abc.abstractmethod
   def action(self, obs):
       """ Abstract method that returns an action. The return type is not specified yet. """
       pass

   @abc.abstractmethod
   def load(self):
       """ Abstract method that loads an internal state. """
       pass

   @abc.abstractmethod
   def save(self):
       """ Abstract method that saves an internal state. """
       pass