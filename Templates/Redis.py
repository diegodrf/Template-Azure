class Metrics:
    #Provider
    providers = 'Microsoft.Cache/Redis/'

    #Metrics
    cacheLatency = ['cacheLatency', 'Maximum']
    cacheRead = [
        'cacheRead,cacheRead0,cacheRead1,cacheRead2,cacheRead3,cacheRead4,cacheRead5,cacheRead6,cacheRead7,cacheRead8,cacheRead9',
        'Maximum']
    cacheWrite = [
        'cacheWrite,cacheWrite0,cacheWrite1,cacheWrite2,cacheWrite3,cacheWrite4,cacheWrite5,cacheWrite6,cacheWrite7,cacheWrite8,cacheWrite9',
        'Maximum']
    cachehits = [
        'cachehits,cachehits0,cachehits1,cachehits2,cachehits3,cachehits4,cachehits5,cachehits6,cachehits7,cachehits8,cachehits9',
        'Total']
    cachemisses = [
        'cachemisses,cachemisses0,cachemisses1,cachemisses2,cachemisses3,cachemisses4,cachemisses5,cachemisses6,cachemisses7,cachemisses8,cachemisses9',
        'Total']
    connectedclients = [
        'connectedclients,connectedclients0,connectedclients1,connectedclients2,connectedclients3,connectedclients4,connectedclients5,connectedclients6,connectedclients7,connectedclients8,connectedclients9',
        'Maximum']
    errors = ['errors', 'Maximum']
    evictedkeys = [
        'evictedkeys,evictedkeys0,evictedkeys1,evictedkeys2,evictedkeys3,evictedkeys4,evictedkeys5,evictedkeys6,evictedkeys7,evictedkeys8,evictedkeys9',
        'Total']
    expiredkeys = [
        'expiredkeys,expiredkeys0,expiredkeys1,expiredkeys2,expiredkeys3,expiredkeys4,expiredkeys5,expiredkeys6,expiredkeys7,expiredkeys8,expiredkeys9',
        'Total']
    getcommands = [
        'getcommands,getcommands0,getcommands1,getcommands2,getcommands3,getcommands4,getcommands5,getcommands6,getcommands7,getcommands8,getcommands9',
        'Total']
    operationsPerSecond = [
        'operationsPerSecond,operationsPerSecond0,operationsPerSecond1,operationsPerSecond2,operationsPerSecond3,operationsPerSecond4,operationsPerSecond5,operationsPerSecond6,operationsPerSecond7,operationsPerSecond8,operationsPerSecond9',
        'Total']
    percentProcessorTime = [
        'percentProcessorTime,percentProcessorTime0,percentProcessorTime1,percentProcessorTime2,percentProcessorTime3,percentProcessorTime4,percentProcessorTime5,percentProcessorTime6,percentProcessorTime7,percentProcessorTime8,percentProcessorTime9',
        'Maximum']
    serverLoad = [
        'serverLoad,serverLoad0,serverLoad1,serverLoad2,serverLoad3,serverLoad4,serverLoad5,serverLoad6,serverLoad7,serverLoad8,serverLoad9',
        'Maximum']
    setcommands = [
        'setcommands,setcommands0,setcommands1,setcommands2,setcommands3,setcommands4,setcommands5,setcommands6,setcommands7,setcommands8,setcommands9',
        'Total']
    totalcommandsprocessed = [
        'totalcommandsprocessed,totalcommandsprocessed0,totalcommandsprocessed1,totalcommandsprocessed2,totalcommandsprocessed3,totalcommandsprocessed4,totalcommandsprocessed5,totalcommandsprocessed6,totalcommandsprocessed7,totalcommandsprocessed8,totalcommandsprocessed9',
        'Total']
    totalkeys = [
        'totalkeys,totalkeys0,totalkeys1,totalkeys2,totalkeys3,totalkeys4,totalkeys5,totalkeys6,totalkeys7,totalkeys8,totalkeys9',
        'Maximum']
    usedmemory = [
        'usedmemory,usedmemory0,usedmemory1,usedmemory2,usedmemory3,usedmemory4,usedmemory5,usedmemory6,usedmemory7,usedmemory8,usedmemory9',
        'Maximum']
    usedmemoryRss = [
        'usedmemoryRss,usedmemoryRss0,usedmemoryRss1,usedmemoryRss2,usedmemoryRss3,usedmemoryRss4,usedmemoryRss5,usedmemoryRss6,usedmemoryRss7,usedmemoryRss8,usedmemoryRss9',
        'Maximum']
    usedmemorypercentage = ['usedmemorypercentage', 'Maximum']

    items = [cacheLatency, cacheRead, cacheWrite, cachehits, cachemisses, connectedclients, errors, evictedkeys,
             expiredkeys, getcommands,
             operationsPerSecond, percentProcessorTime, serverLoad, setcommands, totalcommandsprocessed, totalkeys,
             usedmemory,
             usedmemoryRss, usedmemorypercentage]