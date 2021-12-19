import os
import sys
import time

# Last 10 seconds
average_router = 0
average_google = 0
sum_router=0
sum_google=0
idx = 0

max_ping_last10seconds_router = 0
max_ping_last10seconds_google = 0

local_max_router = 0
local_max_google = 0
google_packet_loss = 0
router_packet_loss = 0
sys.stdout.write('\n\n')
while(1):
    ping = os.popen('ping www.google.com -n 1')
    result = ping.readlines()
    
    ping2 = os.popen('ping 192.168.0.1 -n 1')
    result2 = ping2.readlines()
    local_ping=0
    try:
        google_ping = int(result[-1].strip().split(' = ')[-1].replace("ms"," "),10)
 
    except:
        google_packet_loss = google_packet_loss+1 
        google_ping=0
        pass
     
    try:
        local_ping = int(result2[-1].strip().split(' = ')[-1].replace("ms"," "),10)
    except:
        router_packet_loss = router_packet_loss+1
        google_ping=0
        pass   
        
    sum_google = sum_google+ google_ping
    sum_router = sum_router+ local_ping

    if google_ping>local_max_google:
        local_max_google = google_ping
        
    if local_ping>local_max_router:
        local_max_router= local_ping
        
            
    if idx% 20 == 0:
        average_google = sum_google/20
        average_router = sum_router/20
        sum_google = 0
        sum_router = 0
 
    if idx% 60 == 0:
        max_ping_last10seconds_router = local_max_router
        max_ping_last10seconds_google = local_max_google
        local_max_router = 0
        local_max_google = 0
        
    idx =  idx +1
    sys.stdout.write('google:{0}ms {1}ms  {2}ms router: {3}ms  {4}ms  {5}ms  google loss:{6}  router loss:{7}      \r'\
    .format(google_ping, average_google, max_ping_last10seconds_google, local_ping,average_router,max_ping_last10seconds_router,google_packet_loss,router_packet_loss))
    sys.stdout.flush()
    time.sleep(0.1)
