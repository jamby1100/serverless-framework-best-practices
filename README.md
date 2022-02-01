# Serverless Blackbelt


```sh
python3 -m venv venv
source venv/bin/activate

pip install boto3
```

Enter the python console and create the following parameter store by using the `python` command or `AWS_PROFILE=profile python`

```py

import boto3

client = boto3.client('ssm', region_name="ap-southeast-1")

# define for DEV
client.put_parameter(Name="/sf-blackbelt/dev/DB_USER", Value="dev-admin", Type="String", Overwrite=True)
client.put_parameter(Name="/sf-blackbelt/dev/DB_PASSWORD", Value="dev_secure_password", Type="String", Overwrite=True)

# define for UAT
client.put_parameter(Name="/sf-blackbelt/uat/DB_USER", Value="uat-admin", Type="String", Overwrite=True)
client.put_parameter(Name="/sf-blackbelt/uat/DB_PASSWORD", Value="uat_secure_password", Type="String", Overwrite=True)
```# serverless-framework-best-practices
