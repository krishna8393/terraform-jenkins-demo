aws sts assume-role --role-arn arn:aws:iam::$accountid:role/$rolename --role-session-name jenkins-agent --duration-seconds 3600 --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text
aws sts get-caller-identity
