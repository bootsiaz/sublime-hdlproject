
**_HDLProject is a Verilog and VHDL IDE for Sublime Text 4._**

---


## Features ##

* Simplify project creation
* Mirror FPGA projects
* Live local or remote syntax checking using proven FPGA tools
* Side-by-side hierarchy and file system
* On-hover popups for any definition
* Accelerated project navigation
* Multitask with multiple windows/projects
* Build integration with Vivado and Quartus
* Code on Windows/Linux/macOS
* Get compile order for use with other design tools (for example Modelsim)
* License is not node-locked or time-limited

## Web ##

https://hdlproject.com

https://packagecontrol.io/packages/HDLProject

https://bitbucket.org/bootsiaz/sublime-hdlproject/overview

## Workflow ##

### Project Creation ###

For FPGA development, you can simply use the fpga_project_file to point to the file or path of your FPGA project. No other project settings are required.

Alternatively, you can use one of the example scripts to allow for opening or creating a project by double clicking a file (or right-click Run Program on Linux).

Otherwise, you can add specific files or folders to a project. Please see the example settings file. 

On Windows, please make sure **Windows Developer Mode** is enabled to use this plugin.

For any issues with project creation, please contact me at info@fpgaland.com.

### Navigating the Project ###

The created directory structure is a tree of symlinked files and is stored at your custom output path provided in the preferences file. If not defined, it will be created at **$TEMP/sublime_hdl_project** on Windows, or **~/.sublime_hdl_project** on macOS and Linux. 

The created project is separated into a 'hierarchy' and 'libraries' directories. The 'hierarchy' contains the hierarchical RTL. The 'libraries' contains the original source folders. You can quickly jump between a file in the hierarchy to its source folder by using the sidebar **Reveal in Sidebar File System** and **Reveal in Sidebar Hierarchy** commands, accessed from the context menu when right-clicking on a file in the sidebar. 

### Building FPGA ###

HDLProject integrates with the Vivado and Quartus Tcl command line. You can create your own scripts and add their paths to the **build_tcl** list in the preferences file. These scripts can then be run from the command palette via the **HDLProject: Build Tcl** command. Note that Tcl scripts can only be run after a project has been created. Some example Tcl scripts are provided with the plugin to help get you started.

Builds can be cancelled at any time. Any succeeding build will cancel any build that is currently running. HDLProject includes a **_process manager_** object that will keep track of, and later terminate, any spawned processes when cancelling a build or closing ST4. This allows for complex tasks like building an entire FPGA project, opening the GUI, analyzing placement and routing, all from a tcl script, and initiated from ST4. 

The following parameters are passed to the tcl scripts:

* arg0: **project_file** setting from the preferences file for the active project
* arg1: **top_module** setting from the preferences file for the active project
* arg2: The file name of the open view **window.active_view().file_name()**
* arg3: User defined string **user_tcl_arg**

### On-Hover Definitions ###

Once the project is in memory, a popup will appear when hovering for a few seconds over any port, signal, reg, wire, constant, generic, parameter, define, localparam, instance, variable, type, subtype, use package or include statement. This can be disabled with ctrl+shift+l (cmd+shift+l in macOS).

Popups allow for quick navigation within the active file and project. For example, hovering over a signal will provide information on its definition as well as a link to the definition. Links to assignments (fan-in) within the file are also provided. 

Navigation links are also provided when hovering over a module instance or package/incude statement, which provides a file preview and the ability to jump to any line in that file.  

### Live Syntax Checking ###

Syntax checking requires a third-party tool installation and the location specified with the **syntax_tool_path** setting. If not defined, it will try using the **build_tool_path**. Supported tools are listed in the example user settings file. The **check_syntax_on_save** setting will call the syntax checker thread when any VHDL or Verilog file is saved within a HDL Project window. 

The number of errors is displayed in the status bar. You can navigate syntax errors in your project by using the **go_to_prev_syntax_error** and **go_to_next_syntax_error** commands. A dot is placed in the gutter to the left of the line associated with any error. Hovering over the dot will provide a popup with the error message from the syntax log. To view the syntax log, enable the **check_syntax_panel** setting. Note, as with most other tools, syntax checking only works within an active project.

Remote syntax check is now supported as well. In this way you could, for example, code on MacOS and have live syntax checking on each save. Please use syntax_tool_path with a remote path, for example:
    
    "ubuntu@3.96.71.89:/home/ubuntu/xilinx/Vivado/2019.2/bin"

The remote_project_path setting is needed to set the path on your remote machine where your files will be copied. You can use exclude_dirs to speed up the process. There is an optional setting aws_pem_key for the ssh connection which was tested on AWS EC2 (but might work on other cloud services as well).

### Retrieving Compile Order ###

To get a list of files in the right compile order, run the **Create Compile Order** command from the command palette. If a file you need is missing from the project, for example a non-HDL file, you can specify it in the 'libraries' section in the project settings.

### Key Bindings ###

Windows and Linux:

    { "keys": ["ctrl+shift+l"], "command": "toggle_hdl_popups" },
    { "keys": ["ctrl+shift+b"], "command": "cancel_tcl_build"},
    { "keys": ["alt+r"], "command": "refresh_hdl_project" },

macOS:

    { "keys": ["super+shift+l"], "command": "toggle_hdl_popups" },
    { "keys": ["super+shift+b"], "command": "cancel_tcl_build" },

### Command Reference ###

The following is a list of HDLProject commands accessible from the Command Palette (ctrl+shift+p). Any one of these commands can be mapped to keys via the Preferences->Key Bindings file.

