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
