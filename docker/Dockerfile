FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. System setup
RUN apt-get update && apt-get install -y \
    curl gnupg software-properties-common sudo \
    && add-apt-repository ppa:deadsnakes/ppa -y

# 2. Install Node 24 (Standard for Frappe v15/v16/v17)
RUN curl -fsSL https://deb.nodesource.com/setup_24.x | bash -

# 3. Install Toolchain
RUN apt-get update && apt-get install -y \
    python3.14 python3.14-venv python3.14-dev \
    nodejs mariadb-server mariadb-client redis-server \
    git wget libmariadb-dev pkg-config build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1

# 4. Global Python and JS Tools
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    python3 -m pip install uv frappe-bench --break-system-packages && \
    npm install -g yarn && \
    rm get-pip.py

# 5. User Setup
RUN useradd -ms /bin/bash frappe && echo "frappe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
WORKDIR /home/erp
RUN chown -R frappe:frappe /home/erp

USER frappe

# 6. FLAT STRUCTURE COPY (No symlinks)
# We copy them into a temporary source folder first
COPY --chown=frappe:frappe ERP_Frappe/ /home/erp/src/frappe/
COPY --chown=frappe:frappe ERP_Next/ /home/erp/src/erpnext/
COPY --chown=frappe:frappe TunisianAccounting/ /home/erp/src/tunisian_accounting/

# Copy the scripts
COPY --chown=frappe:frappe docker/setup.sh /home/erp/setup.sh
COPY --chown=frappe:frappe docker/start.sh /home/erp/start.sh
RUN chmod +x /home/erp/setup.sh /home/erp/start.sh

EXPOSE 8000 9000
CMD ["/home/erp/start.sh"]
