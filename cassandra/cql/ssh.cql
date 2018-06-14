
CREATE TABLE shell_cmd(
	uid timeuuid,
	sensor_name text,
	sensor_purpose text,
	timestamp text,
	msg text,
	system text,
	input text,
	state text,
	PRIMARY KEY(uid)
);

CREATE TABLE shell_file(
	uid timeuuid,
	sensor_name text,
	sensor_purpose text,
	timestamp text,
	msg text,
	system text,
	url text,
	attacker_ip text,
	file_md5 text,
	file_sha1 text,
	file_path text,
	PRIMARY KEY(uid,file_md5)
);
