# ECS

## Describe Services
- Check if ManagedTags are enabled:
aws ecs describe-services --services <servicename> --cluster <clustername> --region <region> --query 'services[*].enableECSManagedTags' --output text<br>
[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-services.html)<br>