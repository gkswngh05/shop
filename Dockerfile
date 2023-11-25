FROM python:3.10
EXPOSE 8000
ADD shop.tar /srv
WORKDIR /srv/shop
RUN pip install --no-cache-dir --no-index -f /srv/shop/whl -r /srv/shop/requirements.txt
RUN python3 /srv/shop/manage.py makemigrations
RUN python3 /srv/shop/manage.py migrate
RUN python3 /srv/shop/manage.py collectstatic --noinput
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]