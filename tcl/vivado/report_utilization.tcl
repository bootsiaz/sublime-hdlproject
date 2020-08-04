

set fq_project [lindex $argv 0]
set top_module [lindex $argv 1]
open_checkpoint [string map {.xpr .runs} $fq_project]/impl_1/$top_module\_routed.dcp
report_utilization -file "utilization.txt"
report_utilization -hierarchical -file "utilization_hierarchical.txt"

