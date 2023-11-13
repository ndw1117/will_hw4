# will_hw4

This is a destructive/distracting tool intended to slow down a user or inhibit them completely if they cannot figure out what happened. The tool is a python script named infra.py (I chose this name so it hopefully wouldn’t look too suspicious to a rookie Blue Teamer) that renames the bin directory in a Linux system to ‘ct’ and moves it to the opt directory (for Windows, just change file paths). This will prevent the user from executing basic and essential commands. The user must either find the malicious Python file or recognize the renamed bin directory, rename it, and move it back to where it belongs. This script can be executed every few minutes using the cron service, creating an annoyance for the user even if they manage to fix the problem once. This enhances the competition by creating a sneaky but solvable problem for the Blue Team to learn from. It’s not too difficult of a challenge for a novice Blue Team member, which is good because this is a class where not everybody has a lot of experience.
In order to repeatedly execute the script in Linux, one can use the cron service:

1.	Open a crontab file for editing using crontab -e
2.	One can run the script every 5 minutes by adding the line 
*/5 * * * * /path/to/python/script/infra.py to the file. (Replace path with the path to wherever the file was put)
3.	After saving the file, the cron service should run the script accordingly. One can check existing cron jobs using crontab -l. 
