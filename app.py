
import aws_cdk as cdk

from deploy import stack

app = cdk.App()

stack.LambdaFunction(app, "lambda-router")
  
app.synth()
