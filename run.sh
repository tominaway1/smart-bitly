#!/bin/bash
if [ -z "$VCAP_APP_PORT" ];
then SERVER_PORT=5000;
else SERVER_PORT="$VCAP_APP_PORT";
fi
USER="admin"
PASS="admin"
MAIL=""

python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('${USER}', '${MAIL}', '${PASS}')" | python manage.py shell

echo port is $SERVER_PORT
python manage.py runserver --noreload 0.0.0.0:$SERVER_PORT

