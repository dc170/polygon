CREATE TABLE yara_scan (
	uid timeuuid,
	md5 text,
	sha1 text,
	result text,
	rules_tested list<text>,
	rules_detected list<text>,
	PRIMARY KEY(uid)
);
