import frappe
import json
import os

# Maps account class number to ERPNext root_type
CLASS_ROOT_TYPE = {
    "1": "Equity",      # Capitaux propres, dettes à LT
    "2": "Asset",       # Immobilisations
    "3": "Asset",       # Stocks
    "4": "Liability",   # Tiers (clients/fournisseurs/Etat)
    "5": "Asset",       # Comptes financiers
    "6": "Expense",     # Charges
    "7": "Income",      # Produits
}

# Human-readable names for class-level group accounts
CLASS_LABELS = {
    "1": "Comptes de Capitaux",
    "2": "Comptes d'Immobilisations",
    "3": "Comptes de Stocks",
    "4": "Comptes de Tiers",
    "5": "Comptes Financiers",
    "6": "Comptes de Charges",
    "7": "Comptes de Produits",
}


def setup_tunisian_chart(doc, method):
    """Auto-setup the Tunisian PCT when a company is created."""
    if doc.country != "Tunisia":
        return

    chart_path = os.path.join(
        os.path.dirname(__file__),
        "..", "regional", "tunisia", "chart_of_accounts"
    )

    class_files = [
        ("1", "class1_accounts.json"),
        ("2", "class2_accounts.json"),
        ("3", "class3_accounts.json"),
        ("4", "class4_accounts.json"),
        ("5", "class5_accounts.json"),
        ("6", "class6_accounts.json"),
        ("7", "class7_accounts.json"),
    ]

    company_abbr = frappe.get_value("Company", doc.name, "abbr")

    for class_num, class_file in class_files:
        file_path = os.path.join(chart_path, class_file)
        if not os.path.exists(file_path):
            frappe.log_error(f"Missing PCT file: {class_file}", "PCT Setup")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        flat_accounts = data.get("plan_comptable", {}).get("accounts", [])
        if not flat_accounts:
            continue

        root_type = CLASS_ROOT_TYPE.get(class_num, "Asset")
        class_label = CLASS_LABELS.get(class_num, f"Classe {class_num}")

        # Step 1: Create the top-level class group account
        class_account_name = f"{class_num} - {class_label}"
        class_full_name = _ensure_account(
            account_name=class_account_name,
            company=doc.name,
            abbr=company_abbr,
            parent_account=None,
            root_type=root_type,
            is_group=1,
        )

        # Step 2: Build a dict keyed by code for easy parent lookup
        code_to_fullname = {}

        # Sort accounts by code length so parents are created before children
        sorted_accounts = sorted(flat_accounts, key=lambda a: len(str(a.get("code", ""))))

        for acc in sorted_accounts:
            code = str(acc.get("code", "")).strip()
            libelle = acc.get("libelle", "").strip()
            if not code or not libelle:
                continue

            account_name = f"{code} - {libelle}"

            # Find the nearest existing parent by progressively shortening the code
            parent_full_name = class_full_name
            for length in range(len(code) - 1, 0, -1):
                prefix = code[:length]
                if prefix in code_to_fullname:
                    parent_full_name = code_to_fullname[prefix]
                    break

            # Determine if this account has children (i.e., any other code starts with this code)
            has_children = any(
                str(other.get("code", "")).startswith(code) and str(other.get("code", "")) != code
                for other in flat_accounts
            )

            full_name = _ensure_account(
                account_name=account_name,
                company=doc.name,
                abbr=company_abbr,
                parent_account=parent_full_name,
                root_type=root_type,
                is_group=1 if has_children else 0,
            )

            if full_name:
                code_to_fullname[code] = full_name

    frappe.db.commit()
    frappe.msgprint(f"✅ Plan Comptable Tunisien (PCT) applied to {doc.name}", alert=True)


def _ensure_account(account_name, company, abbr, parent_account, root_type, is_group):
    """Create an ERPNext Account if it doesn't already exist. Returns account full name."""
    full_name = f"{account_name} - {abbr}"

    if frappe.db.exists("Account", full_name):
        return full_name

    try:
        doc = frappe.get_doc({
            "doctype": "Account",
            "account_name": account_name,
            "company": company,
            "parent_account": parent_account,
            "root_type": root_type,
            "is_group": is_group,
            "account_currency": "TND",
        })
        doc.insert(ignore_permissions=True)
        return doc.name
    except Exception as e:
        frappe.log_error(
            f"Could not create account '{account_name}': {e}",
            "PCT Account Creation Error"
        )
        return None
