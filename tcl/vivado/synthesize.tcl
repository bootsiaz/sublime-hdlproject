set fq_project [lindex $argv 0]
set top_module [lindex $argv 1]
open_project $fq_project
reset_run synth_1
launch_runs synth_1
wait_on_run synth_1
close_project
#start_gui
#open_checkpoint [string map {.xpr .runs} $fq_project]/synth_1/$top_module\_routed.dcp
