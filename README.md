
**_HDLProject is a Verilog and VHDL IDE for Sublime Text 3._**

---


## Features ##

* Simplify project creation
* Side-by-side hierarchy and file system
* Integrated syntax checking/linting and error navigation with third party tools.
* On-hover popups for any definition
* Accelerated project navigation
* Multitask with multiple windows/projects
* Build integration with Vivado and Quartus
* Code on Windows/Linux/macOS
* License is not node-locked or time-limited

## Web ##

https://hdlproject.com

https://packagecontrol.io/packages/HDLProject

https://bitbucket.org/bootsiaz/sublime-hdlproject/overview

## Workflow ##

### Project Creation ###

#### Creating a Hierarchical Project from a .sublime-project File ####

A simple method of project creation is by sourcing a **_reference ST3 project_**. This ST3 .sublime-project can be easily created by opening a new view, adding folders to the project via the project menu, and saving the .sublime-project file. You can then create a HDLProject project via the command palette (ctrl+shift+p) using the **Create HDL Project** command, and selecting **_current project_** in the drop-down menu. This will create and open a new HDLProject project and write a new entry to the package settings file. 

Note that when adding folders to your reference ST3 project, all VHDL and Verilog files will be parsed. For best performance, only include folders that are required for your design. In the reference .sublime-project file, folder_exclude_patterns and file_exclude_patterns lists are supported. Wilcards for folder_exclude_patterns can be used in a limited way. For example, '\*src' will ignore all files with the string 'src' in its path. Please consult the ST3 projects docs for usage. https://www.sublimetext.com/docs/3/projects.html

If the window opens without the sidebar visible, you can select **_View->Side Bar->Show Side Bar_**

Once the hierarchical project is created, the status bar will indicate if there are any ambiguous files -- multiple HDL files with the same module/entity name. These can be cleaned up by running the **Cleanup Module Ambiguity** command from the command palette. The ambiguous modules are displayed in a drop-down list, and the user can select which path they want to keep in the project, the remaining paths will be removed. The reference .sublime-project will be automatically updated with new file_exclude_patterns.

#### Creating a Hierarchical Project from a Vivado or Quartus Project File ####

Alternatively, if using Vivado or Quartus, it makes sense to keep your HDLProject project in sync with your designs. There are a couple ways of doing this. The simplest method is to source your Vivado **_.xpr_** or Quartus **_.qsf_**. Enter the path of your vendor project file in the **_files_l_** list in the HDLProject settings file. 

You can also source a **_project Tcl_**. First, create a project Tcl in the vendor gui. Then reference this in the **_files_l_** list. If using Vivado, make sure to select "write all project properties" when generating the Tcl. (A tcl script is also included to create the project tcl for Vivado.)

#### Creating a Hierarchical Project from a List of Files and Folders ####

A third way of creating a project is to add the folders and files directly into the lists in the HDLProject package settings file. This is useful when working with well organized libraries or smaller designs.

The package settings file supports an unlimited number of project configurations.  

Use the **Refresh HDL Project** command to update the active project in memory.

### Navigating the Project ###

The created directory structure is a tree of symlinked files and is stored at your custom output path provided in the preferences file. If not defined, it will be created at **$TEMP/sublime_hdl_project** on Windows, or **~/.sublime_hdl_project** on macOS and Linux. 

The created project is separated into a 'hierarchy' and 'libraries' directories. The 'hierarchy' contains the hierarchical RTL. The 'libraries' contains the original source folders. You can quickly jump between a file in the hierarchy to its source folder by using the sidebar **Reveal in Sidebar File System** and **Reveal in Sidebar Hierarchy** commands, accessed from the context menu when right-clicking on a file in the sidebar. 

### Building FPGA ###

HDLProject integrates with the Vivado and Quartus Tcl command line. You can create your own scripts and add their paths to the **build_tcl** list in the preferences file. These scripts can then be run from the command palette via the **HDLProject: Build Tcl** command. Note that Tcl scripts can only be run after a project has been created. Some example Tcl scripts are provided with the plugin to help get you started.

Builds can be cancelled at any time. Any succeeding build will cancel any build that is currently running. HDLProject includes a **_process manager_** object that will keep track of, and later terminate, any spawned processes when cancelling a build or closing ST3. This allows for complex tasks like building an entire FPGA project, opening the GUI, analyzing placement and routing, all from a tcl script, and initiated from ST3. 

The following parameters are passed to the tcl scripts:

* arg0: **project_file** setting from the preferences file for the active project
* arg1: **top_module** setting from the preferences file for the active project
* arg2: The file name of the open view **window.active_view().file_name()**
* arg3: User defined string **user_tcl_arg**

### On-Hover Definitions ###

Once the project is in memory, a popup will appear when hovering for a few seconds over any port, signal, reg, wire, constant, generic, parameter, define, localparam, instance, variable, type, subtype, use package or include statement. This can be disabled with ctrl+shift+l (cmd+shift+l in macOS).

Popups allow for quick navigation within the active file and project. For example, hovering over a signal will provide information on its definition as well as a link to the definition. Links to assignments (fan-in) within the file are also provided. 

Navigation links are also provided when hovering over a module instance or package/incude statement, which provides a file preview and the ability to jump to any line in that file.  

### Syntax Checking (Linting) ###

