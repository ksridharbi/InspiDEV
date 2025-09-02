
 /* Create View that will be used in the SQL GraphQL Endpoint */
CREATE VIEW SupplyChain.vProductsbySuppliers AS
SELECT COUNT(a.ProductID) AS ProductCount
, a.SupplierLocationID
, b.CompanyName
FROM SupplyChain.Warehouse AS a
INNER JOIN dbo.Suppliers AS b ON a.SupplierID = b.SupplierID
GROUP BY a.SupplierLocationID, b.CompanyName;

GO

