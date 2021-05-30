#!/bin/sh

echo "Waiting for postgres on host $DATABASE_HOST..."

while ! nc -z $DATABASE_HOST 5432; do
    sleep 0.1
done

echo "PostgreSQL started"


exec "$@"