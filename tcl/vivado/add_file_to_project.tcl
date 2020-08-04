
set fq_project [lindex $argv 0]
set curr_file [lindex $argv 2]
open_project $fq_project
add_file $curr_file
close_project

