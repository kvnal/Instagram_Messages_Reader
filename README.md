# Get Instagram chats in Readable Format

## How To Use
1. Get a copy of what you've shared on Instagram.
    * GoTo settings > Security > Download Data 
    * Request Download
2. Extract *.zip/.rar* and locate *__messages.txt__* file.
3. Run *run.py* in cmd/terminal.
    * To get all participants
        ```python run.py -p "/path_To_messages.txt" ```
    * To get all chats of perticular _username_
        ```python run.py -c "<username>" "/path_To_messages.txt" ```
