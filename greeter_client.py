from __future__ import print_function
from const import *
import logging

import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    conn = grpc.insecure_channel(SERVER+':'+PORT)
    stub = calculator_pb2_grpc.GreeterStub(conn)
    print("Escreva dois numeros:")

    a = float(input())

    b = float(input())

    print (a, '+', b, '=', stub.add(calculator_pb2.CalculatorRequest(a=a,b=b)).resp)

    print (a, '-', b, '=', stub.subtract(calculator_pb2.CalculatorRequest(a=a,b=b)).resp)

    print (a, '*', b, '=', stub.multiply(calculator_pb2.CalculatorRequest(a=a,b=b)).resp)

    print (a, '/', b, '=', stub.divide(calculator_pb2.CalculatorRequest(a=a,b=b)).resp)



if __name__ == '__main__':
    logging.basicConfig()
    run()
