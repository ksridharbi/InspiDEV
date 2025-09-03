# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1f5ab556-777d-4994-bfd6-a86c40e8aa38",
# META       "default_lakehouse_name": "MyLakehouse",
# META       "default_lakehouse_workspace_id": "15e8bd13-cceb-4532-b440-2880c41b4cd0",
# META       "known_lakehouses": [
# META         {
# META           "id": "1f5ab556-777d-4994-bfd6-a86c40e8aa38"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE Attendance (
# MAGIC     AttendanceID INT,
# MAGIC     EmployeeName STRING,
# MAGIC     EmployeeEmail STRING,
# MAGIC     AttendanceDate DATE,
# MAGIC     Status STRING
# MAGIC ) USING DELTA;


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE TABLE attendance;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
