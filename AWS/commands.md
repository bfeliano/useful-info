# ECS

## Execute Command
**- Connect to ECS task:**<br>
*aws ecs execute-command --cluster cluster name --task task id --container container name --interactive --command "/bin/sh"*<br>
[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ecs/execute-command.html)<br>

## Describe Services
**- Check if ManagedTags are enabled:**<br>
*aws ecs describe-services --services servicename --cluster clustername --region region --query 'services[\*].enableECSManagedTags' --output text*<br>
[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-services.html)<br>


# SSM

## Put Parameter
**- Creation of SSM parameter:**<br>
*aws ssm put-parameter --name parametername --value 'value' --type SecureString --tags Key=key,Value=value Key=key,Value=value*<br>
[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ssm/put-parameter.html)<br>


# S3

## Delete Object
**- Delete one object:**<br>
*aws s3api delete-object --bucket bucketname --key objectname*<br><br>
**- Delete multiple object:**<br>
*aws s3api delete-objects --bucket <bucketname> --delete '{"Objects":[{"Key":"object name"},{"Key":"object name"}]}'*<br>
[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ssm/put-parameter.html)<br>