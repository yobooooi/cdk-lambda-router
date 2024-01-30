import importlib.util
import logging
import os
import sys

from pathlib import Path

def controller(event, context):
  sys.path.append(str(Path.cwd() / "remediators"))
  try:
    event_pattern = event['event_pattern']
    spec = importlib.util.spec_from_file_location("", location="./remediators/{0}/main.py".format(event["control"]))
    base = spec.loader.load_module()

    remediator = getattr(base, event_pattern)
    remediator().remediate(resource_identifier=event["resource_identifier"], account_id=event["account"])
  except TypeError:
    logging.ERROR("Attempting to instantiate class with missing methods")


if __name__ == "__main__":
  sys.path.append(str(Path.cwd() / "remediators"))
  event = {
    "control"             : "AWSS3BucketPubliclyReadable",
    "resource_identifier" : "arn::test03",
    "account_id"          : "1234567890987"
  }

  spec = importlib.util.spec_from_file_location(
    "", 
    location="./remediators/{0}/main.py".format(event["control"]))
  base = spec.loader.load_module()

  remediator = getattr(base, event["control"])()
  remediator.remediate(resource_identifier=event["resource_identifier"], account_id=event["account_id"])
