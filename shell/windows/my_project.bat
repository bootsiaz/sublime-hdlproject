
SET mypath=%~dp0
set "mypath=%mypath:\=/%"
subl --command "create_hdl_project_shell {\"project_file_path\" : \"%mypath%\"}"
