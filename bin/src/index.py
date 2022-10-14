import importlib.util
import logging
import os
import sys

from pathlib import Path

def controller(event, context):
  try:
    event_pattern = event['event_pattern']
    spec = importlib.util.spec_from_file_location("", location=f"remediators/{event_pattern}.py")
    base = spec.loader.load_module()

    remediator = getattr(base, event_pattern)
    remediator().remediate()
  except TypeError:
    logging.ERROR("Attempting to instantiate class with missing methods")


if __name__ == "__main__":
  sys.path.append(str(Path.cwd() / "remediators"))
  event_pattern = "EC2Remediator"

  spec = importlib.util.spec_from_file_location("", location=f"./remediators/{event_pattern}/main.py")
  base = spec.loader.load_module()

  remediator = getattr(base, event_pattern)
  remediator().remediate()
