ec2_instances = [{
    "instance_name": "Web-server",
    "instance_type": "t3.large",
    "public_ip": "54.32.109.4"
},
{
    "instance_name": "Backend-server",
    "instance_type": "m5.large",
    "public_ip": "21.45.98.101"
},
{
    "instance_name": "Database-server",
    "instance_type": "r5.xlarge",
    "public_ip": "102.1.82.49"
}]


# ec2_instance = ["Web-server", "t3.large", "54.32.109.4"]
# print(ec2_instance[2])

print(ec2_instances[2]["instance_type"])