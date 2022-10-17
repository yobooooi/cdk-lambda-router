import boto3
import logging
import uuid

from botocore.exceptions import ClientError
from controller import Base

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')


class S3Remediator(Base):
  def __init__(self) -> None:
      super()
      self.control_name = "AWS S3 buckets are accessible to public"
      self.control_descreption = "S3 buckets which are publicly accessible. Amazon S3 allows customers to store or retrieve any type of content from anywhere in the web. Often, customers have legitimate reasons to expose the S3 bucket to public, for example, to host website content. However, these buckets often contain highly sensitive enterprise data which if left open to public may result in sensitive data leaks."
      self.control_id = "S3-public-bucket"
      self.control_severity = "high"
      self.control_remediable = True
      self.control_recomendation = "1. Login to the AWS Console\n2. Navigate to the 'S3' service\n3. Click on the 'S3' resource reported in the alert\n4. Click on the 'Permissions'\n5. If Access Control List' is set to 'Public' follow below steps\na. Under 'Access Control List', Click on 'Everyone' and uncheck all items\nb. Click on Save\n6. If 'Bucket Policy' is set to public follow below steps\na. Under 'Bucket Policy', modify the policy to remove public access\nb. Click on Save\nc. If 'Bucket Policy' is not required delete the existing 'Bucket Policy'.\n\nNote: Make sure updating 'Access Control List' or 'Bucket Policy' does not affect S3 bucket data access."
      self.control_remediation_role = ""
      self.control_notify = False

  def remediate(self, resource_identifier, account_id): 
      logging.INFO(f"Control Name: {self.control_name}")
      logging.INFO(f"Control Descriotion: {self.control_descreption}")
      logging.INFO(f"Control Severity: {self.control_severity}")
      logging.INFO(f"Resource Identifier: {resource_identifier}")
      logging.INFO(f"AWS Account: {account_id}")

      if self.control_remediable:
        if self.control_remediation_role == "":
          s3_client = boto3.client("s3")
          try:
            response = s3_client.put_public_access_block(
              Bucket = resource_identifier,
              PublicAccessBlockConfiguration = {
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
              },
            )
            logging.DEBUG(response)
          except ClientError as e:
            logging.ERROR(e)
        else:
          sts_client = boto3.client("sts")
          session_credentials = sts_client.assume_role(
              RoleArn=f"arn:aws:iam::{account_id}:role/{self.control_remediation_role}",
              RoleSessionName=f"{self.control_id}-rememediate-{uuid.uuid1()}",
          )
      
          ACCESS_KEY = session_credentials["Credentials"]["AccessKeyId"]
          SECRET_KEY = session_credentials["Credentials"]["SecretAccessKey"]
          SESSION_TOKEN = session_credentials["Credentials"]["SessionToken"]
      
          s3_client = boto3.client(
              "s3",
              aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY,
              aws_session_token=SESSION_TOKEN,
          )
          try:
            response = s3_client.put_public_access_block(
              Bucket = resource_identifier,
              PublicAccessBlockConfiguration = {
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
              },
            )
            logging.DEBUG(response)
          except ClientError as e:
            logging.ERROR(e)
      else:
        logging.INFO(f"Control is not remediable. Notification is set to {self.control_notify}")

  def evaluator(self):
      pass