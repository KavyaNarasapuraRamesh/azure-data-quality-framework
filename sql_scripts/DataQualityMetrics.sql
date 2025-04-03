CREATE TABLE DataQualityMetrics (
    RunID VARCHAR(255) PRIMARY KEY,
    DatasetName VARCHAR(255),
    RunDate DATETIME,
    TotalRows INT,
    TotalIssues INT,
    CompletenessScore FLOAT,
    RemediatedIssues INT
);
