Write-Host "Starting Tunisian Accounting ERP..."

# Start Redis in WSL
wsl -d Ubuntu -e bash -c "sudo systemctl start redis 2>/dev/null || true"

# Start ERPNext in WSL background
wsl -d Ubuntu -e bash -c "export FRAPPE_BENCH_ROOT=/home/arctic_crystal/Repositories/Custom_Accounting_Desktop_App/ERP_Bench && cd /home/arctic_crystal/Repositories/Custom_Accounting_Desktop_App/ERP_Bench && nohup bench start > /tmp/erp_bench.log 2>&1 & echo $! > /tmp/erp_bench.pid"

# Wait for ERPNext
$maxWait = 60
$waited = 0
do {
    Start-Sleep -Seconds 2
    $waited += 2
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8000" -TimeoutSec 2 -ErrorAction Stop
        Write-Host "ERPNext is ready!"
        exit 0
    } catch {
        Write-Host "Still waiting... ($waited/$maxWait seconds)"
    }
} while ($waited -lt $maxWait)

Write-Host "ERPNext started"
