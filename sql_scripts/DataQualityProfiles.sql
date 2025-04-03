CREATE TABLE DataQualityProfiles (
    ID INT PRIMARY KEY,
    RunID VARCHAR(255),
    ColumnName VARCHAR(255),
    DataType VARCHAR(50),
    NullCount INT,
    NullPercentage FLOAT,
    DistinctCount INT,
    MinValue VARCHAR(255),
    MaxValue VARCHAR(255),
    AvgValue FLOAT
);
