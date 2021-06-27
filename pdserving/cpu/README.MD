###  构建镜像

 `docker build -t pdserving_cpu:v1 .`

### 运行

`docker run -itd --network=host --name pdserving_gpu pdserving_cpu:v1`

### 运行&测试
- 修改`client_test.py`中`url`的`host`测试