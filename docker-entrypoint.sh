# start.sh
#!/bin/sh

case "${DATABASE_TYPE}" in
  0)
    docker-compose -f docker-compose.yml -f database/docker-compose.mysql.yml up -d
    ;;
  1)
    docker-compose -f docker-compose.yml -f database/docker-compose.mssql.yml up -d
    ;;
  2)
    docker-compose -f docker-compose.yml -f database/docker-compose.postgres.yml up -d
    ;;
  *)
    echo "Unsupported DATABASE_TYPE value. Must be 0 (MySQL), 1 (MSSQL), or 2 (PostgreSQL)."
    exit 1
    ;;
esac