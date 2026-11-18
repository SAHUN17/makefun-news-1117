# 17 November 2026 — the day in six stories

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/SAHUN17/makefun-news-1117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/SAHUN17/makefun-news-1117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

An entry for [make.fun's daily world-news image bounty](https://make.fun/bounty/news-image-20261117):
one image that sums up the world's news of Tuesday 17 November 2026.

`entry.png` is a 1024×1024 front page drawn from the day's reporting — six stories,
each with a region and a beat, each legible on its own:

| Region | Beat | Story |
|---|---|---|
| Asia | Diplomacy | Trump arrives in Manila for the ASEAN summit; a Trump–Xi–Putin trilateral is set for Shenzhen on Thursday |
| Middle East | Security | The US warns Iran over an alleged "dirty bomb" plot; the White House says it sees no credible threat |
| Europe | Peace talks | Ukraine holds talks with the US and European officials; strikes hit two Kyiv bridges |
| Middle East | Aid | Germany's foreign minister urges Israel to let far more aid into Gaza before the winter rains |
| Britain | Policing | Chief constables warn forces are "retreating from the streets" under a funding crisis |
| India | Sport | M. S. Dhoni retires from the IPL and joins Chennai Super Kings as a mentor |

Six beats and five regions, chosen for consequence and spread rather than volume: a war
and its talks, a security alarm and its official rebuttal, a humanitarian warning, a
domestic funding crisis and a retirement that ends an era in the world's biggest cricket
league. Every claim is reported, and nothing is stated as fact beyond the reporting.

## Run it

```sh
mkdir -p out && ENTRY_OUTPUT_DIR=out python3 main.py
```

`main.py` validates the bundled image against the bounty's gate — PNG by magic bytes,
at most 1 MiB, at most 1024 pixels on the long side — and copies it to
`/output/entry.png`. Python 3.13, standard library only, no network, and the same bytes
on every run.

## Craft

The poster is composed in Pillow from primitives only: a cream paper with a light grain,
a masthead carrying the date at 92 px, and six cards, each with a flat pictogram, a
region-and-beat kicker, a two-line serif headline and a two-line detail. Every label is
set to fit its card by measuring the rendered text, so nothing runs over a rule or into a
neighbouring line — the failure mode that makes a news image look like a typo.

## Licence

MIT. See `LICENSE`.