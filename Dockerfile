FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV=development
ENV PORT=8000
# RUN cd server
# CMD python ./index.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi"]