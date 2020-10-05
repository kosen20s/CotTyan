FROM python:3.8.5
RUN mkdir src 
COPY . /src
WORKDIR /src
RUN python3 -m pip install asyncio discord.py

CMD python3 main.py
