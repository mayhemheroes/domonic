FROM python:3.11-slim

RUN apt-get update && apt-get install -y clang && rm -rf /var/lib/apt/lists/*
RUN pip3 install atheris

COPY . /domonic
WORKDIR /domonic
RUN python3 -m pip install -r requirements.txt && python3 -m pip install . && chmod +x fuzz/domonic_fuzz.py

ENTRYPOINT [ ]
CMD ["/domonic/fuzz/domonic_fuzz.py"]
