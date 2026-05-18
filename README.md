
**_HDLProject is a Verilog and VHDL IDE for Sublime Text 4._**

---

## Features

HDLProject is designed to make RTL project navigation, FPGA project mirroring, syntax checking, and build automation feel native inside Sublime Text 4.

Key features include:

- Streamlined HDL project creation
- FPGA project mirroring for supported vendor project files
- Live local or remote syntax checking using established FPGA toolchains
- Side-by-side hierarchy and original file-system views
- On-hover popups for definitions, declarations, instances, includes, packages, and related HDL symbols
- Fast project navigation across modules, entities, hierarchy, and source files
- Support for working across multiple Sublime Text windows and HDL projects
- Vivado and Quartus Tcl build integration
- Cross-platform development on Windows, Linux, and macOS
- Compile-order generation for use with external simulation and design tools, such as ModelSim
- Optional ChatGPT integration for selected HDL code
- Flexible licensing that is not node-locked or time-limited

---

## Web

HDLProject is available through Package Control:

```text
https://packagecontrol.io/packages/HDLProject
```

---

## Installation

HDLProject is typically installed through Package Control in Sublime Text 4.

1. Open the Command Palette:

   ```text
   ctrl+shift+p
   ```

2. Search for:

   ```text
   Package Control: Install Package
   ```

3. Type:

   ```text
   HDLProject
   ```

4. Press Enter to install.

Alternatively, you can clone the repository and place it directly in your Sublime Text `Packages` folder.

---

## License

HDLProject requires a license for continued use.

Licenses are issued to a single person and may be used on any number of machines owned or used by that person. Licenses are valid for all updates within the purchased major version.

The license is:

- Not node-locked
- Not time-limited
- Valid across multiple machines for the licensed user
- Valid for all updates within the purchased major version

Licenses can be purchased by request at:

```text
sublimehdlproject@gmail.com
```

A product key will be emailed within 24 hours of purchase.

### Pricing

| License | Price |
|---|---:|
| Professional / Individual | $199 |
| Commercial Seat | $299 |
| Small Team Pack | $749 for 3 seats |
| Site License | $2,500+ |

### License Types

**Professional / Individual License**

For individual engineers, consultants, researchers, students, hobbyists, or solo users purchasing HDLProject for their own use.

**Commercial Seat**

For company-funded use, employee use at a company, reimbursed purchases, invoice or purchase-order workflows, and professional team environments.

**Small Team Pack**

For small teams that need multiple seats under a single purchase.

**Site License**

For organizations that need broader internal access, simplified deployment, or custom licensing terms.

HDLProject is a niche professional RTL productivity tool. Pricing reflects ongoing maintenance for modern HDL workflows, FPGA toolchain compatibility, and professional support expectations. It is priced as an engineering productivity tool, not as a one-off theme or syntax package.

For licensing questions, purchase requests, or support, please contact:

```text
sublimehdlproject@gmail.com
```

## Workflow

### Project Creation

For FPGA development, the simplest setup is to configure `fpga_project_file` so it points to your FPGA project file or project directory. No additional project settings are required for this workflow.

HDLProject can also create or open a project from a launcher file. For example, you can copy `my_project.hdlp` into your FPGA project directory and run the included `hdlp` script. HDLProject will create a mirrored project as long as it can detect a supported source project, such as a `.xpr`, `.xml`, or other supported project file.

On Linux, HDLProject can also be configured so supported FPGA project files, such as `.xpr` files, can be opened directly by double-clicking them. This requires a one-time MIME type and desktop launcher setup.

1. Create and register the MIME type.

   Create the required directories if they do not already exist, then copy:

   ```bash
   sublimehdlproject/shell/linux/launcher/x-xpr.xml
   ```

   to:

   ```bash
   ~/.local/share/mime/packages/
   ```

   Then update the MIME database:

   ```bash
   update-mime-database ~/.local/share/mime/
   ```

2. Create and register the desktop launcher.

   Edit the `Exec` path in:

   ```bash
   sublimehdlproject/shell/linux/launcher/hdlproject-launcher.desktop
   ```

   so it points to the included `launch_hdlproject.sh` script.

   Copy the `.desktop` file to:

   ```bash
   ~/.local/share/applications/
   ```

   Then update the desktop application database:

   ```bash
   update-desktop-database ~/.local/share/applications
   ```

3. Make the launcher script executable.

   ```bash
   chmod +x sublimehdlproject/shell/linux/launcher/launch_hdlproject.sh
   ```

4. Associate the MIME type with the HDLProject launcher.

   ```bash
   xdg-mime default hdlproject-launcher.desktop application/hdlproject
   ```

Alternatively, you can create a project by adding specific files or folders manually. See the example settings file for details.

On Windows, **Windows Developer Mode must be enabled** to use HDLProject. This is required so the plugin can create symbolic links without running Sublime Text as an administrator.

For help with project creation, please contact:

```text
sublimehdlproject@gmail.com
```

Example Linux shell command for creating a project from the current directory:

