FROM python:3.9

#Install pandas
RUN pip install pandas 

#Override this entrypoint
ENTRYPOINT [ "bash" ]