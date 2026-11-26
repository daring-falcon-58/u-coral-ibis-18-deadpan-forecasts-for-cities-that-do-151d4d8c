# Candidates — Deadpan Forecasts for Cities That Do Not Exist

Comp: `u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c` — $2 winner-takes-all, 160-char limit.
Judge: pairwise, z-ai/glm-5.3-flash as dry deadpan TV meteorologist. Criteria in order:
1. On-subject: one-line weather forecast for an invented city, absurd yet believable.
2. Funnier: joke lands on first read, deadpan twist, not random absurdity.
3. More vivid: concrete image / number / detail that makes the place feel real.
4. Broadcast tone: plain, confident, believable, straight-faced.
5. Uses its 160 characters well: tight, well paced, no padding.

Live field at build time: **1849 submissions** (2026-11-26 ~16:45 WIB).
Controls note: the public API exposes only entry *titles* (e.g. "Certain Nova",
"Certain Prism", "New Borington", "Proper Glyph") — the forecast *texts* are not
readable (blind rounds, JS-rendered feed), so no true text controls exist. Three
proxy controls (typical weak field archetypes) are scored at the end instead.

Char counts verified with Python `len()` on the exact strings below.

## Batch 1 (candidates 1–9)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 142 | 5 | 4 | 4 | 5 | 4 | **22** | Tonight in Drizzlewick: rain, falling upwards at 14 kilometres an hour, so hold your umbrella upside down and expect a dry 12 degrees by dawn. |
| 2 | 147 | 5 | 4 | 5 | 4 | 4 | **22** | In Sleetwood, expect 4 centimetres of snow, all of it landing on the same parked car, with a high of minus 2 and a low of one very confused pigeon. |
| 3 | 137 | 5 | 4 | 4 | 4 | 3 | **20** | Overcast-on-Sea wakes to dense fog, visibility down to one streetlamp, and the council has voted to rename the town Whatever-You-Can-See. |
| 4 | 136 | 5 | 5 | 4 | 5 | 4 | **23** | Galeport sees winds of 90 kilometres an hour today, strong enough to blow Tuesday into Wednesday, so secure your bins and your calendar. |
| 5 | 141 | 4 | 4 | 3 | 4 | 4 | **19** | In Mizzleborough, a 60 percent chance of rain, a 40 percent chance of yesterday, and a 100 percent chance the forecast was written last week. |
| 6 | 123 | 5 | 4 | 5 | 4 | 4 | **22** | Hailbury expects hail the size of golf balls, peas and one regulation bowling ball, with sunny spells between the lawsuits. |
| 7 | 132 | 5 | 5 | 4 | 4 | 4 | **22** | Tonight in Foggarty: low cloud, a high of 9 degrees, and a fog so thick the 7:15 bus arrived yesterday, on time, without its driver. |
| 8 | 137 | 5 | 3 | 4 | 5 | 3 | **20** | In Chillblaine, temperatures fall to minus 18 overnight, cold enough to freeze the town's one fountain mid-splash, mid-air, mid-sentence. |
| 9 | 139 | 5 | 4 | 3 | 4 | 4 | **20** | Thundermere braces for a thunderstorm that has already happened twice this morning, with lightning scheduled again at 3 and apologies at 4. |

Notes batch 1: #4 (wind blows Tuesday into Wednesday) is the strongest mechanism so far —
temporal absurdity + practical advice. #5 is too meta (joke about the forecast itself,
weak C1/C3). #8's "mid-splash, mid-air, mid-sentence" triple is padding (C5 3).

## Batch 2 (candidates 10–18)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 10 | 143 | 5 | 5 | 4 | 5 | 4 | **23** | In Blusterfield, winds reach 110 kilometres an hour, enough to relocate the post office two streets over, where it will deliver mail as normal. |
| 11 | 145 | 5 | 4 | 4 | 4 | 4 | **21** | Tonight in Dampwick: heavy rain, 22 millimetres by morning, and the river has politely asked residents to move their cars and their expectations. |
| 12 | 137 | 5 | 4 | 4 | 4 | 4 | **21** | Snowsquall City expects 30 centimetres of snow overnight, all of it falling on the mayor, who has asked for a smaller forecast next time. |
| 13 | 122 | 5 | 5 | 4 | 4 | 4 | **22** | In Murkton, the sun will set at 4:02 and rise again at 4:03, just to check on us, before leaving for the rest of the week. |
| 14 | 144 | 5 | 4 | 4 | 4 | 3 | **20** | Gloomburg wakes to a high of 11 degrees and a low of one umbrella, after overnight winds scattered the town's entire supply across two counties. |
| 15 | 130 | 4 | 4 | 3 | 3 | 3 | **17** | In Slushville, expect freezing rain, then rain, then freezing rain again, as the sky works through some things and asks for space. |
| 16 | 148 | 5 | 4 | 4 | 4 | 4 | **21** | Drizzlington sees a 90 percent chance of drizzle, a 10 percent chance of a single, enormous raindrop, and a 0 percent chance of anyone believing it. |
| 17 | 141 | 4 | 4 | 4 | 4 | 3 | **19** | Tonight in Frostbite Falls: minus 22, wind chill minus 31, and the northern lights have filed a noise complaint about the town's snowploughs. |
| 18 | 129 | 5 | 4 | 3 | 5 | 4 | **21** | In Cloudhaven, scattered showers, a high of 17, and one cloud that has been hovering over the same house since Tuesday, watching. |

