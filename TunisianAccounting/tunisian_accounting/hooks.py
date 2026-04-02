app_name = "tunisian_accounting"
app_title = "Tunisian Accounting"
app_publisher = "Arctic Boy"
app_description = "Tunisian ERP Accounting System"
app_email = "azizhidri001@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tunisian_accounting",
# 		"logo": "/assets/tunisian_accounting/logo.png",
# 		"title": "Tunisian Accounting",
# 		"route": "/tunisian_accounting",
# 		"has_permission": "tunisian_accounting.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tunisian_accounting/css/tunisian_accounting.css"
# app_include_js = "/assets/tunisian_accounting/js/tunisian_accounting.js"

# include js, css files in header of web template
# web_include_css = "/assets/tunisian_accounting/css/tunisian_accounting.css"
# web_include_js = "/assets/tunisian_accounting/js/tunisian_accounting.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tunisian_accounting/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tunisian_accounting/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tunisian_accounting.utils.jinja_methods",
# 	"filters": "tunisian_accounting.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tunisian_accounting.install.before_install"
# after_install = "tunisian_accounting.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tunisian_accounting.uninstall.before_uninstall"
# after_uninstall = "tunisian_accounting.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tunisian_accounting.utils.before_app_install"
# after_app_install = "tunisian_accounting.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tunisian_accounting.utils.before_app_uninstall"
# after_app_uninstall = "tunisian_accounting.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tunisian_accounting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tunisian_accounting.tasks.all"
# 	],
# 	"daily": [
# 		"tunisian_accounting.tasks.daily"
# 	],
# 	"hourly": [
# 		"tunisian_accounting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tunisian_accounting.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tunisian_accounting.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tunisian_accounting.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tunisian_accounting.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tunisian_accounting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tunisian_accounting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tunisian_accounting.utils.before_request"]
# after_request = ["tunisian_accounting.utils.after_request"]

# Job Events
# ----------
# before_job = ["tunisian_accounting.utils.before_job"]
# after_job = ["tunisian_accounting.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tunisian_accounting.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

# Ensure the variable name 'chart_of_accounts' is present and uses { }
chart_of_accounts = {
    "Tunisia": {
        "Plan Comptable Tunisien (PCT)": "regional/tunisia/chart_of_accounts/pct_tunisie.json"
    }
}

# Override chart of accounts on company creation
doc_events = {
    "Company": {
        "after_insert": "tunisian_accounting.setup.company.setup_tunisian_chart"
    }
}
