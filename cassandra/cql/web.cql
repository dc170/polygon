CREATE TABLE web_content(
	uid timeuuid,
	sensor_name text,
	sensor_purpose text,
	content text,
	count int,
	ftim date,
	itim date,
	PRIMARY KEY(uid,sensor_name)
	
);

CREATE TABLE web_event(
	uid timeuuid,
	sensor_name text,
	sensor_purpose text,
	request_url text,
	request_raw text,
	pattern text,
	filename text,
	src_port text,
	dst_port text,
	attacker_ip text,
	PRIMARY KEY(uid,sensor_name)
);
