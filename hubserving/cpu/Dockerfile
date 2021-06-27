FROM paddlepaddle/paddle:2.1.0
LABEL maintainer="steinven@qq.com"
LABEL version="1.0"
LABEL description="PaddleOCR hubserving CPU version"

#github网速太慢或被墙，现用的cnpmjs加速，也可以更换为码云
ENV REPO_LINK=https://github.com.cnpmjs.org/PaddlePaddle/PaddleOCR.git

#模型数据，现用的ch_ppocr_mobile_v2.0_xx，为中英文超轻量OCR模型，因为源码参数中配置的就为该模型，
#所以不用修改源码。如果切换为服务端模型，记得修改deploy/hubserving/ocr_system/params.py下对应的模型位置
ENV	orc_detect_model=https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_det_infer.tar
ENV	orc_direction_model=https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar
ENV	orc_recognition_model=https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_rec_infer.tar

#安装所需的库文件
RUN pip3.7 install --upgrade pip paddlehub -i https://mirror.baidu.com/pypi/simple \
	&& git clone $REPO_LINK /PaddleOCR \
	&& pip3.7 install -r /PaddleOCR/requirements.txt -i https://mirror.baidu.com/pypi/simple \
	&& mkdir -p /PaddleOCR/inference

#下载模型数据并解压
WORKDIR /PaddleOCR/inference/
ADD $orc_detect_model .
ADD $orc_direction_model .
ADD $orc_recognition_model .
RUN for f in *.tar; do tar xf "$f"; done;rm -fr *.tar
WORKDIR /PaddleOCR
EXPOSE 8868

ENTRYPOINT ["/bin/bash","-c","hub install deploy/hubserving/ocr_system/ && hub serving start -m ocr_system -p 8868"]