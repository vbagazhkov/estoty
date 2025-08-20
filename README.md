QA Engineer test

Setup & Execution Guide
1. Clone the base project:

- git --version
→ git version 2.39.5 (Apple Git-154) 
- cd Desktop
- git clone https://github.com/Estoty/qa-engineer-test.git
- cd qa-engineer-test
→ ...
→ Resolving deltas: 100% (30/30), done.
- cd qa-engineer-test 
- ls
→ Assets		Packages	ProjectSettings

*Note: If you see response message after `git --version` command "xcode-select: note: No developer tools were found, requesting install. If developer tools are located at a non-default location on disk, use sudo xcode-select --switch path/to/Xcode.app to specify the Xcode that you wish to use for command line developer tools, and cancel the installation dialog. See man xcode-select for more details." . Install Xcode on your computer with `xcode-select --install` and rerun `git clone` command after installation.


2. Install prerequisites

Unity Hub + the Unity version required by the project.

- Download Unity Hub: https://unity.com/download
- In Unity Hub, add the project from the `qa-engineer-test` folder.
- Create an account for Unity Hub or log in with your existing username.
- Install the Unity Editor in the Installs tab
  
- Download AltTester Desktop (Community Edition): https://alttester.com/downloads/
- Select the "AltTester CE" for your operating system. (MacOs / Win)
- After downloading, install the "AltTester CE" on your computer and run it after installation.

⚠️ Important: Even Community Edition requires a license key. You need to request it from alttester.com or via support. Without it, AltTester Desktop will show “No current subscription”. After a short period of time (~up to 4 hours), you should receive an email confirming that your email has been added to the whitelist and you can re-register on the website to obtain a licensed key for the "AltTester CE". Enter the code you received in the activation line when you started the program.



Development environment:

.NET / C# with NUnit (recommended), or

Python 3.9+ with alttester package if you choose Python.


3. Open project in Unity

Start Unity Hub.

Open the cloned qa-engineer-test project.

Import AltTester Unity SDK:

Unity → Assets → Import Package → Custom Package...

Select the downloaded AltTester-Unity-SDK.unitypackage.
