
# Sentiment Checker

This project checks the sentiment of the text given to the "/analyzer" endpoint.<br>

* used model https://huggingface.co/StatsGary/setfit-ft-sentinent-eval
* prediction comes as 0 or 1. Decided to keep 1 as "positive" and 0 as "neutral/negative"


## Installation

run the server with these commands

```bash
  python -m pip install setfit 

  cd spekterApi
  
  python manage.py runserver
  
```
    