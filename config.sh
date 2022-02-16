# aws sts assume-role --role-arn arn:aws:iam::$accountid:role/$rolename --role-session-name jenkins-agent --duration-seconds 3600 --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text
# aws sts get-caller-identity

export $(
printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" $(
aws sts assume-role --role-arn arn:aws:iam::$accountid:role/$rolename --role-session-name jenkins-agent --duration-seconds 3600 --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text
)
)
terraform init
terraform plan -var 'region=$region'
terraform apply -var 'region=$region' --auto-approve
