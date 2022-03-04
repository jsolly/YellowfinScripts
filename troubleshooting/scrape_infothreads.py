import requests
import time
from datetime import datetime

for i in range(5):
    content = requests.get("http://localhost:8080/info_threads.jsp").text
    current_time = datetime.now().strftime("%m-%d-%y_%H_%M_%S")
    with open(f"{current_time}_info_threads.html", "w") as writer:
        writer.write(content)
        time.sleep(1)


# 5 here represents the length of the grab in seconds, 5 is likely much too small
# while [ $i -le 5 ];do
#         #grab threads with timestamp, enter path info for output file and server info
#         curl -o $path/info_threads-$(date +%H-%M-%S).html https://$localhost:8080/info_threads.jsp
#         #sleep represents your interval between grabs (in seconds), you probably want to leave this at 1
#         sleep 1;
#         i=$((i+1))
# done
