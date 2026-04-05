#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::process::Command;
use std::thread;
use std::time::Duration;

fn start_erpnext() {
    Command::new("powershell")
        .args([
            "-ExecutionPolicy", "Bypass",
            "-WindowStyle", "Hidden",
            "-File", "start_erp.ps1"
        ])
        .current_dir(std::env::current_exe()
            .unwrap()
            .parent()
            .unwrap())
        .spawn()
        .expect("Failed to start ERPNext");

    thread::sleep(Duration::from_secs(8));
}

fn stop_erpnext() {
    Command::new("wsl")
        .args(["-d", "Ubuntu", "-e", "bash", "-c",
            "kill $(cat /tmp/erp_bench.pid 2>/dev/null) 2>/dev/null || true"
        ])
        .spawn()
        .ok();
}

fn main() {
    start_erpnext();

    tauri::Builder::default()
        .on_window_event(|_window, event| {
            if let tauri::WindowEvent::CloseRequested { .. } = event {
                stop_erpnext();
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
