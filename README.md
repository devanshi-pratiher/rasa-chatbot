# RASA Chatbot: Home Automation

### RASA Version: 3.0
### Python Version: 3.8.0
### Used Linux Ubuntu

### Operations Performed:
- Ability to understand 20 user utterances/queries (including reasonable variations of those queries).
- Ability to have at least 2 multi-turn conversations where the user may ask follow-up questions once the bot responds to their original query.
- Ability to collect data from the user, e.g., on what date did the issue occur, how many items did you have in your order, etc.
- Ability to engage in some amount of small talk (e.g., hi, how are you, etc.)
- Ability to use a database (SQLite) to store information obtained from the user.

  - User starts with greetings.
  - Chatbot asks about username and password (which is saved in the database).
  - Then it inquires about Control or Status and provides options such as Light, Fan, AC, Alarms.
  - After choosing, the bot inquires about which room the user wants to make changes/ know about the status in.
  - User can make changes such as Turn light off, on, etc.
  - Also has ability to know if user is sad/ happy and appropriately responds.
  - Can understand multiple rooms and different devices that users can control/ have access to. 

### Challenges
- Initially used my laptop which is an Apple Mac M1 Pro Chip.
  - Faced many installation issues with Python version and dependencies that are in different versions correlating with the environment. 
  - Did not work after 2+ days of trying to configure issues.
- Switched to using Ubuntu laptop.
- Faced more issues since it was a really old laptop which was really slow.
- Very sensitive: small changes breaking the chatbot.
- Taking around 5 to 10 minutes to configure each change in RASA.
- Needed more time to fix bugs.


### Insights
##### Open-Source
- Rasa is an open-source platform: free and have access to the source code. 
- Save money on licensing fees and more control over the development process.

##### Customizable
- Rasa provides a high degree of flexibility and customization.
- Reliant to create a chatbot that is tailored to the specific needs of home automation system and specific users.

##### Natural Language Processing
- Rasa has powerful NLP capabilities.
- Chatbot can understand and respond to complex user queries in an intuitive way. 
- Improve user experience make it easier to interact with home automation systems.


### Build Commands
Build <br>
	rasa train nlu <br>
	rasa train <br>
	
Open a Terminal <br>
	rasa run -m models --enable-api --cors "*" -p 5021 <br>
	
Open a Terminal <br>
	rasa run action -vv <br>
	
Open Browser <br>
	home.html <br>





