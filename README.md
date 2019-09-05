# Demo Serverless - Exposing Lambdas with API Gateway

Code used as example on a introdutory talk about serverlerss architecture and the serverless framework


## Downloading Serverless Framework
> npm install -g serverless

## Deploying to AWS
> serverless --stage dev

## Invoking Funcion
* ### Invoking on AWS
> serverless invoke --stage dev --function add_fixed_value --path example_requests/request.json

* ### Invoking Lambda locally
> serverless invoke local --stage dev --function sub_fixed_value --path example_requests/request.json