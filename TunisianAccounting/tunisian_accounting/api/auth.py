import frappe
from frappe.utils import now_datetime, get_datetime
from datetime import datetime

# Modules that only the Admin should see
ADMIN_ONLY_MODULES = [
    "Core", "Custom", "Desk", "Email", "Integrations", 
    "Printing", "Setup", "Workflow", "Data Import Tool", "Database"
]

@frappe.whitelist(allow_guest=True)
def login_with_token(token: str):
    user = frappe.db.get_value("User", {"api_key": token}, ["name", "token_expiry"], as_dict=True)
    if not user:
        frappe.throw("Jeton invalide.")
    
    if user.token_expiry and now_datetime() > get_datetime(user.token_expiry):
        frappe.throw("Votre jeton a expiré.")

    frappe.local.login_manager.login_as(user.name)
    
    # Hide Admin modules from employee
    user_doc = frappe.get_doc("User", user.name)
    user_doc.block_modules = []
    for module in ADMIN_ONLY_MODULES:
        user_doc.append("block_modules", {"module": module})
    user_doc.save(ignore_permissions=True)
    frappe.db.commit()
    return "ok"

@frappe.whitelist(allow_guest=True)
def request_access(fullname: str, email: str, role: str = ""):
    if frappe.db.exists("Access Request", {"email": email, "status": "Pending"}):
        frappe.throw("Une demande est déjà en cours pour cet email.")

    doc = frappe.get_doc({
        "doctype": "Access Request",
        "fullname": fullname,
        "email": email,
        "role": role,
        "status": "Pending"
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return "ok"

@frappe.whitelist(allow_guest=True)
def request_daily_token(email: str):
    if not frappe.db.exists("User", email):
        frappe.throw("Aucun compte trouvé.")

    token = frappe.generate_hash(length=20)
    today_midnight = get_datetime(now_datetime().strftime('%Y-%m-%d 23:59:59'))

    frappe.db.set_value("User", email, {"api_key": token, "token_expiry": today_midnight})
    frappe.db.commit()
    return "sent"

# --- ADMIN DASHBOARD FUNCTIONS (The missing ones) ---

@frappe.whitelist()
def get_access_requests():
    """Returns pending requests for the admin dashboard"""
    return frappe.get_all("Access Request", 
        filters={"status": "Pending"}, 
        fields=["name", "fullname", "email", "role"]
    )

@frappe.whitelist()
def approve_request(request_name: str):
    req = frappe.get_doc("Access Request", request_name)
    if not frappe.db.exists("User", req.email):
        user = frappe.get_doc({
            "doctype": "User",
            "email": req.email,
            "first_name": req.fullname,
            "user_type": "System User",
            "send_welcome_email": 0,
            "roles": [
                {"role": "Employee"},
                {"role": "Desk User"}
            ]
        })
        user.insert(ignore_permissions=True)
    
    token = frappe.generate_hash(length=20)
    midnight = get_datetime(now_datetime().strftime('%Y-%m-%d 23:59:59'))
    
    frappe.db.set_value("User", req.email, {"api_key": token, "token_expiry": midnight})
    frappe.db.set_value("Access Request", request_name, "status", "Approved")
    frappe.db.commit()
    return token

@frappe.whitelist()
def reject_request(request_name: str):
    frappe.db.set_value("Access Request", request_name, "status", "Rejected")
    frappe.db.commit()
    return "ok"

@frappe.whitelist()
def get_employees():
    return frappe.get_all("User", 
        filters={"enabled": 1, "user_type": "System User", "name": ["!=", "Administrator"]}, 
        fields=["name", "full_name", "email", "api_key"]
    )

@frappe.whitelist()
def generate_employee_token(user_email: str):
    token = frappe.generate_hash(length=20)
    midnight = get_datetime(now_datetime().strftime('%Y-%m-%d 23:59:59'))
    frappe.db.set_value("User", user_email, {"api_key": token, "token_expiry": midnight})
    frappe.db.commit()
    return token
    