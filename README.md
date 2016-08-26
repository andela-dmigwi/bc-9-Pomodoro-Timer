### bc-9-Pomodoro-Timer
Repo will hold information about a pomodoro timer

To run the app install the virtual environmnent and `requirements.txt`

###What is a pomodoro timer??
This is a timer that counts time periods each with a default interval of 25 minutes but the interval can be adjusted.  
There is a short break between each cycle with a default time of 5 minutes but its adjustable  
After the third cycle the user is forced into a long break that has a default time 15 minutes but it is also adjustable  

This app is built use __cliff__ command line framework that the implementer the right to have an almost simmilar to commmandline applications like *git*  

The pomodoro Timer application has the following commands  
1.pomodoro create\*<title> this creates a timer object with the *title* implemented as 
    `pomodoro create*Presentation2` 
2. pomodoro config_time\*<hrs:min:sec> this command modifies the default duration time 
   `pomodoro config_time*1:34:20` the interval is 1 hr 34 minutes and 20 secs 
3. pomodoro config_shortbreak\*<hrs:min:sec> 
   `pomodoro config_shortbreak*7:0` the shortbreak time is 7 minutes 0 seconds 
4. pomodoro config_longbreak*<hrs:min:sec> 
   `pomodoro config_longbreak*20:0` the longbreak time is 20 minutes 0 seconds 
5. pomodoro config_sound\*<on/off> Command sets the sound to either ring or not 
    `pomodoro config_sound*on` set sound on 
6. pomodoro timer\*<hrs:min:sec> command set time from which the timer should start counting default time is now  
   `pomodoro timer*1:30:0` command sets to start the timer to start in 1hr and 30min  
7. pomodoro start\*<title> command pushes all the data of a created task to the database  
 `pomodoro start*Presentation2` presentation2 has been set active and timer is countinng or its waiting to start counting  
8. pomodoro pause\*<title> command moves a task that is in status active to status pending which means its timer has been stopped temporarirly  
   `pomodoro pause*Presentation2` 
9. pomodoro stop\*<title> task is moved at status finished. At this status a task is considered permanently stopped or its timer rang  
   `pomodoro stop*Presentation`
10. listitems This command list all the data in the database  
  `listitems`
11. listitems byday\*<dd:mm:YYYY> This command Lists all task with the start time equal to the given parameter  
  `listitems byday*28:08:2016` check all the command with the start date as 28th August 2016  

__To do List__
  * command 6
  * command 8
  * command 11
  * command 9

Done by __Migwi Ndung'u__ @ 
###0703764266
