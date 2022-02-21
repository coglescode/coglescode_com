python manage.py collectstatic --noinput
sudo systemctl restart nginx.service
sudo systemctl restart emperor.uwsgi.service
