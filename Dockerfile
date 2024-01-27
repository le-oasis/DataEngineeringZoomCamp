FROM python:3.9

#Install pandas
RUN pip install pandas 

# The working direcotry docker would interact with  
WORKDIR /app

# It would do cd /aoo to get this file
COPY pipeline.py pipeline.py

#Override this entrypoint
ENTRYPOINT [ "bash" ]