```bash
bash -c 'subl --command "create_hdl_project_shell {\"project_file_path\" : \"$(pwd)\"}"'
```

---

### Navigating the Project

HDLProject creates a directory tree made up of symbolic links to your original source files. The generated project is stored at the custom output path defined in your preferences file.

If no output path is configured, HDLProject uses the following defaults:

- Windows: `$TEMP/sublime_hdl_project`
- macOS and Linux: `~/.sublime_hdl_project`

The generated project is organized into two main directories:

- `hierarchy` — contains the hierarchical RTL view
- `libraries` — contains the original source folder structure

You can quickly move between a file in the hierarchy view and its original source location using the sidebar context menu:

- **Reveal in Sidebar File System**
- **Reveal in Sidebar Hierarchy**

These commands are available by right-clicking a file in the Sublime Text sidebar.

---

### On-Hover Definitions

After the project is loaded into memory, HDLProject provides hover popups for common HDL symbols and constructs, including:

- Ports
- Signals
- Registers
- Wires
- Constants
- Generics
- Parameters
- Defines
- Localparams
- Instances
- Variables
- Types and subtypes
- Package `use` statements
- Include statements

Hovering over a supported item for a few seconds displays a popup with definition and navigation information.

Popups can be toggled with:

- Windows/Linux: `ctrl+shift+l`
- macOS: `cmd+shift+l`

Hover popups support quick navigation within the active file and across the project. For example, hovering over a signal shows its definition and provides a link to jump to it. Assignment links, or fan-in references, are also shown when available within the active file.

Hovering over a module instance, package statement, or include statement provides navigation links, a file preview, and the ability to jump directly to a line in the referenced file.

---

### Live Syntax Checking

Syntax checking requires a supported third-party HDL tool. Configure the tool path using the `syntax_tool_path` setting.

If `syntax_tool_path` is not defined, HDLProject will attempt to use `build_tool_path`. Supported syntax tools are listed in the example user settings file.

When `check_syntax_on_save` is enabled, HDLProject runs the syntax checker whenever a VHDL or Verilog file is saved inside an active HDLProject window.

Syntax checking results are shown in several places:

- The number of errors appears in the status bar.
- Error locations are marked with gutter icons.
- Hovering over an error marker displays the corresponding syntax error message.
- The syntax log can be shown by enabling `check_syntax_panel`.

You can navigate between syntax errors with the following commands:

- `go_to_prev_syntax_error`
- `go_to_next_syntax_error`

As with most HDLProject features, syntax checking requires an active project.

#### Remote Syntax Checking

HDLProject also supports remote syntax checking. This allows you to edit locally, for example on macOS, while running syntax checks on a remote Linux machine or cloud instance.

To configure remote syntax checking, set `syntax_tool_path` to a remote path. For example:

```json
"syntax_tool_path": "ubuntu@3.96.71.89:/home/ubuntu/xilinx/Vivado/2019.2/bin"
```

You must also configure `remote_project_path`, which specifies where files will be copied on the remote machine.

To improve sync performance, use `exclude_dirs` to omit unnecessary directories.

The optional `aws_pem_key` setting can be used for SSH authentication. This has been tested with AWS EC2 and may also work with other cloud providers.

---

### ChatGPT Integration

HDLProject includes commands for sending selected HDL code to ChatGPT. Preset commands are provided, and a custom request command allows you to write your own prompt.

To use this feature, highlight text in a supported file type, such as VHDL or Verilog, then run a ChatGPT request command. The selected text is appended to the request message.

#### Setup

First, install the OpenAI Python package from the command line:

```bash
pip install --upgrade openai
```

Then configure your OpenAI API key in the HDLProject settings file.

If your API account has access to GPT-4, set `chatgpt_model` to `"gpt-4"`.

Example settings:

```json
// Settings for ChatGPT requests.
"chatgpt_api_key": "",
"chatgpt_model": "gpt-3.5-turbo",
"chatgpt_organization": "",
"chatgpt_system_content": "You are a helpful assistant."
```

The `chatgpt_organization` and `chatgpt_system_content` settings are included for future use and customization.

---

### Building FPGA Projects

HDLProject integrates with the Vivado and Quartus Tcl command-line flows.

You can create your own Tcl scripts and add their paths to the `build_tcl` list in the preferences file. These scripts can then be launched from the Command Palette using:

```text
HDLProject: Build Tcl
```

Tcl scripts can only be run after an HDLProject has been created.

Example Tcl scripts are included with the plugin to help you get started.

Builds can be cancelled at any time. Starting a new build automatically cancels any currently running build.

HDLProject includes a process manager that tracks spawned processes and terminates them when a build is cancelled or when Sublime Text 4 is closed. This supports more complex workflows, such as:

- Building an entire FPGA project
- Opening the FPGA tool GUI
- Running placement and routing analysis
- Launching custom Tcl-based automation from Sublime Text

The following arguments are passed to Tcl scripts:

| Argument | Value |
|---|---|
| `arg0` | The `project_file` setting for the active project |
| `arg1` | The `top_module` setting for the active project |
| `arg2` | The active file path from `window.active_view().file_name()` |
| `arg3` | The user-defined `user_tcl_arg` string |