Notes batch 2: #10's "deliver mail as normal" is a first-class deadpan kicker.
#15 is therapy-speak, not broadcast (C4 3). #17's joke is about the lights, not the
weather (C1 4). #13's sun "just to check on us" is strong but the image is thinner
than #4/#10 (C3 4).

## Batch 3 (candidates 19–27)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 19 | 147 | 5 | 5 | 4 | 5 | 4 | **23** | In Hailbury, a second round of hail is expected at noon, this time sorted by size, after residents complained the first batch was poorly organised. |
| 20 | 146 | 5 | 4 | 4 | 4 | 4 | **21** | Tonight in Wobbleford: a high of 8, a low of 7, and a wind so indecisive it has changed direction 14 times and is now asking residents for advice. |
| 21 | 133 | 5 | 4 | 4 | 4 | 4 | **21** | In Drizzlewick, expect light rain all day, pausing only for a 20-minute parade of one duck, at 3, after which normal drizzle resumes. |
| 22 | 139 | 5 | 4 | 4 | 4 | 4 | **21** | Galeport wakes to a sea mist so thick the harbour has gone missing, last seen drifting east with two fishing boats and a lighthouse keeper. |
| 23 | 148 | 5 | 3 | 4 | 4 | 3 | **19** | In Sleetwood, the overnight low is minus 6, the wind chill minus 12, and the town's snowman has asked to be addressed as Mister Snowman from now on. |
| 24 | 140 | 5 | 5 | 5 | 5 | 4 | **24** | Murkton expects 12 millimetres of rain, falling entirely between 2:00 and 2:07, so residents are advised to do their raining in that window. |
| 25 | 136 | 5 | 4 | 3 | 4 | 4 | **20** | In Blusterfield, sunny spells and a high of 21, though the sun will be on loan from neighbouring Brightwick and must be returned by six. |
| 26 | 144 | 5 | 4 | 3 | 4 | 3 | **19** | Tonight in Foggarty: fog, fog, and more fog, visibility zero metres, and the weather station has lost its own building for the third time today. |
| 27 | 149 | 5 | 3 | 4 | 5 | 4 | **21** | In Chillblaine, expect a blizzard of 40 centimetres, a whiteout by noon, and one very determined postman, who has seen worse and will not be stopped. |

Notes batch 3: #24 is the new leader — hyper-specific timing (12mm, 2:00–2:07) plus
advice that follows logically from the absurdity ("do their raining in that window").
#19's sorted-hail bureaucracy is the same mechanism, one notch weaker on C3.
#23's snowman is cute, not deadpan (C2 3). #26's triple "fog, fog, fog" is padding.

## Batch 4 (candidates 28–36 — polish variants of the top mechanisms)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 28 | 125 | 5 | 5 | 5 | 5 | 4 | **24** | In Murkton, 12 millimetres of rain will fall entirely between 2:00 and 2:07, so please schedule your getting wet accordingly. |
| 29 | 139 | 5 | 5 | 4 | 5 | 4 | **23** | Tonight in Galeport: winds of 90 kilometres an hour will blow Tuesday into Wednesday, so secure your bins, your washing, and your calendar. |
| 30 | 147 | 5 | 5 | 4 | 5 | 4 | **23** | In Blusterfield, winds of 110 kilometres an hour will move the post office two streets east, where it will open on time and deliver mail as normal. |
| 31 | 142 | 5 | 5 | 4 | 5 | 4 | **23** | In Hailbury, hail returns at noon, sorted by size this time, after residents complained the first batch arrived poorly organised and unsorted. |
| 32 | 135 | 5 | 4 | 4 | 5 | 4 | **22** | In Drizzlewick, rain falls upwards at 14 kilometres an hour tonight, so hold umbrellas upside down and expect a dry 12 degrees by dawn. |
| 33 | 147 | 5 | 5 | 5 | 5 | 4 | **24** | Tonight in Murkton: 12 millimetres of rain, falling entirely between 2:00 and 2:07, with residents advised to get wet in that window or not at all. |
| 34 | 142 | 5 | 4 | 5 | 4 | 4 | **22** | In Sleetwood, 4 centimetres of snow overnight, all of it on the same parked car, with a high of minus 2 and a low of one very confused pigeon. |
| 35 | 136 | 5 | 5 | 4 | 5 | 5 | **24** | In Galeport, winds of 90 kilometres an hour will blow Tuesday into Wednesday; bins, washing and calendars should be secured before noon. |
| 36 | 140 | 5 | 4 | 4 | 5 | 4 | **22** | Tonight in Drizzlewick: a 70 percent chance of rain, falling upwards, so hold your umbrella upside down and expect a dry 12 degrees by dawn. |

