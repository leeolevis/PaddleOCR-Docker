###  构建镜像
`docker build -t hubserving_cpu:v1 .`

###  运行
`docker run -itd --network=host  --name hubserving_cpu hubserving_cpu:v1`