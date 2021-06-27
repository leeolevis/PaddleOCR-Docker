FROM paddlepaddle/paddle:2.1.0-gpu-cuda10.2-cudnn7
LABEL maintainer="steinven@qq.com"
LABEL version="1.0"
LABEL description="PaddleOCR pdserving GPU version"

#github网速太慢或被墙，现用的cnpmjs加速，也可以更换为码云
ENV REPO_LINK=https://github.com.cnpmjs.org/PaddlePaddle/PaddleOCR.git

#模型数据
ENV	orc_detect_model=https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_det_infer.tar
ENV	orc_recognition_model=https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_rec_infer.tar

#whl包，开发测试阶段，未上传到pypi
ENV paddle_serving_client_test=https://paddle-serving.bj.bcebos.com/test-dev/whl/paddle_serving_client-0.0.0-cp37-none-any.whl

#安装所需的库文件
RUN pip3.7 install --upgrade pip paddle-serving-server-gpu==0.6.1.post101 paddle-serving-app==0.6.1 -i https://mirror.baidu.com/pypi/simple \
	&& git clone $REPO_LINK /PaddleOCR \
	&& pip3.7 install -r /PaddleOCR/requirements.txt -i https://mirror.baidu.com/pypi/simple


#下载模型数据并解压
WORKDIR /PaddleOCR/deploy/pdserving
ADD $orc_detect_model .
ADD $orc_recognition_model .
ADD $paddle_serving_client_test .
RUN for f in *.tar; do tar xf "$f"; done;rm -fr *.tar \
	&& pip3.7 install paddle_serving_client-0.0.0-cp37-none-any.whl \
	&& python3.7 -m paddle_serving_client.convert --dirname ./ch_ppocr_mobile_v2.0_det_infer/ \
                                         --model_filename inference.pdmodel          \
                                         --params_filename inference.pdiparams       \
                                         --serving_server ./ppocr_det_mobile_2.0_serving/ \
                                         --serving_client ./ppocr_det_mobile_2.0_client/ \
    && python3.7 -m paddle_serving_client.convert --dirname ./ch_ppocr_mobile_v2.0_rec_infer/ \
                                         --model_filename inference.pdmodel          \
                                         --params_filename inference.pdiparams       \
                                         --serving_server ./ppocr_rec_mobile_2.0_serving/  \
                                         --serving_client ./ppocr_rec_mobile_2.0_client/ \
	&& rm -fr *.tar


EXPOSE 9998

ENTRYPOINT ["/bin/bash","-c","python3.7 web_service.py"]