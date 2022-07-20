FROM python:3

WORKDIR /webInterface

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY . ./

CMD [ "streamlit", "run", "./app/interface.py" ]