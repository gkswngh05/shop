FROM python:3.10
EXPOSE 8000
#ADD shop.tar.gz /srv/shop
COPY shop/ /srv/shop/shop
COPY shopapp/ /srv/shop/shopapp
COPY whl/ /srv/shop/whl
COPY manage.py /srv/shop
COPY requirements.txt /srv/shop
COPY mysql.cnf /srv/shop
WORKDIR /srv/shop
#RUN apt update && apt install -y --no-install-recommends python3-dev default-libmysqlclient-dev build-essential pkg-config && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --no-index -f /srv/shop/whl -r /srv/shop/requirements.txt
RUN python3 /srv/shop/manage.py makemigrations
RUN python3 /srv/shop/manage.py migrate
RUN python3 /srv/shop/manage.py collectstatic --noinput
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]