---

### Retrieving Compile Order

To generate a file list in compile order, run the following command from the Command Palette:

```text
Create Compile Order
```

If a required file is missing from the project, such as a non-HDL support file, add it to the `libraries` section in the project settings.

---

### Key Bindings

#### Windows and Linux

```json
{ "keys": ["ctrl+shift+l"], "command": "toggle_hdl_popups" },
{ "keys": ["ctrl+shift+b"], "command": "cancel_tcl_build" },
{ "keys": ["alt+r"], "command": "refresh_hdl_project" }
```

#### macOS

```json
{ "keys": ["super+shift+l"], "command": "toggle_hdl_popups" },
{ "keys": ["super+shift+b"], "command": "cancel_tcl_build" }
```

---

### Command Reference

The following HDLProject commands are available from the Command Palette:

```text
open_hdl_project
delete_hdl_project
refresh_hdl_project
context_open_original_containing_folder
open_hdl_project_file
do_tcl_build
toggle_hdl_popups
create_hdl_project
generate_hdl_compile_order
check_hdl_syntax
go_to_prev_hdl_syntax_error
go_to_next_hdl_syntax_error
cleanup_module_ambiguity
open_reference_project
comment_selection
cancel_tcl_build
open_hdl_panel
open_module_by_filename
open_module_by_hierarchy
generate_file_list
open_output_path
explore_file_system_in_quick_panel
add_new_project_entry
open_hdl_parent
create_data_structure_json
update_project_generics
toggle_split_panel
create_workspace
```

Any command can be mapped to a custom key binding through:

```text
Preferences > Key Bindings
```

---

### Completions

HDLProject includes VHDL and Verilog completions for common HDL keywords.

---

### Supported Platforms

HDLProject has been tested on:

- Windows 10/11
- Ubuntu 22.04 / Pop!_OS
- macOS Ventura

---

### Syntax Highlighting

HDLProject includes forked versions of the `sublime-vhdl` and `sublime-verilog` syntax highlighting packages.

These syntaxes can be selected from the Sublime Text menu:

```text
View > Syntax > HDLProject > VHDL
View > Syntax > HDLProject > Verilog
```

The updated syntax definitions are designed to improve navigation within the active file and across the project.

Useful navigation shortcuts include:

- `ctrl+r` — opens the Goto Definition dropdown for the active file
- `ctrl+shift+r` — opens the Goto Definition dropdown for the project

The active-file dropdown allows you to jump to module instances within the current file. The project-wide dropdown allows you to jump to any module or entity definition in the project.

The syntax packages remain open source and are also available separately:

- [VHDL Syntax Package](https://github.com/bootsiaz/sublime-vhdl)
- [Verilog Syntax Package](https://github.com/bootsiaz/sublime-verilog)

#### Verilog Syntax Notes

Sublime Text 4 syntax definitions support single-line regular expression matching. Because of this limitation, the Goto Panel and color scheme detect Verilog instances only when they follow the supported formatting patterns.

For instances without parameters, place the opening parenthesis on the first line:

```verilog
instance_name module_name (
  <port_list>
);
```

For instances with parameters, use the following format:

```verilog
instance_name (
  <parameters>
) module_name (
  <port_list>
);
```

The [Boxy Theme](https://github.com/ihodev/sublime-boxy) was used while testing changes to the syntax files.

---

### HDLProject on Windows

#### Administrator Privileges

On Windows 10/11, HDLProject requires **Windows Developer Mode**. This allows HDLProject to create symbolic links without requiring Sublime Text to be run as an administrator.

Without Developer Mode, Sublime Text may need to be launched with administrator privileges for symbolic link creation to work.

#### Windows Path Character Limit

Large HDL projects can exceed the Windows `MAX_PATH` limit of 260 characters, especially when working with deeply nested hierarchies or unwrapped IP cores.

When HDLProject detects paths that exceed this limit, it automatically creates secondary hierarchy folders with appropriate naming. However, very large or deeply nested projects may still exceed the Windows path limit.

To reduce the chance of path-length issues:

- Use shorter entity, module, and IP names where possible.
- Keep project paths short.
- Enable long path support in Windows.

To enable long paths, run PowerShell as administrator and execute:

```powershell
Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -value 1
```

If HDLProject cannot create a link because of the path length limit, a warning similar to the following will be shown during project creation:

```text
WARNING: Failed to create link due to Windows 260 character limit for target: ...
```

---

## Contact

Having trouble getting started?

Contact:

```text
sublimehdlproject@gmail.com
```

## Changelog ##

#### v1.7.0 ####

* Added verilog_header_dir setting to mirror projects with verilog globals
* Updated dependencies to >= 4050
* Some support for vhdl record completion
* Fix related to multiprocessing python package changes
* Fixes for quartus syntax checking
* Other bug fixes

#### v1.5.3 ####

* Added initial ChatGPT integration.


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


**_Copyright 2026, Andrew Carter, All rights reserved._**
