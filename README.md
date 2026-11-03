# Our First Disney Trip

The family trip page for Sami and Aydin's first Disney trip and our first Disney cruise together, Nov 7 to 13, 2026.
It's published with GitHub Pages at https://ebigelow1.github.io/Disney-Trip/

How it's put together:

- `content.md` holds everything on the page. Confirmation codes, ticket numbers and reservation numbers are left out on purpose, since the page is public.
- `data.json` holds the parts that change every day: the weather table and the flight gates. A scheduled task updates it each morning, and the page loads it fresh every time it opens.
- `build.py` turns `content.md` and `template.html` into `index.html`. Run `python3 build.py` after changing `content.md`. Changing `data.json` doesn't need a rebuild.
