@load Bro/ElasticSearch/logs-to-elasticsearch.bro

global mime_to_ext: table[string] of string = {
	["application/x-dosexec"] = "exe",
	["application/vnd.android.package-archive"] = "apk",
	["application/vnd.apple.installer+xml"] = "mpkg",
	["application/x-sh"] = "sh",
	["application/x-csh"] = "csh",
	["application/java-archive"] = "jar",
	["application/x-msdownload"] = "exe",
	["application/octet-stream"] = "bin",
};

event bro_init()
    {
    local filter: Log::Filter =
        [
        $name="sqlite",
        $path="./conn",
        $config=table(["tablename"] = "conn"),
        $writer=Log::WRITER_SQLITE
        ];
    
     Log::add_filter(Conn::LOG, filter);

    local pefilter: Log::Filter =
        [
        $name="sqlite",
        $path="./pe",
        $config=table(["tablename"] = "pe"),
        $writer=Log::WRITER_SQLITE
        ];
    
     Log::add_filter(PE::LOG, pefilter);

     local filefilter: Log::Filter =
        [
        $name="sqlite",
        $path="./file",
        $config=table(["tablename"] = "file"),
        $writer=Log::WRITER_SQLITE
        ];
    
     Log::add_filter(Files::LOG, filefilter);

    }


event file_sniff(f: fa_file, meta: fa_metadata)
	{
	if ( ! meta?$mime_type )
		return;

	if ( meta$mime_type !in mime_to_ext )
		return;

	local fname = fmt("%s.%s", f$id, mime_to_ext[meta$mime_type]);
	print fmt("Extracting file %s", fname);
	Files::add_analyzer(f, Files::ANALYZER_EXTRACT, [$extract_filename=fname]);
	}
