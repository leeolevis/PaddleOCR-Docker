##  构建镜像
`docker build -t hub_install_cpu:v1 .`

##  运行
`docker run -itd --network=host  --name hub_install_cpu hub_install_cpu:v1 `