Syntax checking requires a third-party tool installation and the location specified with the **syntax_tool_path** setting. If not defined, it will try using the **build_tool_path**. Supported tools are Vivado, Quartus, Modelsim, and SynplifyPro. The **check_syntax_on_save** setting will call the syntax checker thread when any file is saved within a HDL Project window. 

The number of errors is displayed in the status bar. You can navigate syntax errors in your project by using the **go_to_prev_syntax_error** and **go_to_next_syntax_error** commands. A dot is placed in the gutter to the left of the line associated with any error. Hovering over the dot will provide a popup with the error message from the syntax log. To view the syntax log, enable the **check_syntax_panel** setting. Note, as with most other tools, syntax checking only works within an active project.

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

VHDL and Verilog completions for common keywords is included. These are still under development. 

### Platforms ###

* Tested on Windows 10, Ubuntu 20.04 (Pop!\_OS), and macOS High Sierra

### Syntax Highlighting ###

HDLProject comes with forked versions of the sublime-vhdl and sublime-verilog syntax highlighting packages. These can be selected from the View menu, at View->Syntax->HDLProject->VHDL/Verilog. 

These updated syntaxes allow for uncluttered navigation of the active file and project. Typing ctrl+R brings up the Goto Definition dropdown for the active file. This allows you to jump to module instances within that file. Typing ctrl+shift+R bring up the Goto Definition dropdown for the project. This allows you to jump to any module/entity definition in the project. 

The packages remain open source. If interested, they can also be found externally here:
    * [VHDL Syntax Package](https://github.com/bootsiaz/sublime-vhdl)
    * [Verilog Syntax Package](https://github.com/bootsiaz/sublime-verilog)

##### Verilog.sublime-syntax #####

Since ST3 syntax only supports single-line regex matching, the Goto Panel and color scheme will pickup Verilog instances in only the specified format. For instances without parameters include the opening bracket on the first line. 

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

Note that on Windows, for advanced users, it is recommended to run ST3 with admin privileges. This allows for the creation of symlinks and speeds up project creation. Without admin privileges, hardlinks are created which are usually not supported by other plugins -- for example, revision control plugins. Although HDLProject itself will work just fine.

##### Network Drives #####

For a project that contains files on a network drive, you need to be running ST3 in admin mode and have the EnableLinkedConnections registry key set to "1".
https://serverfault.com/questions/780639/enablelinkedconnections-isnt-working-on-some-windows-10-machines

##### Case Sensitivity #####

Files and folders are cases sensitive on all platforms. 

##### Windows Path Character Limit #####

For hierarchies with paths longer than 260 characters (MAX_PATH), the Windows character limit will be exceeded. This may happen with large projects and/or when unwrapping IP cores. When the Windows MAX_PATH length is exceeded, the tool will automatically create secondary hierarchy folders with appropriate naming. If this becomes an issue, it is recommended the user shrink the entity/module or IP names to as few characters as possible. 

##### Symbolic Link Limit #####

On Windows, there is also a maximum number of symbolic links that can be created. This will only be reached after a very large number of projects have been created, after several months, or years, depending on usage. Therefore, it is recommended to periodically cleanout old HDLProject directories. 

## License ##

HDLProject only requires a license for projects larger than 50 files. The license is not node-locked nor time-limited. Licenses are valid for a single person, on any number of machines, and are valid for all upgrades to the major version purchased. A license can be purchased through PayPal at https://hdlproject.com. 

Please contact me at **info@intrachip.com** with any questions or concerns.

## Install ##

HDLProject is usually installed as a plugin via Package Control within Sublime Text 3. Use shift+ctrl+P, type 'install', then type 'HDLProject' and press Enter.

## Contact ##

Please contact me at **info@intrachip.com** with any questions or concerns.

## Changelog ##

#### v1.4.0 ####

* Added initial support for choosing from multiple syntax tools from command pallette.
* Started on updates for ST4.
* Changed licensing to require product key for projects with more than 50 files. 

#### v1.3.0 ####

* Added support for Modelsim linting via **syntax_tool_path** setting as per user request.
* Added support for SynplifyPro syntax checking via **syntax_tool_path** setting as per user request.
* Fix for generating compile order with nested packages/includes.
* Added syntax_log.txt to project top level.  
* Added project refresh key binding as per user suggestion, to alt+r. 
* Bug fixes.

#### v1.2.0 ####

* Added support for extending completions to all files in scope. 
* Added new boolean setting "extend_completions".
* Added syntax support for 'localparam integer' and 'localparam int'
* Added initial support for creating workspaces, though can't do anything with them yet. 
* Sped up project creation and refresh, especially on Linux. 
* Deprecated "post_refresh_update_generics" setting. 
* Added "parse_generics_and_parameters" setting. 
* Added limited support to wildcards in folder_exclude_patterns
* Bug fixes.


#### v1.1.5 ####

* Added initial support for popups in standalone VHDL and Verilog files as per user request.
* Added popups_enabled setting
* Added post_refresh_check_syntax setting
* Added post_refresh_update_generics setting
* Added expand_hierarchy_on_win_path_limit setting for Windows
* Bugfix to detect moved source files during refresh project
* Bugfix for records not being picked up in signal assignment list
* Fix for popup link line numbers



**_Copyright 2020, IntraChip Solutions Inc., All rights reserved._**
