# starlab-website

This is a homepage that introduces NLP☆CL.

To add a new download entry, copy the template below and put it on donwloads.json and fill the details.
The file itself has to be uploaded somewhere else.
Please make sure that the link works after you have added it.

**example**
```
{
    "repo-name": "artext",
    "repo-title": "Artext: Artificial Text Generation",
    "description": "Probabilistic Noising of Natural Language",
    "last-update": "7 November 2018",
    "download-link": "/static/zip/artext.zip"
},
```

## Run

## Run Service
```bash
sudo python3 app.py
```

## Deploy
```bash
pip install fabric3
fab deploy
```

## Reference

* BlackrockDigital's startbootstrap-clean-blog repository [[github]](https://github.com/BlackrockDigital/startbootstrap-clean-blog)


## Contributors

[Seungwon](http://nlp.kaist.ac.kr/~swyoon), [Fitsum](http://nlp.kaist.ac.kr/~fgaim)
