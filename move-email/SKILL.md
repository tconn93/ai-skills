---
name: move-email
description: A custom OpenClaw skill to move email in Gmail from one inbox/label to another. 
---

# Prompt 
To move an email you will need to make a tool call to execute the following command:  
`gog gmail labels modify {threadId}  --remove {currentLabel} --add {newLabel} `  
To be able to move a email you need to know the thread ID, current label and the new label. 