REM ######Application Information
sc config Appinfo start=auto
REM ######AppX Deployment Service (AppXSVC)
sc config AppXSvc start=auto
REM ######AVCTP service
sc config BthAvctpSvc start=auto
REM ######Background Tasks Infrastructure Service
sc config BrokerInfrastructure start=auto
REM ######Base Filtering Engine
sc config BFE start=auto
REM ######Capability Access Manager Service
sc config camsvc start=auto
REM ######Client License Service (ClipSVC)
sc config ClipSVC start=auto
REM ######CoreMessaging
sc config CoreMessagingRegistrar start=auto
REM ######Cryptographic Services
sc config CryptSvc start=auto
REM ######CyberGhost 7 Service
sc config CG7Service start=auto
REM ######DCOM Server Process Launcher
sc config DcomLaunch start=auto
REM ######DHCP Client
sc config Dhcp start=auto
REM ######DNS Client
sc config Dnscache start=auto
REM ######EasyAntiCheat 
sc config EasyAntiCheat start=auto
REM ######Group Policy Client
sc config gpsvc start=auto
REM ######Local Session Manager
sc config LSM start=auto
REM ######Network Store Interface Service
sc config nsi start=auto
REM ######NVIDIA
sc config NVDisplay.ContainerLocalSystem start=auto
REM ######Remote Procedure Call (RPC)
sc config RpcSs start=auto
REM ######RPC Endpoint Mapper
sc config RpcEptMapper start=auto
REM ######Security Accounts Manager
sc config SamSs start=auto
REM ######Server
sc config LanmanServer start=auto
REM ######State Repository Service
sc config StateRepository start=auto
REM ######System Events Broker
sc config SystemEventsBroker start=auto
REM ######Task Scheduler
sc config Schedule start=auto
REM ######Wacom Professional Service
sc config WTabletServicePro start=auto
REM ######Windows Audio
sc config Audiosrv start=auto
REM ######Windows Audio Endpoint Builder
sc config AudioEndpointBuilder start=auto
REM ######WinHTTP Web Proxy Auto-Discovery Service
sc config WinHttpAutoProxySvc start=auto
REM ######Workstation
sc config LanmanWorkstation start=auto
REM ######Windows Defender Firewall
sc config mpssvc start=auto
REM ######Windows Management Instrumentation
sc config Winmgmt start=auto
REM ######Windows Security Service
sc config SecurityHealthService start=auto
REM ######Windows Update
sc config wuauserv start=auto
REM ######User Profile Service
sc config ProfSvc start=auto
REM ######User Manager
sc config UserManager start=auto
sc start Appinfo
sc start AppXSvc
sc start BthAvctpSvc 
sc start BrokerInfrastructure 
sc start BFE
sc start camsvc
sc start ClipSVC
sc start CoreMessagingRegistrar
sc start CryptSvc
sc start CG7Service start=auto
sc start DcomLaunch
sc start Dhcp
sc start Dnscache
sc start EasyAntiCheat
sc start gpsvc
sc start LSM
sc start nsi
sc start NVDisplay.ContainerLocalSystem
sc start RpcSs
sc start RpcEptMapper
sc start SamSs
sc start LanmanServer
sc start StateRepository
sc start SystemEventsBroker
sc start Schedule
sc start WTabletServicePro
sc start Audiosrv
sc start AudioEndpointBuilder
sc start WinHttpAutoProxySvc
sc start LanmanWorkstation
sc start mpssvc
sc start Winmgmt
sc start SecurityHealthService
sc start wuauserv
sc start ProfSvc
sc start UserManager
PAUSE