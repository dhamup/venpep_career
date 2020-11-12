# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "venpep"
app_title = "Venpep"
app_publisher = "Venpep"
app_description = "Venture for People"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dhamodaran.p@venpep.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/venpep/css/venpep.css"
# app_include_js = "/assets/venpep/js/venpep.js"

# include js, css files in header of web template
# web_include_css = "/assets/venpep/css/venpep.css"
# web_include_js = "/assets/venpep/js/venpep.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "venpep.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "venpep.install.before_install"
# after_install = "venpep.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "venpep.notifications.get_notification_config"

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
	
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"venpep.tasks.all"
# 	],
# 	"daily": [
# 		"venpep.tasks.daily"
# 	],
# 	"hourly": [
# 		"venpep.tasks.hourly"
# 	],
# 	"weekly": [
# 		"venpep.tasks.weekly"
# 	]
# 	"monthly": [
# 		"venpep.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "venpep.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "venpep.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "venpep.task.get_dashboard_data"
# }

