#!/bin/bash
set -e

# Verificar permisos de ejecución
if [[ ! -x "$0" ]]; then
    echo "Error: No tengo permisos de ejecución!"
    exit 1
fi

# Generar odoo.conf dinámicamente
cat <<EOF > /etc/odoo/odoo.conf
[options]
addons_path = /mnt/extra-addons/enterprise,/mnt/extra-addons/custom
data_dir = /var/lib/odoo
admin_passwd = ${ADMIN_PASSWD:-admin}
db_host = ${DB_HOST}
db_port = ${DB_PORT:-5432}
db_user = ${DB_USER}
db_password = ${DB_PASSWORD}
EOF

exec odoo  "$@"