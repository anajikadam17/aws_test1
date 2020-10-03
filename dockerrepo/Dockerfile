FROM ubuntu

RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y  install python3
RUN apt-get -y install python3-pip
RUN mkdir anaji
RUN cd anaji
RUN git clone https://github.com/anajikadam17/aws_test1.git
RUN cd aws_test1
RUN pip3 install -r  aws_test1/requirements.txt
RUN cd bin

CMD ["python3","aws_test1/bin/app.py"]