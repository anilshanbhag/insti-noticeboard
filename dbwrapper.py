# DB Wrapper

from datetime import datetime

class DBWrapper:
	def __init__(self):
		"""
		Initialze the DB connection with Postgres DB
		"""
		pass

	def add(self, event):
		"""
		INSERT new event
		"""
		pass

	def update(self, event):
		"""
		UPDATE event
		"""
		pass

	def delete(self, event):
		"""
		DELETE event
		"""
		pass

	def select(self, date_from, date_to):
		"""
		SELECT Events between the two datetime objects
		"""
		pass