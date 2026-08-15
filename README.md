
# League Patch Notes Watch

An automated Python scrapper that tracks patch notes only for my specific champion pool and dispatches directly to a Discord channel via Webhooks.



## Architecture

**Scrapper:** Python + BeautifulSoup4

**Automation:** Github Actions running every other Thursday 5AM GMT+8

**Config:** Champion pool managed via JSON


## Configuration

To change or add champions to track, update the 'champs.json' file int the root directory.

```json
{
  "champions": ["tryndamere", "singed", "gragas", "garen", "jayce", "yorick", "renekton"]
}
```

The pipeline requires a GitHub repository secret named `DISCORD_WEBHOOK` containing your target Discord channel's webhook URL.

## Why I built this

League of Legends releases patch notes every two weeks, but I only care about changes affecting my champion pool. This project automatically retrieves the latest patch notes, extracts relevant champion changes, and sends them to Discord.

