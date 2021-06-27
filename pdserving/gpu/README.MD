###  构建镜像

 `docker build -t pdserving_gpu:v1 .`

### 运行

`docker run -itd --network=host --gpus all  --name pdserving_gpu pdserving_gpu:v1`

### 修改配置
查看运行日志发现没有错误后，低端显卡的话，别先进行测试。我们需要修改一下配置文件。
默认的配置对显卡要求较高，需要修改一下`QPS`,默认的两个并发参数分别为8、4，现在拿我的`GeForce 750` 2GB显存，我需要把它改成2、1
- 进入容器：`docker exec -it pdserving_gpu  /bin/bash`
- 打开配置文件`vim /PaddleOCR/deploy/pdserving/config.yml`,找到下图对应的两个参数，进行修改
![](https://img2020.cnblogs.com/blog/1435533/202106/1435533-20210626220657665-330979003.png)
- 重启`docker`容器:`docker restart pdserving_gpu  `
- 修改`client_test.py`中`url`的`host`测试