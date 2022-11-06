import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_book_cdk.serverless_book_cdk_stack import ServerlessBookCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_book_cdk/serverless_book_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessBookCdkStack(app, "serverless-book-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
