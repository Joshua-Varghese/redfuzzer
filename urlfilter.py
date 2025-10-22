#Function to filter out 'www' if it exist.
def filter_domain(bd):
	filter_bd = bd.split(".")
	if filter_bd[0] == "www":
		del filter_bd[0]
	return ".".join(filter_bd)