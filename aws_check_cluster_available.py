from aws_create_cluster import config_parse_file, aws_client, aws_open_redshift_port, check_cluster_creation, aws_resource, config_persist_cluster_infos


# This one you should run several times 
# until your cluster becomes available - takes from 3 to 6 minutes:
# python aws_check_cluster_available.py

def main():
    config_parse_file()

    redshift = aws_client('redshift', "us-east-2")

    if check_cluster_creation(redshift):
        print('cluster available!')
        # Create an AWS client resource
        ec2 = aws_resource('ec2', 'us-east-2')
        # Write back to the dwh.cfg configuration file the cluster endpoint and IAM ARN
        config_persist_cluster_infos(redshift)
        # Open the Redshift port on the VPC security group.
        aws_open_redshift_port(ec2, redshift)
    else:
        print('Not Yet...')


if __name__ == '__main__':
    main()