#!/bin/ksh

aws lambda create-function \
--cli-input-json file:///home/prashant/python_code/src/aws_lambda/invocation_functions/cliscripts/cli_lambda_input_worker_function.json

