class Metrics:
    # Provider
    providers = 'Microsoft.Compute/virtualMachines/'

    # Metrics
    PercentageCPU = ['Percentage CPU', 'Average']
    NetworkIn = ['Network In', 'Total']
    NetworkOut = ['Network Out', 'Total']
    DiskReadBytes = ['Disk Read Bytes', 'Total']
    DiskWriteBytes = ['Disk Write Bytes', 'Total']
    DiskReadOperationsSec = ['Disk Read Operations/Sec', 'Average']
    DiskWriteOperationsSec = ['Disk Write Operations/Sec', 'Average']
    CPUCreditsRemaining = ['CPU Credits Remaining', 'Average']
    CPUCreditsConsumed = ['CPU Credits Consumed', 'Average']
    PerDiskReadBytessec = ['Per Disk Read Bytes/sec', 'Average']
    PerDiskWriteBytessec = ['Per Disk Write Bytes/sec', 'Average']
    PerDiskReadOperationsSec = ['Per Disk Read Operations/Sec', 'Average']
    PerDiskWriteOperationsSec = ['Per Disk Write Operations/Sec', 'Average']
    PerDiskQD = ['Per Disk QD', 'Average']
    OSPerDiskReadBytessec = ['OS Per Disk Read Bytes/sec', 'Average']
    OSPerDiskWriteBytessec = ['OS Per Disk Write Bytes/sec', 'Average']
    OSPerDiskReadOperationsSec = ['OS Per Disk Read Operations/Sec', 'Average']
    OSPerDiskWriteOperationsSec = ['OS Per Disk Write Operations/Sec', 'Average']
    OSPerDiskQD = ['OS Per Disk QD', 'Average']

    items = [PercentageCPU,
             NetworkIn,
             NetworkOut,
             DiskReadBytes,
             DiskWriteBytes,
             DiskReadOperationsSec,
             DiskWriteOperationsSec,
             CPUCreditsRemaining,
             CPUCreditsConsumed,
             PerDiskReadBytessec,
             PerDiskWriteBytessec,
             PerDiskReadOperationsSec,
             PerDiskWriteOperationsSec,
             PerDiskQD,
             OSPerDiskReadBytessec,
             OSPerDiskWriteBytessec,
             OSPerDiskReadOperationsSec,
             OSPerDiskWriteOperationsSec,
             OSPerDiskQD]