* open_hdl_project
* delete_hdl_project
* refresh_hdl_project
* context_open_original_containing_folder
* open_hdl_project_file
* do_tcl_build
* toggle_hdl_popups
* create_hdl_project
* generate_hdl_compile_order
* check_hdl_syntax
* go_to_prev_hdl_syntax_error
* go_to_next_hdl_syntax_error
* cleanup_module_ambiguity
* open_reference_project
* comment_selection
* cancel_tcl_build
* open_hdl_panel
* open_module_by_filename
* open_module_by_hierarchy
* generate_file_list
* open_output_path
* explore_file_system_in_quick_panel
* add_new_project_entry
* open_hdl_parent
* create_data_structure_json
* update_project_generics
* toggle_split_panel
* create_workspace

### Completions ###

VHDL and Verilog completions for common keywords are included. 

### Platforms ###

* Tested on Windows 10/11, Ubuntu 22.04 (Pop!\_OS), and macOS Ventura

### Syntax Highlighting ###

HDLProject comes with forked versions of the sublime-vhdl and sublime-verilog syntax highlighting packages. These can be selected from the View menu, at View->Syntax->HDLProject->VHDL/Verilog. 

These updated syntaxes allow for uncluttered navigation of the active file and project. Typing ctrl+R brings up the Goto Definition dropdown for the active file. This allows you to jump to module instances within that file. Typing ctrl+shift+R bring up the Goto Definition dropdown for the project. This allows you to jump to any module/entity definition in the project. 

The packages remain open source. If interested, they can also be found externally here:
    * [VHDL Syntax Package](https://github.com/bootsiaz/sublime-vhdl)
    * [Verilog Syntax Package](https://github.com/bootsiaz/sublime-verilog)

##### Verilog.sublime-syntax #####

Since ST4 syntax only supports single-line regex matching, the Goto Panel and color scheme will pickup Verilog instances in only the specified format. For instances without parameters include the opening bracket on the first line. 

    instance_name module_name (
      <port_list>
    );

For instances with parameters, the following is supported. 

    instance_name (
      <parameters>
    ) module_name (
      <port_list>
    );


Note, the theme [Boxy Theme] (https://github.com/ihodev/sublime-boxy) was used for testing changes to the syntax files. 

### HDLProject on Windows ###

##### Admin Privileges #####

**_Note that to use HDLProject on Windows 10/11, it is necessary to run in Developer Mode.** This allows for the creation of symlinks. Otherwise, Sublime Text would need to be run with admin privileges.

##### Windows Path Character Limit #####

For hierarchies with paths longer than 260 characters (MAX_PATH), the Windows character limit will be exceeded. This may happen with large projects and/or when unwrapping IP cores. When the Windows MAX_PATH length is exceeded, the tool will automatically create secondary hierarchy folders with appropriate naming. But even this could run into a path length limit. It is recommended the user shrink the entity/module or IP names to as few characters as possible. 

You can get better results with long paths enabled. This can be done by running powershell as admin and using this command:

    Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -value 1

In the worst case, you will see a warning message during project creation:

    "WARNING: Failed to create link due to Windows 260 character limit for target: ..."

## License ##

HDLProject requires a monthly subscription. Licenses are valid for a single person, on any number of machines, and are valid for all upgrades to the major version purchased. The license is not node-locked nor time-limited. A license can be purchased through PayPal at https://hdlproject.com. A product key will be emailed to you within 24h of purchase.

Please contact me at **info@fpgaland.com** with any questions or concerns.

## Install ##

HDLProject is usually installed as a plugin via Package Control within Sublime Text 4. Use shift+ctrl+P, type 'install', then type 'HDLProject' and press Enter.

## Contact ##

Having trouble getting started? Please contact me at **info@fpgaland.com**!

## Changelog ##

#### v1.5.2 ####

* Fix for subscription licensing.
* Added windows project creation script.

#### v1.5.1 ####

* Fixed project creation from fpga_project_file setting on Windows.
* Added support for remote syntax check with linux client (and linux server).

#### v1.5.0 ####

* Various fixes for signal pop-ups in VHDL and Verilog
* Added multiple-tool syntax check when syntax_tool_path list has multiple entries
* Added support for fpga_project_file as a file when sole entry to simplify project creation.
* Added support for parsing Efinix projects.
* Hid split-panel mode support.
* Added intitial remote syntax checking with remote_project_path, exclude_dirs, and optional aws_pem_key.
* Fixed for compile order generation when there are VHDL packages within other packages.
* Changed licensing to subscription based with one free month
* More updates for workspaces, but not fully supported yet.

#### v1.4.5 ####

* Added expanding of paths that have environment variables.
* Fixed cleanup of all open views when syntax errors are fixed.
* Added support for project creation with just one setting when tracking FPGA projects: fpga_project_file
* Added support for fpga_project_file as a path (no recursion yet)
* Added support for global per_parse_script setting
* Added pre_parse_with_relative_paths setting for running pre_parse_script with paths realtive to fpga_project_file.

#### v1.4.4 ####

* Tentative fix for Modelsim syntax check when install dir is Mentor/modeltech...

#### v1.4.3 ####

* Cleaned up the popup follower links
* Fixed regression when parsing signals for files outside the project.

#### v1.4.2 ####

* Updates and fixes for signal follower links in popups
* Fix for panelview auto-scrolling for ST4, added new autoscroll setting.
* Fix for sync sidebar for ST4
* Bug fixes

#### v1.4.1 ####

* Added initial signal follower in popups for vhdl. 
* Added forward assignment popup links in vhdl.
* Fix for links to vhdl records with end tag name.
* Fix for inconsistent behavior after first opening ST3/4 vs after working with a project in memory. 
* Other bug fixes

#### v1.4.0 ####

* Added initial support for choosing from multiple syntax tools from command pallette.
* Started on updates for ST4.
* Changed licensing to require product key for projects with more than 50 files. 



**_Copyright 2023, Andrew Carter, All rights reserved._**
