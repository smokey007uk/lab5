import dns.reversename
nuum = dns.reversename.from_address("127.0.0.1")
print (nuum)
print dns.reversename.to_address(nuum)