# sleep 5
while ! nc -w 1 -z -v db_master 5432;
do 
sleep 1;
echo "wait for connecting to database ... "
done;

python manage.py runserver 0.0.0.0:8000
