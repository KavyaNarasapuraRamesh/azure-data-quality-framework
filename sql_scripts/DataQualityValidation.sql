CREATE TABLE DataQualityValidation (
    ValidationID INT PRIMARY KEY,
    RunID VARCHAR(255),
    DatasetName VARCHAR(255),
    ValidationDate DATETIME,
    CleanlinessScore FLOAT,
    CleanlinessStatus VARCHAR(50),
    RemainingIssuesCount INT,
    CertificationFlag BIT
);
