CREATE TABLE DataQualityIssues (
    ID INT PRIMARY KEY,
    RunID VARCHAR(255),
    RuleName VARCHAR(255),
    ColumnName VARCHAR(255),
    IssueCount INT,
    Severity VARCHAR(50),
    Status VARCHAR(50)
);
