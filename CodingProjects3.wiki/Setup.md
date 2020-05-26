# Welcome to Coding Projects wiki!

Find some of my findings along the way of Coding.

I am trying to get my hands on some C++ Code and document my process along the way. This should be seen as a living document and every contribution is welcome.
 
### A. Setup of your desired IDE
#### Visual Studio Code on Mac

The following steps loosely adhere to this [tutorial](https://code.visualstudio.com/docs/languages/cpp)
1. Make sure your prerequisites are fulfilled:
* C++ compilers are installed:
clang for XCode on macOS

Simply check whether your compiler is executable on your platform path so the extension can find it. 

Do so by:
`clang --help`

2. Download VSC via <https://code.visualstudio.com/download>
3. Install and open VSC
4. Open new project

![Visual Studio Code](https://github.com/bikenthusiast/c_plusplus/blob/master/VSC.png)

task.json.
This will create a `tasks.json` file in the `.vscode` folder and open it in the editor.

Replace the contents of that file with the following:

```bash
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "label": "clang++ build active file",
      "command": "/usr/bin/clang++",
      "args": [
        "-std=c++17",
        "-stdlib=libc++",
        "-g",
        "${file}",
        "-o",
        "${fileDirname}/${fileBasenameNoExtension}"
      ],
      "options": {
        "cwd": "${workspaceFolder}"
      },
      "problemMatcher": ["$gcc"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```
VS Code creates a `launch.json` file, opens it in the editor, and builds and runs 'helloworld'. Your `launch.json ` file will look something like this:

```bash
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "clang++ - Build and debug active file",
      "type": "cppdbg",
      "request": "launch",
      "program": "${fileDirname}/${fileBasenameNoExtension}",
      "args": [],
      "stopAtEntry": true,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": false,
      "MIMode": "lldb",
      "preLaunchTask": "clang++ build active file"
    }
  ]
}
```

Now the Setup of your C++ compiler on your machine should be complete.

### B. integration of remote repository
1. Click on the remote repository administration:

![Visual Studio Code](https://github.com/bikenthusiast/c_plusplus/blob/master/VSC.png)

2. Enter the URL of your repository
3. Enter credentials of your account

# Setup Anaconda

1. Download .sh files from
2. `bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh`
set path
3. `conda config --set auto_activate_base False`
4. `source ~/.bashrc`
5. `conda create -n linear_regression python=3.6`
6. Activate ENV by `conda activate <ENV NAME>`
7. Install required packages into environment by:

```bash
pip install tensorflow
pip install keras
...
```
#Adapt Pycharm to access Anaconda