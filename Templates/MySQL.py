class Metrics:
    # Provider
    providers = 'Microsoft.DBforMySQL/servers/'

    # Metrics
    cpu_percent = ['cpu_percent', 'Average']
    memory_percent = ['memory_percent', 'Average']
    io_consumption_percent = ['io_consumption_percent', 'Average']
    storage_percent = ['storage_percent', 'Average']
    storage_used = ['storage_used', 'Average']
    storage_limit = ['storage_limit', 'Average']
    serverlog_storage_percent = ['serverlog_storage_percent', 'Average']
    serverlog_storage_usage = ['serverlog_storage_usage', 'Average']
    serverlog_storage_limit = ['serverlog_storage_limit', 'Average']
    active_connections = ['active_connections', 'Average']
    connections_failed = ['connections_failed', 'Total']
    seconds_behind_master = ['seconds_behind_master', 'Average']
    network_bytes_egress = ['network_bytes_egress', 'Total']
    network_bytes_ingress = ['network_bytes_ingress', 'Total']

    items = [cpu_percent,
             memory_percent,
             io_consumption_percent,
             storage_percent,
             storage_used,
             storage_limit,
             serverlog_storage_percent,
             serverlog_storage_usage,
             serverlog_storage_limit,
             active_connections,
             connections_failed,
             seconds_behind_master,
             network_bytes_egress,
             network_bytes_ingress]