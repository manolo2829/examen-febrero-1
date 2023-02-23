FROM python:3
RUN git clone https://github.com/manolo2829/um-computacion-final
WORKDIR /um-computacion-final
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]
