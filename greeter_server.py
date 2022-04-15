from concurrent import futures
from const import *
import logging

import grpc
import calculator_pb2
import calculator_pb2_grpc


class Greeter(calculator_pb2_grpc.GreeterServicer):

    def add(self, request, context):
        return calculator_pb2.CalculatorReply(resp=request.a+request.b)
    def subtract(self, request, context):
        return calculator_pb2.CalculatorReply(resp=request.a-request.b)
    def multiply(self, request, context):
        return calculator_pb2.CalculatorReply(resp=request.a*request.b);
    def divide(self, request, context):
        return calculator_pb2.CalculatorReply(resp=request.a/request.b);


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:'+PORT)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
