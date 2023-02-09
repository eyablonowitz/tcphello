FROM python:3.10
WORKDIR /app
COPY tcphello tcphello
CMD ["python", "tcphello/tcphello.py"]
