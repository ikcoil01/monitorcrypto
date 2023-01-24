FROM redhat/ubi8
COPY cryptoscraper.py cryptoscraper.py
COPY run.sh run.sh
RUN dnf install python3 -y
RUN python3 -m ensurepip --upgrade
RUN pip3 install requests python-daemon bs4 prometheus_client
ENTRYPOINT [ "bash","run.sh"]