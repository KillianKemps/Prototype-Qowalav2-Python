*Caution:* This prototype is under heavy development and should be tested carefully

Current version will start Twitter and Reddit streams simultaneously.

Create a virtualenv
```
virtualenv venv
```

Source the venv:
```
source venv/bin/activate
```

Install dependencies:
```
pip install -U requirements.txt
```

Create a JSON at `plugins/Qtwitter/tokens.json` with your credentials:
```
{
"CONSUMER_KEY" : "",
"CONSUMER_SECRET" : "",
"ACCESS_KEY" : "",
"ACCESS_SECRET" : ""
}
```

Start the app with following command:

```
python app.py
```
