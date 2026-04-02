# Copyright (c) 2026, Arctic Boy and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AccessRequest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		daily_token: DF.Data | None
		email: DF.Data
		fullname: DF.Data
		role: DF.Data | None
		status: DF.Literal["Pending", "Approved", "Rejected"]
		token_expiry: DF.Datetime | None
	# end: auto-generated types

	pass
