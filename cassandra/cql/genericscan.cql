CREATE TABLE generic_scan (
	uid timeuuid,
	md5 text,
	sha1 text,
	general_result text,
	clamscan text,
	yarascan text,
	neural text,
	prob text,
	heuristic text,
	knn text,
	sender_ip text,
	sender_user text,
	sender_system text,
	PRIMARY KEY(uid)
);
