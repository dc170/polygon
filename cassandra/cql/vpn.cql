CREATE TABLE vpn_client(
	uid timeuuid,
	client_name text,
	client_org text,
	client_lastip text,
	PRIMARY KEY(uid,client_name)
);

CREATE TABLE vpn(
	uid timeuuid,
	config_file text,
	net_addr text,
	clients list<text>,
	PRIMARY KEY(uid,net_addr)

);
