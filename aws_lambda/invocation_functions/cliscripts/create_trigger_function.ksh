#!/bin/ksh


## Creates a schedule
aws events put-rule --name Invoke_SSH_Event_15_mins \
--schedule-expression "rate(15 minutes)" \
--state DISABLED

aws lambda create-function \
--cli-input-json file:///home/prashant/python_code/src/aws_lambda/invocation_functions/cliscripts/cli_lambda_input_trigger_function.json \
--zip-file fileb:///home/prashant/python_code/src/aws_lambda/invocation_functions/ssh_trigger_function.zip

#aws lambda update-function-code \
#--function-name ssh_trigger_function \
#--zip-file fileb:///home/prashant/python_code/src/aws_lambda/invocation_functions/ssh_trigger_function.zip

# Associating the schedule to the function and allowing only the schedule to execute the function
aws lambda add-permission \
        --function-name ssh_trigger_function \
        --statement-id Invoke_SSH_Event_15_mins \
        --action lambda:InvokeFunction \
        --principal events.amazonaws.com \
        --source-arn 'arn:aws:events:ap-south-1:973265861767:rule/Invoke_SSH_Event_15_mins'

## Adding lambda as a target to the schedule rule
aws events put-targets --rule Invoke_SSH_Event_15_mins \
        --targets "Id"="1","Arn"="arn:aws:lambda:ap-south-1:973265861767:function:ssh_trigger_function"

