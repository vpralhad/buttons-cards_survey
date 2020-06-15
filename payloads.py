survey_payload = {
  #"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYTVjMGM1MjAtNzk4Ny0xMWU4LTgwMzctN2I3NDhmZmFiYTZm",
 # "attachments": [
    #{
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "stretch",
                "items": [
                  {
                    "type": "TextBlock",
                    "text": "DveNet Express (DNA)",
                    "color": "Accent",
                    "size": "Medium",
                    "weight": "Bolder",
                    "fontType": "Monospace"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Post Event Survey",
                    "color": "Accent"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Virtual DevNet Express for DNA - What did you think?",
                    "wrap": True
                  }
                ]
              }
            ]
          },
          {
            "type": "TextBlock",
            "text": "Your Name*",
            "weight": "Bolder"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "maxLength": 30,
            "id": "Name"
          },
          {
            "type": "TextBlock",
            "text": "How was the website?\n",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent",
            "fontType": "Monospace"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "maxLength": 10,
            "id": "how_web"
          },
          {
            "type": "TextBlock",
            "text": "Was the event what you were expecting?",
            "weight": "Bolder"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "maxLength": 100,
            "id": "expect"
          },
          {
            "type": "TextBlock",
            "text": "About the sessions and hands-on missions",
            "size": "ExtraLarge",
            "wrap": True
          },
          {
            "type": "TextBlock",
            "text": "Some of the following sessions won't be relevant to your event, but the rest will.  \n\nPlease rate the ones that were covered at your DevNet Express.",
            "wrap": True,
            "horizontalAlignment": "Left"
          },
          {
            "type": "TextBlock",
            "text": "Getting set up and verifying the lab enviornment",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "lab_setup",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "Python Fundamentals",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "python",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "REST API fundamentals",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "restapi",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "Model-Driven Programmability",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "model_driven",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "Model-Driven Programmability: the MISSION",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "model_driven_mission",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "Guest Shell",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "guest_shell",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "Guest Shell: the MISSION",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "guest_shell_mission",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "NFVIS",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "nfvis",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "NFVIS: the MISSION",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "nfvis_mission",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "How was your level of understanding of DNA before the event?*",
            "wrap": True,
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "before",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "And after?*",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "1: Poor ... 5: Excellent"
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "id": "after",
            "maxLength": 10000
          },
          {
            "type": "TextBlock",
            "text": "General Comments",
            "weight": "Bolder"
          },
          {
            "type": "TextBlock",
            "text": "If you were very happy or very dissatisfied with anything before or during the event (content or food or anything at all!) please let us know below.  Thank you.",
            "wrap": True
          },
          {
            "type": "Input.Text",
            "placeholder": "",
            "maxLength": 10000,
            "id": "comments",
            "isMultiline": True
          },
          {
            "type": "ActionSet",
            "horizontalAlignment": "Left",
            "actions": [
              {
                "type": "Action.Submit",
                "title": "Submit",
                "data": {

                    }
              }
            ]
          }
        ]
      }
    }
