QA Engineer test

Setup & Execution Guide
1. Clone the base project:

- git --version
git version 2.39.5 (Apple Git-154)
- cd Desktop
- git clone https://github.com/Estoty/qa-engineer-test.git
- cd qa-engineer-test
...
Resolving deltas: 100% (30/30), done.
- cd qa-engineer-test 
- ls
Assets		Packages	ProjectSettings


2. Install prerequisites

Unity Hub + the Unity version required by the project.

- AltTester Desktop (Community Edition) → Download here: https://alttester.com/downloads/
- Select the "AltTester CE" for your operating system. (MacOs / Win)
- After downloading, install the "AltTester CE" on your computer and run it after installation.

⚠️ Important: Even Community Edition requires a license key. You need to request it from alttester.com
 or via support. Without it, AltTester Desktop will show “No current subscription”. 

Development environment:

.NET / C# with NUnit (recommended), or

Python 3.9+ with alttester package if you choose Python.


3. Open project in Unity

Start Unity Hub.

Open the cloned qa-engineer-test project.

Import AltTester Unity SDK:

Unity → Assets → Import Package → Custom Package...

Select the downloaded AltTester-Unity-SDK.unitypackage.
