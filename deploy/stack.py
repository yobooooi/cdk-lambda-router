"""Deployment module of custon CDK constructs"""

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
            ),
            handler="index.controller",
        )
