
set fq_project [lindex $argv 0]
open_project $fq_project
write_project_tcl -all_properties -no_copy_sources -force [string map {.xpr .tcl} $fq_project]
close_project

