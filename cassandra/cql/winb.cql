CREATE TABLE win_binaries (
	uid timeuuid,
	filename text,
	debugsize double,
	debugrva double,
	imageversion int,
	osversion int,
	exportrva double,
	exportsize double,
	iatrva double,
	ressize double,
	linkerversion double,
	numberofsections int,
	stackrevsize int,
	dll double,
	upx int,
	numdlls int,
	numimports int,
	entropy double,
	md5 text,
	sha1 text,
	dlls list<text>,
	functions list <text>,
	PRIMARY KEY (uid)
);

	
