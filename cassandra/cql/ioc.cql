CREATE TABLE attacker_file (
	uid timeuuid,
	filename text,
	md5 text,
	sha1 text,
	PRIMARY KEY(uid)
);

CREATE TABLE attacker_mail (
	uid timeuuid,
	mail text,
	PRIMARY KEY(uid)
);
