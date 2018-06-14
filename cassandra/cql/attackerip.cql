CREATE TABLE attacler_ip (
	uid timeuuid,
	ip text,
	ip_resolve text,
	country text,
	country_code text,
	PRIMARY KEY(uid,ip)
);
