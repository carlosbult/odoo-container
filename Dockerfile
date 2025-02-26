FROM odoo:17.0

# Copy extra-addons
COPY ./extra-addons /mnt/extra-addons

# Copy odoo.conf
COPY ./odoo.conf /etc/odoo/odoo.conf

