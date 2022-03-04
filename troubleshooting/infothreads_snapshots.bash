#!/bin/bash
i=0
#5 here represents the length of the grab in seconds, 5 is likely much too small
while [ $i -le 5 ];do
        #grab threads with timestamp, enter path info for output file and server info
        curl -o "$path/info_threads-$(date +%H-%M-%S).html" "http://$localhost:8080/info_threads.jsp"
        #sleep represents your interval between grabs (in seconds), you probably want to leave this at 1
        sleep 1;
        i=$((i+1))
done