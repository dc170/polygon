CREATE TABLE file_watch (
	uid timeuuid,
	filepath text,
	md5 text,
	sha1 text,
	purpose text,
	sender_ip text,
	sender_user text,
	sender_system text,
	sender_clientcode text,
	PRIMARY KEY(uid)
);
