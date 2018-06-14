CREATE TABLE clamav_scan (
	uid timeuuid,
	md5 text,
	sha1 text,
	result text,
	PRIMARY KEY(uid)
);
