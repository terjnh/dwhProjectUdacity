import configparser
import pandas as pd
config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))

DWH_CLUSTER_TYPE       = config.get("DWH","DWH_CLUSTER_TYPE")
DWH_NUM_NODES          = config.get("DWH","DWH_NUM_NODES")
DWH_NODE_TYPE          = config.get("DWH","DWH_NODE_TYPE")
DWH_CLUSTER_IDENTIFIER = config.get("DWH","DWH_CLUSTER_IDENTIFIER")
DWH_IAM_ROLE_NAME      = config.get("DWH", "DWH_IAM_ROLE_NAME")

IAM_ROLE               = config.get("IAM_ROLE", "ARN")

CLUSTER_HOST           = config.get("CLUSTER", "HOST")
CLUSTER_DB_NAME        = config.get("CLUSTER", "DB_NAME")
CLUSTER_DB_USER        = config.get("CLUSTER", "DB_USER")
CLUSTER_DB_PASSWORD    = config.get("CLUSTER", "DB_PASSWORD")
CLUSTER_DB_PORT        = config.get("CLUSTER", "DB_PORT")


df = pd.DataFrame({"Param":
                  ["DWH_CLUSTER_TYPE", "DWH_NUM_NODES", "DWH_NODE_TYPE", "DWH_CLUSTER_IDENTIFIER", "DWH_IAM_ROLE_NAME", "IAM_ROLE", "CLUSTER_HOST", "CLUSTER_DB_NAME", "CLUSTER_DB_USER", "CLUSTER_DB_PASSWORD", "CLUSTER_DB_PORT"],
              "Value":
                  [DWH_CLUSTER_TYPE, DWH_NUM_NODES, DWH_NODE_TYPE, DWH_CLUSTER_IDENTIFIER, DWH_IAM_ROLE_NAME, IAM_ROLE, CLUSTER_HOST, CLUSTER_DB_NAME, CLUSTER_DB_USER, CLUSTER_DB_PASSWORD, CLUSTER_DB_PORT]
             })

print(df)