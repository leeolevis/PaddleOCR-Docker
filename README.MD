# 一、各种部署方式特点及注意事项

`hubserving`=`PaddleHub Serving`

`pdserving`=`PaddleHub Serving`

`hub install `=指通过`paddlehub`库直接安装部署服务

##  部署特点
`pdserving`更适合企业级部署，性能更高，摘取官方的介绍:
- 支持客户端和服务端之间高并发和高效通信
- 支持 工业级的服务能力 例如模型管理，在线加载，在线A/B测试等
- 支持 多种编程语言 开发客户端，例如C++, Python和Java

`hubserving`可以理解为源码方式安装某个服务，配置型强

`hub install `其实和`hubserving`方式一样，都使用`paddlehub`库进行部署的，其首次进行识别的的时候，会自动下载模型文件，真正一条命令就可以运行起来一个服务，部署起来超简单。
不足之处在于我现在还没找到对于相关模块的配置。只有`paddlehub`自己的一些启动参数可配置。如果你的显卡比较好，又想快点部署，优先考虑采用本方式。低端显卡要是使用此种方式，会导致显存迅速拉满，然后不可用，我现在也没找到解决办法。
相同配置的硬件，使用该种方式，`CPU`版相较于`hubserving`明显速度变慢很多，估计是某些参数没设置好，请酌情使用，`GPU`版本未测试
除了本文的`OCR`，还有很多有趣的服务通过此种方式可快速搭建，[详见](https://www.paddlepaddle.org.cn/hublist)


##  注意事项
- 相同价格的硬件，识别速度上还是`GPU`速度更快，优先选择`GPU` 
- 部署方式上优先选择`pdserving`方式
- 如果你没有显卡，只能用`CPU`的话，一定要确认你的`CPU`要支持`AVX`指令集，验证方法:`lscpu | grep avx`
没有`AVX`指令的话，部署起来比较困难，而且识别速度应该会很慢。
如果你真想部署的话，要安装对应的`noavx`版本的`paddlepaddle`，`whl`包[在这](https://www.paddlepaddle.org.cn/whl/openblas/stable/noavx.html)并且只能使用`Python3.8`,这个我暂时没时间验证是否能安装成功。等后面有时间了再研究一下...
- 当你使用`wget`获取资源的时候，如果发现速度很慢，只有几十`KB`,你可以尝试一下`Ctrl+C`取消后再重新获取，这个问题是什么导致的我也不清楚
- 如果你使用的是阿里云或者其他（非百度）的云平台获取资源的时候，速度奇慢，我想是被百度限制了，这时候你可能需要在本地下载好再传到你机器上，当然你也可以使用代理的方式
- 当你真想部署成一个可靠的服务时，`GPU`显存我感觉最少要`16 GB`
- 当你在阿里云上使用`pdserving`方式部署，有可能遇到显存被瞬间填满，机器卡死的情况。我本以为是`PaddleServing`造成的现存泄露，我也一直在纠结这个问题。但在百度的`aistudio`上，同样`16G`显存，`aistudio`是正常的