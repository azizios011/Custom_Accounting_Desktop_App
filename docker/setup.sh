#!/bin/bash
set -e

# 1. Startup Services
echo "Starting MariaDB & Redis..."
sudo service mariadb start
sudo service redis-server start
sudo mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'root'; FLUSH PRIVILEGES;" 2>/dev/null || true

# 2. Create Real Bench Structure (Physical, not Symlinked)
echo "Creating physical bench structure..."
mkdir -p ERP_Bench/apps ERP_Bench/sites ERP_Bench/config/pids ERP_Bench/logs

# MOVE files from src to apps (Making them physical folders)
cp -r /home/erp/src/frappe ERP_Bench/apps/frappe
cp -r /home/erp/src/erpnext ERP_Bench/apps/erpnext
cp -r /home/erp/src/tunisian_accounting ERP_Bench/apps/tunisian_accounting

cd ERP_Bench

# 3. Python Environment
echo "Installing Python packages..."
uv venv env --seed --python python3.14
./env/bin/pip install frappe-bench
./env/bin/pip install -e apps/frappe
./env/bin/pip install -e apps/erpnext
./env/bin/pip install -e apps/tunisian_accounting

# 4. Node dependencies with Plyr Fix
echo "Installing Node dependencies..."
cd apps/frappe
yarn add plyr@3.7.8 --exact
yarn install
cd ../erpnext
yarn add onscan.js --exact
yarn install
cd ../..

# 5. Configs
echo -e "frappe\nerpnext\ntunisian_accounting" > sites/apps.txt
echo '{
  "background_workers": 1,
  "db_host": "localhost",
  "redis_cache": "redis://127.0.0.1:6379",
  "redis_queue": "redis://127.0.0.1:6379",
  "redis_socketio": "redis://127.0.0.1:6379",
  "webserver_port": 8000
}' > sites/common_site_config.json

echo 'web: ./env/bin/bench serve --port 8000
socketio: node /home/erp/ERP_Bench/apps/frappe/socketio.js
watch: ./env/bin/bench watch
schedule: ./env/bin/bench schedule
worker_short: ./env/bin/bench worker --queue short
worker_long: ./env/bin/bench worker --queue long
worker_default: ./env/bin/bench worker --queue default' > Procfile

# 6. Site Creation
echo "Creating site..."
export FRAPPE_BENCH_ROOT=/home/erp/ERP_Bench
./env/bin/bench new-site mysite.local --db-root-password root --admin-password admin123 --mariadb-user-host-login-scope='%'
./env/bin/bench --site mysite.local install-app erpnext
./env/bin/bench --site mysite.local install-app tunisian_accounting
./env/bin/bench --site mysite.local set-config developer_mode 1

# 7. Asset Build (This will now succeed because paths are physical)
echo "Building assets..."
./env/bin/bench build --force

echo "Setup complete!"
