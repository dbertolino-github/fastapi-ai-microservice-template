FROM python:3.10
LABEL maintainer="Dario Bertolino <bertolino.dario@live.com> <https://github.com/dbertolino-github>"

# UPDATE PYTHON LIBRARIES
RUN apt-get update -y && \
    apt-get install zip
RUN pip install --upgrade pip

# COPY SOURCE CODE AND SET WORKDIR
COPY ./src /src
WORKDIR /src

# INSTALL FASTAPI AND PYTHON REQUIREMENTS
RUN pip install fastapi[all] --no-warn-script-location
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# RUN SERVER
EXPOSE 80
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]