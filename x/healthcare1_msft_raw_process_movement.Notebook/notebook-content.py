# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ffb375ef-a3f9-4bc1-b918-04c42f2d71d6",
# META       "default_lakehouse_name": "healthcare1_msft_bronze",
# META       "default_lakehouse_workspace_id": "15e8bd13-cceb-4532-b440-2880c41b4cd0"
# META     },
# META     "environment": {
# META       "environmentId": "1e85783e-9622-8814-4f3b-9ceedbca9234",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### WARNING
# The following notebook is intended to be read only. Please do not modify the contents of this notebook.


# CELL ********************

%run healthcare1_msft_config_notebook

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

%run healthcare1_msft_config_notebook {"enable_spark_setup" : true, "enable_packages_mount" : false}

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# PARAMETERS CELL ********************

inline_params = "{}"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

from microsoft.fabric.hls.hds.services.file_orchestration_service import FileOrchestrationService
import json

# convert inline params into dictionary
inline_params_dict = json.loads(inline_params)

service = FileOrchestrationService(spark, 
                workspace_name=workspace_name,
                solution_name=solution_name,
                admin_lakehouse_name=administration_database_name,
                inline_params=inline_params_dict,
                one_lake_endpoint=one_lake_endpoint)

service.run()

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

mssparkutils.fs.unmount(packages_mount_name)

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }
