FROM ubuntu

RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y  install python3
RUN apt-get -y install python3-pip
RUN git clone https://github.com/anajikadam17/aws_test1.git
WORKDIR aws_test1
RUN pip3 install -r  requirements.txt
COPY dummy.txt anaji/dummy.txt
WORKDIR bin
CMD ["python3","app.py"]