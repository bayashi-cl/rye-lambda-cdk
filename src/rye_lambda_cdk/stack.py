import cdk_pyproject
from aws_cdk import RemovalPolicy, Stack, aws_lambda, aws_logs
from constructs import Construct


class RyeLambdaCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
        runtime = aws_lambda.Runtime.PYTHON_3_12

        project = cdk_pyproject.PyProject.from_rye(runtime, ".")

        app = aws_lambda.Function(
            self,
            "AppFunction",
            code=project.code("lambda-app"),
            handler="lambda_app.handler",
            runtime=runtime,
            layers=[],
        )
        aws_logs.LogGroup(
            self,
            "AppLogGroup",
            log_group_name=f"/aws/lambda/{app.function_name}",
            removal_policy=RemovalPolicy.DESTROY,
        )
