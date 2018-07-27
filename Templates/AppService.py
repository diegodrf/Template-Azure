class Metrics:
    #Provider
    providers = 'Microsoft.Web/sites'

    #Metric
    CpuTime = ['CpuTime', 'Total']  # Unit = Seconds // Name = CPU Time
    Requests = ['Requests', 'Total']  # Unit = Count // Name = Requests
    BytesReceived = ['BytesReceived', 'Total']  # Unit = Bytes // Name = Data In
    BytesSent = ['BytesSent', 'Total']  # Unit = Bytes // Name = Data Out
    Http101 = ['Http101', 'Total']  # Unit = Count // Name = Http 101
    Http2xx = ['Http2xx', 'Total']  # Unit = Count // Name = Http 2xx
    Http3xx = ['Http3xx', 'Total']  # Unit = Count // Name = Http 3xx
    Http401 = ['Http401', 'Total']  # Unit = Count // Name = Http 401
    Http403 = ['Http403', 'Total']  # Unit = Count // Name = Http 403
    Http404 = ['Http404', 'Total']  # Unit = Count // Name = Http 404
    Http406 = ['Http406', 'Total']  # Unit = Count // Name = Http 406
    Http4xx = ['Http4xx', 'Total']  # Unit = Count // Name = Http 4xx
    Http5xx = ['Http5xx', 'Total']  # Unit = Count // Name = Http Server Errors
    MemoryWorkingSet = ['MemoryWorkingSet', 'Average']  # Unit = Bytes // Name = Memory working set
    AverageMemoryWorkingSet = ['AverageMemoryWorkingSet',
                               'Average']  # Unit = Bytes // Name = Average memory working set
    AverageResponseTime = ['AverageResponseTime', 'Average']  # Unit = Seconds // Name = Average Response Time
    AppConnections = ['AppConnections', 'Average']  # Unit = Count // Name = Connections
    Handles = ['Handles', 'Average']  # Unit = Count // Name = Handle Count
    Threads = ['Threads', 'Average']  # Unit = Count // Name = Thread Count
    PrivateBytes = ['PrivateBytes', 'Average']  # Unit = Bytes // Name = Private Bytes
    IoReadBytesPerSecond = ['IoReadBytesPerSecond', 'Total']  # Unit = BytesPerSecond // Name = IO Read Bytes Per Second
    IoWriteBytesPerSecond = ['IoWriteBytesPerSecond',
                             'Total']  # Unit = BytesPerSecond // Name = IO Write Bytes Per Second
    IoOtherBytesPerSecond = ['IoOtherBytesPerSecond',
                             'Total']  # Unit = BytesPerSecond // Name = IO Other Bytes Per Second
    IoReadOperationsPerSecond = ['IoReadOperationsPerSecond',
                                 'Total']  # Unit = BytesPerSecond // Name = IO Read Operations Per Second
    IoWriteOperationsPerSecond = ['IoWriteOperationsPerSecond',
                                  'Total']  # Unit = BytesPerSecond // Name = IO Write Operations Per Second
    IoOtherOperationsPerSecond = ['IoOtherOperationsPerSecond',
                                  'Total']  # Unit = BytesPerSecond // Name = IO Other Operations Per Second
    RequestsInApplicationQueue = ['RequestsInApplicationQueue',
                                  'Average']  # Unit = Count // Name = Requests In Application Queue
    CurrentAssemblies = ['CurrentAssemblies', 'Average']  # Unit = Count // Name = Current Assemblies
    TotalAppDomains = ['TotalAppDomains', 'Average']  # Unit = Count // Name = Total App Domains
    TotalAppDomainsUnloaded = ['TotalAppDomainsUnloaded',
                               'Average']  # Unit = Count // Name = Total App Domains Unloaded
    Gen0Collections = ['Gen0Collections', 'Total']  # Unit = Count // Name = Gen 0 Garbage Collections
    Gen1Collections = ['Gen1Collections', 'Total']  # Unit = Count // Name = Gen 1 Garbage Collections
    Gen2Collections = ['Gen2Collections', 'Total']  # Unit = Count // Name = Gen 2 Garbage Collections
    items = [CpuTime, Requests, BytesReceived, BytesSent, Http101, Http2xx, Http3xx, Http401, Http403, Http404, Http406,
            Http4xx, Http5xx, MemoryWorkingSet, AverageMemoryWorkingSet, AverageResponseTime, AppConnections, Handles,
            Threads, PrivateBytes, IoReadBytesPerSecond, IoWriteBytesPerSecond, IoOtherBytesPerSecond,
            IoReadOperationsPerSecond, IoWriteOperationsPerSecond, IoOtherOperationsPerSecond,
            RequestsInApplicationQueue, CurrentAssemblies, TotalAppDomains, TotalAppDomainsUnloaded, Gen0Collections,
            Gen1Collections, Gen2Collections]