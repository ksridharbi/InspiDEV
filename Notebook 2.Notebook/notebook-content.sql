-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "sqldatawarehouse"
-- META   },
-- META   "dependencies": {
-- META     "warehouse": {
-- META       "default_warehouse": "3c6734ab-a541-454e-b13d-f58e6c5b286d",
-- META       "known_warehouses": [
-- META         {
-- META           "id": "3c6734ab-a541-454e-b13d-f58e6c5b286d",
-- META           "type": "MountedWarehouse"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Welcome to your new notebook
-- Type here in the cell editor to add code!


-- METADATA ********************

-- META {
-- META   "language": "python",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

SELECT TOP (100) [ProductID],
			[CompanyName],
			[TotalOrderQty]
FROM [DEVDB].[SupplyChain].[vProductsBySupplier]

-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }
