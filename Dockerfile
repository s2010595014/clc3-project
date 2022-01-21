FROM python:3.8
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO
COPY . ./
CMD ["python", "-u", "hello_world.py"]
