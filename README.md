# pull-campaign-ids
A simple Python script to automate pulling campaign IDs from form pages into a CSV file.

## Initial Setup
**Step 1:** Download this Git Repo somewhere on your computer.

Go to Code and select "Download Zip"

**Step 2:**
Download Python: https://www.python.org/ftp/python/3.14.3/python-3.14.3-macos11.pkg

**Step 3:** Open Terminal

On your Mac go to Applications > Utilities > Terminal

**Step 4:** In Terminal Navigate to pull-campaign-ids folder

Open Terminal and type cd

Then drag the pull-campaign-ids to the line after CD and press enter. Your Terminal should now be at the location of your folder.

**Step 5:** Test that the application works.

In the Terminal type: python3 id.py

Terminal should run then output a CSV file with 3 URLs and campaign IDs.

**Setup is finished!**


## Get started with pulling YOUR campaign IDs

**Step 1:** Compile your URLs. I recommend putting them in a text editor. The format must look like this:

"URL GOES HERE", "URL GOES HERE",
OR
"URL GOES HERE",
"URL GOES HERE",

**Step 2:** Copy paste your formatted URLs into id.py.

It should go after urls = [

and before

]

Once added, save.

**Step 3:** Open Terminal

**Step 4:** In Terminal Navigate to pull-campaign-ids folder

**Step 5:** Run python3 id.py

This will output your CSV file with all your campaign IDs and URLs.