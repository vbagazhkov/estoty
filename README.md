# QA Engineer Test Project

## Purpose
This project contains automated tests for the Unity application using AltTester Community Edition. The tests validate the counter functionality in the sample application.

## Preconditions

### Required Software
- **Unity Hub** ([download](https://unity.com/download))
- **Unity Editor 2021.3.18f1 LTS** ([download](https://unity.com/releases/editor/whats-new/2021.3.18f1))
- **AltTester Unity SDK** ([download](https://alttester.com/downloads/))
- **AltTester Desktop CE** ([download](https://alttester.com/downloads/))

### License Requirement
⚠️ **Important**: AltTester Community Edition requires a free license key. Request it from [alttester.com](https://alttester.com/) before proceeding.


## Setup & Execution Guide
1. Clone the base project:
```
# git --version
git version 2.39.5 (Apple Git-154) 
# cd Desktop
# git clone https://github.com/Estoty/qa-engineer-test.git
# cd qa-engineer-test
...
Resolving deltas: 100% (30/30), done.
# cd qa-engineer-test 
# ls
Assets		Packages	ProjectSettings
```

*Note: If you see response message after `git --version` command "xcode-select: note: No developer tools were found, requesting install. If developer tools are located at a non-default location on disk, use sudo xcode-select --switch path/to/Xcode.app to specify the Xcode that you wish to use for command line developer tools, and cancel the installation dialog. See man xcode-select for more details." . Install Xcode on your computer with `xcode-select --install` and rerun `git clone` command after installation.


2. Install prerequisites and config project

Unity Hub + the Unity version required by the project.

- Download Unity Hub: https://unity.com/download
- Download AltTester® Unity SDK: https://alttester.com/downloads/
- Create an account for Unity Hub or log in with your existing username.
- Start Unity Hub.
- Install the Unity Editor in the "Installs" tab
- In the Unity Hub, add the project from the `qa-engineer-test` folder by clicking on the Add button → Add Project from disk → Select the `qa-engineer-test` folder and click on the Open button.
- Via Terminal check Project version: `cat ~/AltTester-Unity-SDK/ProjectSettings/ProjectVersion.txt` → m_EditorVersion: 2021.3.18f1 → here we can download special Unity build for project: https://unity.com/releases/editor/whats-new/2021.3.18f1 by clicking on the "Install" button.
- In the "Project" section, click on the "Editor version" and select installed `2021.3.18f1 LTS` build from the list.
- In the "Project" section, click on your imported project and an additional window will open.
- Go to the Unity window.
- At the bottom of the Project section, click on the Assets folder, right-click and select Import Package → Custom Package, and add the previously downloaded `AltTesterUnitySDK.unitypackage` file.
- After downloading, select the Scenes folder.
- Left-click on SampleScene.unity and click the play button (triangle pointing right) at the top. After that, you should see the "Submitted" button and a counter at the bottom (If the counter is not visible, increase the display area of the scene by lowering the borders. The counter should initially display 0, and after clicking, the value increases by 1 unit).
- In order for our value to reach 10, we need to change the file:
  - At the bottom of the Project section, click on the Assets folder and find Submit file, Right-click and select Open. Visual Studio Code will open, and in the code that appears, find the method “public void OnSubmit()” → change 
```
  public void OnSubmit()
        {
            count++;
            UpdateCountText();
        }
  ```
to 
```
    public void OnSubmit()
    {
        if (count < 10)
        {
            count++;
            UpdateCountText();
        }
    }
```
  - Close Visual Studio Code Editor tab, it should automatically save the changes if not it will ask you Save or not changes, which can be seen on the right in the Inspector section.
  - Again click on the play button and press several time button "Submitted" - the counter should stop at 10.
- Go back to the Unity and in the Hierarchy and Right-click and choose Create Empty (name: AltTesterManager)
- Select AltTesterManager object (should be highlighted as blue)
- Go to the Inspector (window wight side) and click on the "Add Component" → New script → name: AltTesterManager → click on the "Create and Add" button
  



AltTester Desktop

- Download AltTester Desktop (Community Edition): https://alttester.com/downloads/
- Select the "AltTester CE" for your operating system. (MacOs / Win)
- After downloading, install the "AltTester CE" on your computer and run it after installation.

⚠️ Important: Even Community Edition requires a license key. You need to request it from alttester.com or via support. Without it, AltTester Desktop will show “No current subscription”. After a short period of time (~up to 4 hours), you should receive an email confirming that your email has been added to the whitelist and you can re-register on the website to obtain a licensed key for the "AltTester CE". Enter the code you received in the activation line when you started the program.





## Troubleshooting
### Common Issues
License Error: Ensure you have valid AltTester CE license
Connection Issues: Verify application is running before tests
Version Mismatch: Use exact Unity version 2021.3.18f1

### Support
For technical issues:
AltTester Documentation: https://alttester.com/docs/
Unity Support: https://unity.com/support

### License
This test project is created for evaluation purposes as part of Estoty Latvia's QA Engineer recruitment process.





