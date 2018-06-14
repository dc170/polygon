CREATE TABLE logfile (
	uid timeuuid,
	filepath text,
	service text,
	sender_ip text,
	sender_user text,
	sender_system text,
	sender_clientcode text,
	PRIMARY KEY(uid)
);
