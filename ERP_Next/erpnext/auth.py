# ERP_Next/erpnext/api/auth.py

import frappe

@frappe.whitelist(allow_guest=True)
def login_with_token(token):
    # Find user by token
    user = frappe.db.get_value(
        "User", 
        {"api_key": token}, 
        "name"
    )
    
    if not user:
        frappe.throw("Invalid token", frappe.AuthenticationError)
    
    # Log them in
    frappe.local.login_manager.login_as(user)
    frappe.local.response["message"] = "ok"
    