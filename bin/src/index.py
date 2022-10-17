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
  event = {
    "control"             : "AWS-S3-buckets-are-accessible-to-public",
    "resource_identifier" : ""
  }

  spec = importlib.util.spec_from_file_location(
    "", 
    location="./remediators/{0}/main.py".format(event["control"]))
  base = spec.loader.load_module()

  remediator = getattr(base, event["control"])
  remediator().remediate(resource_identifier=event["resource_identifier"])
