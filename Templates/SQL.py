class Metrics:
    #Provider
    providers = 'Microsoft.Sql/servers/'

    #Metrics
    blocked_by_firewall = ['blocked_by_firewall', 'Total']  # Count - Blocked by Firewall
    connection_failed = ['connection_failed', 'Total']  # Count - Failed Connections
    connection_successful = ['connection_successful', 'Total']  # Count - Successful Connections
    cpu_limit = ['cpu_limit', 'Average']  # Count - CPU limit
    cpu_percent = ['cpu_percent', 'Average']  # Percent - CPU percentage
    cpu_used = ['cpu_used', 'Average']  # Count - CPU used
    deadlock = ['deadlock', 'Total']  # Count - Deadlock
    dtu_consumption_percent = ['dtu_consumption_percent', 'Average']  # Percent - DTU percentage
    dtu_limit = ['dtu_limit', 'Average']  # Count - DTU Limit
    dtu_used = ['dtu_used', 'Average']  # Count - DTU used
    log_write_percent = ['log_write_percent', 'Average']  # Percent - Log IO percentage
    physical_data_read_percent = ['physical_data_read_percent', 'Average']  # Percent - Data IO percentage
    sessions_percent = ['sessions_percent', 'Average']  # Percent - Sessions percentage
    storage = ['storage', 'Maximum']  # Bytes - Total database size
    storage_percent = ['storage_percent', 'Maximum']  # Percent - Database size percentage
    workers_percent = ['workers_percent', 'Average']  # Percent - Workers percentage
    xtp_storage_percent = ['xtp_storage_percent', 'Average']  # Percent - In-Memory OLTP storage percent

    items = [blocked_by_firewall,
             connection_failed,
             connection_successful,
             cpu_limit, cpu_percent,
             cpu_used, deadlock,
             dtu_consumption_percent,
             dtu_limit, dtu_used,
             log_write_percent,
             physical_data_read_percent,
             sessions_percent,
             storage,
             storage_percent,
             workers_percent,
             xtp_storage_percent]