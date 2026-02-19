---
name: classify-unread.json
description: A custom skill for OpenClaw to start classifying all unread emails. 
---

# PROMPT
Please perform the following steps.
1. make a tool call to read `/assistant/emails/unread.json` file.
2. make a tool call to read '/assistant/emails/labels.json` file.
3. Then for each email object in `/assistant/emails/unread.json` do the following:
    1. make a tool call to execute the following command:  
      `gog gmail get {id} `
    2. Classify the email from the previous step to one of the following labels: `Needs Response`,`For your review`,`Heartland`,`Junk`, or `Spam`.  
    3. With the label you classified the email, make a tool call to execute the following command:  
    `gog gmail labels modify {id} --remove INBOX --add {classified_label}`
 4. Give the user a summary of what label you moved each email thread to.

