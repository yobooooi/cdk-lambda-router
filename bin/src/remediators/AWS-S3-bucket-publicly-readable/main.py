from controller import Base


class EC2Remediator(Base):
  def __init__(self) -> None:
      super()

  def remediate(self, resource_identifier):
      print("remediate EC2")
  
  def evaluator(self):
    pass