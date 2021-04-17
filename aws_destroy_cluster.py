# 3. Destroying the cluster
# After the ETL process done, nor whenever you want, 
# you can destroy it with a single command: python aws_destroy_cluster.py

from aws_create_cluster import config_parse_file, aws_client, check_cluster_creation, \
    config_persist_cluster_infos, destroy_redshift_cluster, get_redshift_cluster_status


def main():
    config_parse_file()

    redshift = aws_client('redshift', "us-east-2")

    if check_cluster_creation(redshift):
        print('cluster available')
        destroy_redshift_cluster(redshift)
        print('New redshift cluster status: ')
        print(get_redshift_cluster_status(redshift))
    else:
        print('not yet...')


if __name__ == '__main__':
    main()