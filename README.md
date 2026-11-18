# 17 November 2026 — the world in one day

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/SAHUN17/makefun-news-1117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/SAHUN17/makefun-news-1117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

An entry for [make.fun's daily world-news image bounty](https://make.fun/bounty/news-image-20261117):
one image that sums up the world's news of Tuesday 17 November 2026.

`entry.png` is a 1024×1024 front page holding **27 stories from six continents**: three illustrated lead
stories, six developed stories, and eighteen one-line briefs.

## The day, as the page sets it

**Lead — Europe, war in Ukraine.** Ukrainian drones and missiles cut a road span of the
Kerch Bridge, the crossing between Russia and occupied Crimea; Russia struck two bridges
in Kyiv, and US and European envoys carried the peace talks into Berlin.

**Six developed stories**

| Region | Beat | Story |
|---|---|---|
| Middle East | Iran war | The US struck Qeshm after a drone hit its radar in Bahrain; Kuwait reported drones |
| Middle East | Hormuz | Mines set at least five ships ablaze in the strait |
| Asia | Diplomacy | Trump landed in Manila for ASEAN and the Quad; a Trump–Xi–Putin trilateral is set for Shenzhen |
| Middle East | Gaza | Germany urged Israel to let far more aid in before the winter rains |
| Economy | Nvidia | Revenue doubled to $115.8bn, the first results since Jensen Huang left the chief executive's chair |
| Health | United States | After 26 years, America lost its measles-elimination status |

**Fourteen briefs** — Dhoni's IPL retirement and Chennai's mentorship; Bilkis Bano's vow to
fight the bail given to two convicts; the chief constables' warning that forces are
"retreating from the streets"; COP31's first draft urging a fast exit from fossil fuels;
Jordan's block on Telegram; Estonia's border closures after the attack on a drone plant; a
Siberian military crash that killed 19; Mondlane's terror trial in Mozambique; an Ebola
outbreak "out of control" in DR Congo; Eritrea's trachoma elimination; a Costa Rican
journalist shot dead, the first such killing in 25 years; the UN on winter rains wrecking
tents in Gaza; Lieberman chairing the Knesset's foreign affairs committee; and Pope Leo
XIV's South American tour.

## Run it

```sh
mkdir -p out && ENTRY_OUTPUT_DIR=out python3 main.py
```

`main.py` validates the bundled image against the bounty's gate — a PNG or JPEG by its
magic bytes, at most 1 MiB, at most 1024 pixels on the long side — copies it to
`/output/entry.png`, and checks the copy against the source so a truncated write cannot
pass silently. Python 3.13, standard library only, no network, the same bytes every run.

## Craft

Everything is drawn in Pillow from primitives: cream paper with a light grain, a masthead
whose date is set at 74 px, a lead package with a hand-drawn bridge — deck, piers, the cut
span with jagged stubs, fire, smoke and drones — plus a six-card grid and a two-column
brief list, all measured to fit. No stock art, no image model: every label is set to fit
its box by measuring the rendered text, so nothing runs over a rule or into its neighbour.

## Licence

MIT. See `LICENSE`.