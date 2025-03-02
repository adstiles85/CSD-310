INSERT INTO SupplyOrder (SupplierID, WineID, QuantityOrdered, OrderDate, ExpectedDeliveryDate, ActualDeliveryDate, OrderStatus)
VALUES
-- Order from 'Glass Bottles Inc.' for Merlot
(1, 1, 1000, '2024-03-01', '2024-03-10', '2024-03-09', 'Delivered'),

-- Order from 'Label Masters' for Cabernet Sauvignon
(2, 2, 800, '2024-05-15', '2024-05-25', '2024-05-27', 'Delayed'),

-- Order from 'Vats & More Co.' for Chablis Classic
(3, 3, 600, '2024-08-20', '2024-08-30', '2024-08-30', 'Delivered'),

-- Order from 'Glass Bottles Inc.' for Chardonnay Reserve (Delayed Order)
(1, 4, 900, '2025-02-20', '2025-28-15', NULL, 'Pending');

-- Order from 'Label Masters' for Chablis Classic (Arrived Early)
(2, 3, 750, '2025-01-10', '2024-01-20', '2024-01-18', 'Delivered'),

-- Order from 'Vats & More Co.' for Cabernet Sauvignon (Arrived Late)
(3, 2, 500, '2024-01-15', '2024-01-25', '2024-01-26', 'Pending');


ALTER TABLE Wine 
MODIFY COLUMN WineType ENUM('Merlot', 'Cabernet', 'Chablis', 'Chardonnay', 'Pinot Noir', 'Blended Red Wine', 'Zinfandel', 'Syrah') NOT NULL;


INSERT INTO Wine (WineName, WineType, ProductionQuantity) 
VALUES 
('Pinot Noir Reserve', 'Pinot Noir', 350),
('Red Special Blend', 'Blended Red Wine', 450);


INSERT INTO Distributor (DistributorName, ContactInfo) 
VALUES 
('Prestige Wine Distributors', 'prestige@distributor.com'),
('Global Vines', 'global@distributor.com'),
('Heritage Wine Supply', 'heritage@distributor.com');


INSERT INTO WineDistributor (WineID, DistributorID) 
VALUES 
((SELECT WineID FROM Wine WHERE WineName = 'Pinot Noir Reserve'), 
 (SELECT DistributorID FROM Distributor WHERE DistributorName = 'Prestige Wine Distributors')),

((SELECT WineID FROM Wine WHERE WineName = 'Red Special Blend'), 
 (SELECT DistributorID FROM Distributor WHERE DistributorName = 'Global Vines')),

((SELECT WineID FROM Wine WHERE WineName = 'Red Special Blend'), 
 (SELECT DistributorID FROM Distributor WHERE DistributorName = 'Heritage Wine Supply'));


INSERT INTO Inventory (WineID, StockQuantity) 
VALUES 
((SELECT WineID FROM Wine WHERE WineName = 'Pinot Noir Reserve'), 350),
((SELECT WineID FROM Wine WHERE WineName = 'Red Special Blend'), 450);


INSERT INTO SalesTransaction (DistributorID, WineID, QuantitySold, SalePrice, SaleDate, PaymentStatus) 
VALUES 
-- Prestige Wine Distributors purchases Pinot Noir Reserve
((SELECT DistributorID FROM Distributor WHERE DistributorName = 'Prestige Wine Distributors'),
 (SELECT WineID FROM Wine WHERE WineName = 'Pinot Noir Reserve'),
  120, 18.99, '2024-07-15', 'Paid'),

-- Global Vines purchases Red Special Blend
((SELECT DistributorID FROM Distributor WHERE DistributorName = 'Global Vines'),
 (SELECT WineID FROM Wine WHERE WineName = 'Red Special Blend'),
  90, 22.50, '2024-09-10', 'Pending');