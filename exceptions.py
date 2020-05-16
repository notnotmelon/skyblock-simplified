class SkyblockError(Exception):
	"""A general exception from the skyblock library"""
	def __str__(self):
		return self.reason

class DataError(SkyblockError):
	"""You entered wrong data"""

class ExternalAPIError(SkyblockError):
	"""There was an issue connecting to the Hypixel API"""
	def __init__(self, reason=''):
		self.reason = reason
	
class HypixelError(ExternalAPIError):
	"""The Hypixel API had some error"""
	def __init__(self, reason=''): 
		self.reason = reason
	 
class BadNameError(SkyblockError):
	"""This uuid, or username, or guild name is invalid"""
	def __init__(self, uname_or_uuid, reason=''): 
		self.uname_or_uuid = uname_or_uuid
		self.reason = reason
		
	def __str__(self):
		return f'{self.reason}; {self.uname_or_uuid}'

class NeverPlayedSkyblockError(BadNameError):
	"""This user has never played skyblock before!"""
	def __init__(self, uname_or_uuid, reason=''):
		self.uname_or_uuid = uname_or_uuid
		self.reason = reason
		
class BadGuildError(BadNameError):
	"""This is an invalid guild"""
	def __init__(self, guild, reason=''):
		self.guild = guild
		self.reason = reason
		
	def __str__(self):
		return f'{self.reason}; {self.guild}'
		
class APIKeyError(SkyblockError):
	"""You used an invalid API key"""
	def __init__(self, key, reason=''): 
		self.key = key
		self.reason = reason
		
	def __str__(self):
		return f'{self.reason}; {self.key}'
	
class LoadError(SkyblockError):
	"""You tried to load a module that was already loaded"""
	def __init__(self, module, reason=''):
		self.module
		self.reason = reason
		
	def __str__(self):
		return f'{self.reason}; module: {self.module}'