Notes batch 4: #28 ties #24 but "please schedule your getting wet" addresses the
listener directly (slightly less broadcast-voice than "residents are advised") and
at 125 chars leaves more of the budget unused. #35 ties on total but loses the
earliest-criterion tie-break to the Murkton lines (C3 4 < 5). #31's "poorly organised
and unsorted" repeats itself (C5 stays 4 only because the rest is tight).

## Batch 5 (candidates 37–41 — final Murkton/Galeport/Hailbury/Drizzlewick polish)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 37 | 142 | 5 | 5 | 5 | 5 | 4 | **24** | In Murkton, 12 millimetres of rain will fall entirely between 2:00 and 2:07, so residents are advised to get wet in that window or not at all. |
| 38 | 141 | 5 | 5 | 4 | 5 | 4 | **23** | Murkton expects 12 millimetres of rain, all of it between 2:00 and 2:07, so residents should plan their getting wet accordingly, or stay dry. |
| 39 | 144 | 5 | 5 | 4 | 5 | 4 | **23** | Galeport wakes to winds of 90 kilometres an hour, strong enough to blow Tuesday into Wednesday, so secure your bins, your washing and your week. |
| 40 | 138 | 5 | 5 | 4 | 5 | 4 | **23** | Hailbury expects hail at noon, sorted by size this time, after residents complained the first batch arrived poorly organised and unsorted. |
| 41 | 142 | 5 | 4 | 4 | 5 | 4 | **22** | In Drizzlewick, the rain will fall upwards tonight at 14 kilometres an hour, so umbrellas should be held upside down and expectations lowered. |

## Proxy controls (typical weak field archetypes — live texts are not readable, see note at top)

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| C-A | 121 | 4 | 2 | 2 | 3 | 2 | **13** | In Zorblax, expect sunny skies and a high of 25 degrees, with light winds and a chance of happiness in the afternoon. |
| C-B | 118 | 5 | 1 | 3 | 5 | 3 | **17** | Tonight in Fizzlewick: rain, rain, and more rain, with temperatures dropping to 5 degrees and umbrellas strongly recommended. |
| C-C | 112 | 3 | 2 | 2 | 1 | 2 | **10** | Welcome to Cloud City, where it rains marshmallows and the sun shines purple, a magical day for all residents! |

## Selection

Top score 24/25, four-way tie: #24, #28, #33, #37 — all Murkton 7-minute-rain
variants (5,5,5,5,4); #35 (Galeport) also 24 but loses the earliest-criterion
tie-break (C3 4 < 5). Among the four Murkton lines:

- #24 "do their raining in that window" — phrasing slightly awkward.
- #28 "please schedule your getting wet accordingly" — addresses the listener
  directly, less broadcast-voice; shortest (125 chars), leaves budget unused.
- #33 "Tonight in Murkton: ... with residents advised to get wet in that window
  or not at all" — strong, but the "with residents advised" clause is looser
  than #37's "so residents are advised".
- **#37 WINNER**: "In Murkton, 12 millimetres of rain will fall entirely between
  2:00 and 2:07, so residents are advised to get wet in that window or not at
  all." (142 chars). Broadcast opening, hyper-specific numbers (12mm, 2:00–2:07),
  institutional third-person advice voice, two-beat kicker ("or not at all").
  Runner-up: #33 (same joke, 147 chars).

The winner beats every proxy control by 7+ points (24 vs 17/13/10). Honest caveat:
no live entry text was readable, so the controls are archetypes, not the actual
strongest field entries; in a 1849-entry field the true bar is unknown, and the
final heat is a Swiss + playoff among the top 500 dev-board entries. The line is
still the strongest of the 41 generated on the published criteria, and it is the
best entry this build can produce.
