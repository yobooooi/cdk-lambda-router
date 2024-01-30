"""Deployment module of custon CDK constructs"""
import cdk as core

from aws_cdk import (
    aws_lambda as _lambda,
    Stack,
)

from constructs import Construct

class LambdaFunction(Stack):
    """
    Class deploying AWS Lambda Function

            Parameters
                    a) Stack: CDK Stack
            Returns
                    None
    """
    def __init__(self, scope: Construct, stack_id: str, **kwargs) -> None:
        super().__init__(scope, stack_id, **kwargs)

        _lambda.Function(
            self,
            "controller",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset(
                "bin/src/",
                bundling=core.BundlingOptions(
                    image=_lambda.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        "bash", "-c",
                        "pip install --no-cache -r requirements.txt -t /asset-output && cp -au . /asset-output"
                    ],
                ),    
            ),
            handler="index.controller",
        )