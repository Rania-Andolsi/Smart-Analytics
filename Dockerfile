# Use the official Odoo image as a parent image
FROM odoo:14.0

# Switch to root user to install dependencies
USER root

# Install any additional dependencies
RUN apt-get update && apt-get install -y python3-pip

# Switch back to odoo user
USER odoo

# Copy custom addons
COPY ./custom_addons /mnt/extra-addons

# Expose Odoo port
EXPOSE 8069

# Run Odoo
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
