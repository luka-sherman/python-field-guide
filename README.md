Python Field Guide

I was trying to find a good all-in-one cheatsheet for highschool python students and couldn't find anything I liked that they would consistently use. I needed:
- quick intuitive navigation
- was simple enough to understand for beginners, without advanced topics that overwhelmed
- free 
- clean minimal UI

I went with mkdocs because I needed a lightweight markdown library and liked that this was in python. 

I implemented pyodide blocks so that users could instantly experiment with each new concept.

When I found myself overriding too much, I switched over to the Material for Mkdocs theme so I could stop reinventing the wheel. 

## Running locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve   # live-reloading dev server at http://127.0.0.1:8000
```

## Deploying

Pushes to `main` are automatically built and published to GitHub Pages by
[.github/workflows/deploy.yml](.github/workflows/deploy.yml), which runs `mkdocs gh-deploy`
to push the built site to the `gh-pages` branch. No manual deploy step is needed — just push
to `main`.

The repo's GitHub Pages source (Settings → Pages) needs to point at the `gh-pages` branch for
this to take effect.

## License

The content and code in this repo are not licensed for reuse — see [LICENSE](LICENSE).