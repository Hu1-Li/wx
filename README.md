# wx
WeChat application

This is a WeChat application for learning Using WeRobot.


# Nginx Proxy

```
location / {
    client_body_buffer_size 128k;
    proxy_send_timeout   90;
    proxy_read_timeout   90;
    proxy_buffer_size    4k;
    proxy_buffers     16 32k;
    proxy_busy_buffers_size 64k;
    proxy_temp_file_write_size 64k;
    proxy_connect_timeout 30s;
    proxy_redirect off;
    proxy_pass   http://localhost:8888;
    proxy_set_header   Host   $host;
    proxy_set_header   X-Real-IP  $remote_addr;
    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
}

```

# Supervisor Config

```
[program:wx]
command=/home/LH/wx_env/bin/python wx.py
directory=/home/LH/wx_dev/
autostart=true
autorestart=true
stdout_logfile=/yundisk/wx_dev/log/wx.log
redirect_stderr=true
stopsignal=QUIT
```