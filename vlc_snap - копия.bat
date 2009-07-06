@echo OFF
cd /D "C:\Program Files\VideoLAN\VLC"
vlc --snapshot-path="D:\viu" --snapshot-prefix=ss --snapshot-sequential -vvv -I dummy -V image --start-time 5 --stop-time 6 --image-out-format jpg --image-out-ratio 25 --image-out-prefix "ss415" "J:\Music\Video\Scooter\Live\[1997.04.05] Scooter @ Dance Palace, Hamburg, Germany\I_m_Raving__Live_At_Dance_Palace_97_.mpg" vlc:quit
cd /D "D:\viu"