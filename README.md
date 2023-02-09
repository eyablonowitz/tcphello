# tcphello
Python TCP socket listener example.

### Build
```shell
docker build -t tcphello .
```

### Run
```shell
docker run -d -p 12345:12345/tcp tcphello
```

### Client example

Using netcat:
```shell
% nc -v localhost 12345                                         
Connection to localhost port 12345 [tcp/italk] succeeded!
Hello, 172.17.0.1!
```
