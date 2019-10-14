ps aux | grep -ie "$1" | awk '{print $2}' | xargs kill -9
