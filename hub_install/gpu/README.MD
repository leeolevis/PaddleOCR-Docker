##  构建镜像
`docker build -t hub_install_gpu:v1 .`

##  运行
`docker run -itd --network=host --gpus kall --name hub_install_gpu hub_install_gpu:v1 `

## 注意
相同配置的硬件，使用该种方式，`CPU`版相较于`hubserving`明显速度变慢，估计是某些参数没设置好，请酌情使用