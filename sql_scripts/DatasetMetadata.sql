CREATE TABLE DatasetMetadata (
    DatasetID INT PRIMARY KEY,
    DatasetName VARCHAR(255),
    DateAdded DATETIME,
    LastProcessed DATETIME,
    LatestRunID VARCHAR(255),
    TotalRows INT,
    ColumnCount INT,
    TotalIssues INT,
    CompletenessScore FLOAT,
    Status VARCHAR(50),
    Description VARCHAR(255)
);
