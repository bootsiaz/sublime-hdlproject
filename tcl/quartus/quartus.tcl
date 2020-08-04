
set proj [lindex $argv 0]
set proj_name [file rootname [file tail $proj]] 
qexec "quartus_map $proj_name"
qexec "quartus_cdb $proj_name --merge"
qexec "quartus_fit $proj_name"
qexec "quartus_asm $proj_name"
qexec "quartus_sta $proj_name"
return
