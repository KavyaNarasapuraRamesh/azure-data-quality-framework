CREATE TABLE DataQualityRules (
    ID INT PRIMARY KEY,
    RunID VARCHAR(255),
    RuleName VARCHAR(255),
    RuleDescription VARCHAR(500),
    ColumnName VARCHAR(255),
    Severity VARCHAR(50)
);
