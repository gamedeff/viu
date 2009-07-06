@echo OFF
cd /D "C:\Program Files\VideoLAN\VLC"
vlc.exe --intf=dummy --dummy-quiet --start-time 5 --stop-time 6 --no-audio --vout=image --image-out-format jpg --image-out-prefix=ss415 --image-out-replace --no-osd "J:\Music\Video\Scooter\Live\[1997.04.05] Scooter @ Dance Palace, Hamburg, Germany\I_m_Raving__Live_At_Dance_Palace_97_.mpg" vlc://quit
cd /D "D:\viu"