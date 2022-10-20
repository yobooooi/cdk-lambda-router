from threading import local
import boto3
import logging
import uuid

from botocore.exceptions import ClientError
from controller import Base

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s")
logging.getLogger().setLevel(logging.INFO)


class AWSS3BucketPubliclyWritable(Base):
    def __init__(self) -> None:
        super()
        self.control_name = "AWS S3 bucket publicly writable"
        self.control_descreption = "This policy identifies the S3 buckets that are publicly writable by Put/Create/Update/Replicate/Write/Delete bucket operations. These permissions permit anyone, malicious or not, to Put/Create/Update/Replicate/Write/Delete bucket operations on your S3 bucket if they can guess the namespace. S3 service does not protect the namespace if ACLs and Bucket policy is not handled properly, with this configuration you may be at risk of compromise of critical data by leaving S3 public.\n\nFor more details:\nhttps://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-permissions.html\nhttps://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html#ensure-object-ownership"
        self.control_id = "S3-public-writable"
        self.control_severity = "high"
        self.control_remediable = False
        self.control_recomendation = "1. Log in to the AWS Console\n2. Navigate to the 'S3' service\n3. Click on the S3 resource reported in the alert\n4. Click on the 'Permissions' tab\n5. If Access Control List is set to 'Public' follow the below steps\na. Under 'Access Control List', Click on 'Everyone' and uncheck all items\nb. Click on Save changes\n6. If 'Bucket Policy' is set to public follow the below steps\na. Under 'Bucket Policy', Select 'Edit Bucket Policy' and consider defining what explicit 'Principal' should have the ability to PUT/CREATE/REPLICATE/DELETE objects in your S3 bucket. You may also want to specifically limit the 'Principal' ability to perform specific PUT/CREATE/REPLICATE/DELETE functions, without the wild card.\nIf 'Bucket Policy' is not required delete the existing 'Bucket Policy'.\nb. Click on Save changes\n\nNote: Make sure updating 'Access Control List' or 'Bucket Policy' does not affect S3 bucket data access."
        self.control_remediation_role = ""
        self.control_notify = False

    def remediate(self, resource_identifier, account_id):
        logging.info("Control Name: {0}".format(self.control_name))
        logging.info("Control Description: {0}".format(self.control_descreption))
        logging.info("Control Severity: {0}".format(self.control_severity))
        logging.info("Resource Identifier: {0}".format(resource_identifier))
        logging.info("AWS Account: {0}".format(account_id))

        logging.info("Control is not remediable. Notification is set to {0}".format(self.control_notify))

    def evaluator(self):
        pass
