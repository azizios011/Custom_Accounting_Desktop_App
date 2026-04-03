#!/bin/bash

# Start services
sudo service mariadb start
sudo service redis-server start
sleep 2

# Check if site exists. Note: setup.sh is in /home/erp/
if [ ! -d "/home/erp/ERP_Bench/sites/mysite.local" ]; then
    echo "First run - running setup..."
    bash /home/erp/setup.sh
fi

# Now that setup has run, this directory exists
cd /home/erp/ERP_Bench
export FRAPPE_BENCH_ROOT=/home/erp/ERP_Bench
exec ./env/bin/bench start
