FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV=development
# RUN cd server
# CMD python ./index.py
CMD ["flask", "run"]
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi"]