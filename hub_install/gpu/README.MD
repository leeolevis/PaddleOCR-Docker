##  构建镜像
`docker build -t hub_install_gpu:v1 .`

##  运行
`docker run -itd --network=host --gpus kall --name hub_install_gpu hub_install_gpu:v1 `