from controller import Base


class S3Remediator(Base):
  def __init__(self) -> None:
      super()

  def remediate(self, resource_identifier):
      print("remediate S3")
  
  def evaluator(self):
    pass