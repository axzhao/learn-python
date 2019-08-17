## 解压测试数据

wc命令
-- word count
> wc -l <文件名> 输出行数统计  
> wc -c <文件名> 输出字节数统计  
> wc -m <文件名> 输出字符数统计  
> wc -L <文件名> 输出文件中最长一行的长度  
> wc -w <文件名> 输出单词数统计  

```
$ unzip flags.zip
$ ls flags | wc -w
$ find flags | grep .gif | wc -l
$ find flags | grep .json | wc -l
$ ls flags/ad
```

## 配置Nginx

`--conf-path=` 配置文件
```
$ nginx -V
$ vi /usr/local/etc/nginx/nginx.conf

server {
    listen 8001;
    location /flags/ {
            root /Users/Dev/example-code-master/17-futures/countries/;
    }
}

$ nginx
$ nginx -s reload
```
`http://localhost:8001/flags/ad/ad.gif`

## Toxiproxy 模拟网络条件的框架

```
$ brew tap shopify/shopify
$ brew install toxiproxy 
```

In One terminal
> $ toxiproxy-server

In another terminal  
1. Created new proxy nginx_flags_delay     
2. Added downstream latency toxic 'latency_downstream' on proxy 'nginx_flags_delay'  
> $ toxiproxy-cli create nginx_flags_delay -l localhost:8002 -u localhost:8001   
> $ toxiproxy-cli toxic add nginx_flags_delay -t latency -a latency=500 

`http://localhost:8002/flags/ad/ad.gif`

## Python3

```
python3 flags.py
python3 flags_threadpool.py
python3 flags_asyncio.py
```