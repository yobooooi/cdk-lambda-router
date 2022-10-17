from abc import ABC, abstractmethod


class Base(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def remediate(self, resource_identifier):
    pass

  @abstractmethod
  def evaluator(self):
    pass
