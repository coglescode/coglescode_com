pip install -r /home/coglescode/coglescode_com/requirements.txt
python manage.py collectstatic --noinput
sudo systemctl restart nginx.service
sudo systemctl restart emperor.uwsgi.service
