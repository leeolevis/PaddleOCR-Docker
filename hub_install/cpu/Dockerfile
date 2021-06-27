FROM paddlepaddle/paddle:2.1.0
LABEL maintainer="steinven@qq.com"
LABEL version="1.0"
LABEL description="hub install CPU version"


#安装所需的库文件
RUN pip3.7 install --upgrade pip paddlehub shapely pyclipper -i https://mirror.baidu.com/pypi/simple

ENTRYPOINT ["/bin/bash","-c","hub serving start -m chinese_ocr_db_crnn_server -p 8868"]