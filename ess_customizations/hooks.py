app_name = "ess_customizations"
app_title = "Ess Customizations"
app_publisher = "Safdar Ali"
app_description = "this is ess customizations"
app_email = "safdar211@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ess_customizations",
# 		"logo": "/assets/ess_customizations/logo.png",
# 		"title": "Ess Customizations",
# 		"route": "/ess_customizations",
# 		"has_permission": "ess_customizations.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ess_customizations/css/ess_customizations.css"
# app_include_js = "/assets/ess_customizations/js/ess_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/ess_customizations/css/ess_customizations.css"
# web_include_js = "/assets/ess_customizations/js/ess_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ess_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Visit" : "public/js/visit.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ess_customizations/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ess_customizations.utils.jinja_methods",
# 	"filters": "ess_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ess_customizations.install.before_install"
# after_install = "ess_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ess_customizations.uninstall.before_uninstall"
# after_uninstall = "ess_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ess_customizations.utils.before_app_install"
# after_app_install = "ess_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ess_customizations.utils.before_app_uninstall"
# after_app_uninstall = "ess_customizations.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ess_customizations.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Visit": {
		"after_insert": "ess_customizations.events.set_location_address.set_location_address",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ess_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"ess_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"ess_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ess_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ess_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ess_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ess_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ess_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ess_customizations.utils.before_request"]
# after_request = ["ess_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["ess_customizations.utils.before_job"]
# after_job = ["ess_customizations.utils.after_job"]

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
# 	"ess_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

