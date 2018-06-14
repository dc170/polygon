CREATE TABLE attacker_login (
	uid timeuuid,
	client_ip text,
	client_codename text,
	client_org text,
	service text,
	ip text,
	ip_resolve text,
	country text,
	country_code text,
	PRIMARY KEY(uid,service)
);

CREATE TABLE honeypot_login (
	uid timeuuid,
	user text,
	pass text,
	service text,
	PRIMARY KEY(uid, service)
);
