CREATE TABLE SENSOR_ALERT (
	uid timeuuid,
	src_ip text,
	attacker_country text,
	attacker_countrycode text,
	sensor_ip text,
	sensor_name text,
	client_code text,
	client_org text,
	dst_ip text,
	src_port text,
	dst_port text,
	proto text,
	app_proto text,
	action text,
	signature text,
	category text,
	severity int,
	PRIMARY KEY(uid,dst_ip)
);

CREATE TABLE PCAP_SCAN (
	uid timeuuid,
	file text,
	sensor_ip text,
	sensor_name text,
	client_code text,
	client_org text,
	pkts float,
	bytes float,
	ipv4  float,
	ipv6 float,
	tcp float,
	udp float,
	avg_pkt_size float,
	max_pkt_size float,
	http float,
	smtp float,
	tls float,
	ssh float,
	smb float,
	alerts list<text>,
	PRIMARY KEY(uid,file)
);

CREATE TABLE suricata_rule (
	uid timeuuid,
	sensor_name text,
	sensor_ip text,
	sensor_version text,
	rule_file text,
	rule_cat text,
	rule_lines list<text>,
	PRIMARY KEY(uid,rule_file)
);
