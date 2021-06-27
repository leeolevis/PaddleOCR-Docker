##  构建`docker`镜像
`docker build -t hubserving_gpu:v1 .`

##  运行
`docker run -itd --network=host --gpus all  --name hubserving_gpu hubserving_gpu:v1`

##  检查运行状态，查看是否有错误,查看端口号
`docker logs -f hubserving_gpu `
