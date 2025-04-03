"""
SQL Export Module for Data Quality Framework
This module handles exporting data quality metrics and results to SQL Database
"""

import pandas as pd
import datetime
import json
from pyspark.sql import SparkSession

def write_to_sql_jdbc(spark, df, table_name, jdbc_url):
    """
    Write a DataFrame to SQL Server table using JDBC
    
    Parameters:
    - spark: SparkSession
    - df: DataFrame to export
    - table_name: Target SQL table name
    - jdbc_url: JDBC connection URL for SQL Server
    """
    try:
        # Write DataFrame to SQL Server table
        df.write \
          .format("jdbc") \
          .option("url", jdbc_url) \
          .option("dbtable", table_name) \
          .mode("append") \
          .save()
        
        print(f"Successfully exported data to {table_name} table using JDBC")
        return True
    except Exception as e:
        print(f"Error exporting to {table_name}: {str(e)}")
        return False

def export_metrics_to_sql(spark, run_id, profile_report, remediation_results, jdbc_url):
    """
    Export main metrics to DataQualityMetrics table
    
    Parameters:
    - spark: SparkSession
    - run_id: Unique identifier for this quality run
    - profile_report: Dictionary containing profile data
    - remediation_results: List of remediation results
    - jdbc_url: JDBC connection URL for SQL Server
    """
    try:
        # Calculate metrics
        total_issues = sum(item.get("violations_before", 0) for item in remediation_results)
        remediated_issues = sum(item.get("fixed_count", 0) for item in remediation_results)
        
        # Prepare metrics data
        metrics_data = [{
            'RunID': run_id,
            'DatasetName': 'adult_census',
            'RunDate': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'TotalRows': int(profile_report.get('total_rows', 0)),
            'TotalIssues': int(total_issues),
            'RemediatedIssues': int(remediated_issues),
            'CompletenessScore': float(profile_report.get('completeness_score', 0))
        }]
        
        # Create Spark DataFrame
        metrics_df = spark.createDataFrame(metrics_data)
        
        # Export to SQL
        return write_to_sql_jdbc(spark, metrics_df, "DataQualityMetrics", jdbc_url)
    except Exception as e:
        print(f"Error exporting metrics to SQL: {str(e)}")
        return False

def export_profiles_to_sql(spark, run_id, profile_report, jdbc_url):
    """
    Export column profiles to DataQualityProfiles table
    
    Parameters:
    - spark: SparkSession
    - run_id: Unique identifier for this quality run
    - profile_report: Dictionary containing profile data
    - jdbc_url: JDBC connection URL for SQL Server
    """
    try:
        # Process column profiles
        profiles_data = []
        
        for col_name, profile in profile_report.get('column_profiles', {}).items():
            # Handle avg value
            avg_value = profile.get('avg', 0)
            if isinstance(avg_value, str):
                try:
                    avg_value = float(avg_value)
                except:
                    avg_value = 0
            
            # Create profile entry
            profile_entry = {
                'RunID': run_id,
                'ColumnName': col_name,
                'DataType': profile.get('data_type', 'Unknown'),
                'NullCount': int(profile.get('null_count', 0)),
                'NullPercentage': float(profile.get('null_percentage', 0)),
                'DistinctCount': int(profile.get('distinct_count', 0)),
                'MinValue': str(profile.get('min', 'N/A')),
                'MaxValue': str(profile.get('max', 'N/A')),
                'AvgValue': float(avg_value)
            }
            profiles_data.append(profile_entry)
        
        # Create Spark DataFrame
        profiles_df = spark.createDataFrame(profiles_data)
        
        # Export to SQL
        return write_to_sql_jdbc(spark, profiles_df, "DataQualityProfiles", jdbc_url)
    except Exception as e:
        print(f"Error exporting profiles to SQL: {str(e)}")
        return False

