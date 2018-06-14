CREATE TABLE attacker_url (
	uid timeuuid,
	url text,
	ip text,
	ip_resolve text,
	country text,
	country_code text,
	PRIMARY KEY(uid,ip)
);