def export_issues_to_sql(spark, run_id, rules, issues, jdbc_url):
    """
    Export issues to DataQualityIssues table
    
    Parameters:
    - spark: SparkSession
    - run_id: Unique identifier for this quality run
    - rules: List of rules applied
    - issues: List of issues found
    - jdbc_url: JDBC connection URL for SQL Server
    """
    try:
        # Prepare issues data
        issues_data = []
        
        for issue in issues:
            # Create issue entry
            issue_entry = {
                'RunID': run_id,
                'RuleName': issue.get('rule_name', issue.get('rule_id', 'Unknown')),
                'ColumnName': issue.get('column_name', 'Unknown'),
                'IssueCount': int(issue.get('issue_count', 0)),
                'Severity': issue.get('severity', 'MEDIUM'),
                'Status': issue.get('status', 'Open')
            }
            issues_data.append(issue_entry)
        
        if issues_data:
            # Create Spark DataFrame
            issues_df = spark.createDataFrame(issues_data)
            
            # Export to SQL
            return write_to_sql_jdbc(spark, issues_df, "DataQualityIssues", jdbc_url)
        return True
    except Exception as e:
        print(f"Error exporting issues to SQL: {str(e)}")
        return False

def export_rules_to_sql(spark, run_id, rules, jdbc_url):
    """
    Export rules to DataQualityRules table
    
    Parameters:
    - spark: SparkSession
    - run_id: Unique identifier for this quality run
    - rules: List of rules applied
    - jdbc_url: JDBC connection URL for SQL Server
    """
    try:
        # Prepare rules data
        rules_data = []
        
        for rule in rules:
            rule_entry = {
                'RunID': run_id,
                'RuleName': rule.get('rule_name', 'Unknown'),
                'RuleDescription': rule.get('description', ''),
                'ColumnName': rule.get('column', 'Unknown'),
                'Severity': rule.get('severity', 'MEDIUM')
            }
            rules_data.append(rule_entry)
        
        # Create Spark DataFrame
        rules_df = spark.createDataFrame(rules_data)
        
        # Export to SQL
        return write_to_sql_jdbc(spark, rules_df, "DataQualityRules", jdbc_url)
    except Exception as e:
        print(f"Error exporting rules to SQL: {str(e)}")
        return False

def integrate_sql_export(spark, profile_report, remediation_results, run_id, rules, jdbc_url):
    """
    Export all data quality metrics to SQL Database
    
    Parameters:
    - spark: SparkSession
    - profile_report: Dictionary containing profile data
    - remediation_results: List of remediation results
    - run_id: Unique identifier for this quality run
    - rules: List of rules applied 
    - jdbc_url: JDBC connection URL for SQL Server
    """
    print("Starting SQL export...")
    
    try:
        # Export metrics
        metrics_success = export_metrics_to_sql(spark, run_id, profile_report, remediation_results, jdbc_url)
        
        # Export profiles
        profiles_success = export_profiles_to_sql(spark, run_id, profile_report, jdbc_url)
        
        # Export issues
        issues_data = []
        for rule in rules:
            for result in remediation_results:
                if result["rule_id"] == rule["rule_id"]:
                    issues_data.append({
                        "rule_id": rule["rule_id"],
                        "rule_name": rule["rule_name"],
                        "column_name": rule["column"],
                        "issue_count": result["violations_before"],
                        "severity": rule["severity"],
                        "status": "Remediated" if result["fixed_count"] > 0 else "Open"
                    })
        
        issues_success = export_issues_to_sql(spark, run_id, rules, issues_data, jdbc_url)
        
        # Export rules
        rules_success = export_rules_to_sql(spark, run_id, rules, jdbc_url)
        
        if metrics_success and profiles_success and issues_success and rules_success:
            print("SQL export completed successfully.")
        else:
            print("Some SQL exports were not successful. Check the error messages above.")
        
        return metrics_success and profiles_success and issues_success and rules_success
        
    except Exception as e:
        print(f"Error during SQL export: {str(e)}")
        return False