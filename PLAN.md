# Team Management Plan: The Jackson 5 Centers (Jayde69)

League: **Fantasy Ballers** (`1413931525723992064`), Sleeper NBA, 2026-27 season.
Written 2026-11-07, during week 3. Our record is 3-1.

---

## 1. League rules and what they mean for us

| Setting | Value | What it means |
|---|---|---|
| Format | **Lock-In**, head-to-head, 10 teams | Each starter's score for the week is **one game**: the game we "lock". If we don't lock, the player's **last game of the week** counts, even if it's a 0 because he sat out. |
| League-average match | On | Every week we play our opponent **and** the league median, so 2 W/L results per week. Raw point totals matter as much as the head-to-head result. |
| Lineup | PG, SG, G, SF, PF, F, C, UTIL, UTIL, plus 5 bench and 1 IR | 9 starter slots. The IR slot takes players listed Out, Suspended or DNR. It does not take GTD/DTD players. |
| Waivers | FAAB, $100 budget for the season (we haven't spent any), dropped players stay on waivers for 2 days, and a player becomes waiver-locked once his game starts | Players nobody claims become free agents and can be added instantly. We can't add a player after he has a big game and then lock that game. |
| Playoffs | 6 of 10 teams make it, playoffs start week 22, trade deadline is week 18 | Top-6 is a soft target. That gives us room to take risks for upside. |
| Keepers | 1 | Young players with upside are worth a little extra. |

### Scoring (points league)

`PTS 0.5 · 3PM +0.5 · REB 1 · AST 1 · STL 2 · BLK 2 · TO −1 · Double-double +1 · Triple-double +2 · 40-pt bonus +2 · 50-pt bonus +2 · Technical −2 · Flagrant −2`

What this scoring rewards:
- **Points are only worth half.** A 30-point scorer who doesn't rebound or pass is worth less than he looks. Guards who only score lose value.
- **Rebounds and assists count 1:1, and steals and blocks count 2x.** That makes "stat-stuffer" big men and do-everything forwards the most valuable players: Şengün, Jokić, Wembanyama, Giannis and similar. Big men who get blocks are especially valuable.
- **Turnovers cost −1.** High-usage ball handlers lose a bit of value.
- **Double-doubles (+1) and triple-doubles (+2)** add more value to big men and point forwards.
- Rule of thumb: **fantasy points per game ≈ 0.5·PTS + REB + AST + 2·(STL+BLK) − TO.** I rank players by this, computed from real stats in `tools/report.py`, not by NBA reputation.

## 2. How Lock-In works and the strategy I'll use

Lock-In is a timing game. The main strategy points from my research (RotoWire, FantasyPros' weekly "Lock or Pass" column, Sleeper support):

1. **Only starters can be locked**, and only if they were in a starting slot when the game was played. A slot's score comes from **whoever ends up locked in it**. So a bench player can rotate into a starting slot on a night he plays. If he has a big game, I lock it.
2. **Each lineup slot gets several chances a week.** With 9 slots, 5 bench spots and teams playing 3-4 games a week, we get many player-games to choose from. **A healthy, active bench is worth more here than in normal leagues. Injured players on the bench waste chances.**
3. **When to lock:** each night after games end, for every unlocked slot, I lock the game if it beats what I expect to get by waiting. Waiting means the remaining games for that player (and any bench player who can fill the slot), with some risk of a dud or a rest day. In practice:
   - Lock a **clearly above-average game** (about 20%+ above the player's average) early in the week. Lock almost any decent game late in the week.
   - **Never let a player's slot default to his last game** if he's questionable or on the second night of a back-to-back. Lock earlier or swap in someone else.
   - **Matchup context:** ahead in the matchup and above the league median → lock safe scores. Behind → wait for upside.
4. **The Sunday-night check:** before the last games of each week, every unlocked slot must hold a player who is actually playing that day. Otherwise the slot scores 0.

## 3. Where our roster stands right now

Our top 9 average about **213 fantasy points/week**, which is 5th of 10 (the best team is about 232). The core is strong (Şengün 31.9 fp/g, Towns 27.4, Bridges 25, Trae Young 23.4). **Depth is the problem: 4 of our 14 players are Out.**

| Player | Status | Plan |
|---|---|---|
| Chet Holmgren | Out, knee (patellar tendon), **8-10 weeks**, from Oct 30 | **Move to IR now.** The IR slot is empty, which wastes a roster spot. |
| Josh Hart | Out, ankle, **currently in our starting lineup** | Bench him, start Naji Marshall at F |
| Jaren Jackson Jr. | Out, knee | Watch. Drop him if the timeline is long, since IR is taken |
| Ja Morant | Out, hamstring | Hold if it's a short absence. He's a high-upside player |
| DeMar DeRozan | GTD, back; 11.7 fp/g, age 37 | **Drop candidate.** He's our worst player |

### Immediate moves I'd make (as soon as I can log in)
1. **IR Holmgren.**
2. **Add Wendell Carter Jr. (ORL, C, 20.4 fp/g, 33 min/g), drop DeRozan.** Carter would be our 5th-best player. He's projected for about 26 tonight vs GSW.
3. **Fix the lineup:** Hart out of the F slot, Marshall in, as long as that slot isn't already locked.
4. Next-best free agents on the watch list: **Anthony Black** (ORL, 20.2, plays guard and forward), **Ajay Mitchell** (OKC, 20.0), **Fred VanVleet** (HOU, 19.9), **Duncan Robinson** (DET, 19.4). If the Morant or JJJ news is bad, swap one of them for Black or Mitchell.

## 4. Routine for running the team

| When | What I do |
|---|---|
| **Daily, ~1 hour before the first game** | Refresh injuries and lineups. Make sure every unlocked slot has a healthy player whose game is today, rotating bench players in. Set the lineup. |
| **Daily, after the last game ends (~1am ET)** | Make lock decisions for that night's games using the rules in section 2. Log every decision. |
| **Daily** | Scan free agents. If a free agent scores more per game than our worst healthy player (sustained over 5+ games, with real minutes), make the swap. |
| **Before waivers process** | Place FAAB bids. Budget rules: ≤$5 for streamers, $10-25 for a breakout getting starter minutes, up to $40 once a season for a star whose role suddenly opens up. Keep at least $25 for injuries after the trade deadline. |
| **Weekly (Monday)** | Review: points vs median, which locks worked, standings, upcoming schedule (teams with 4 games = more chances). Look for trade targets: stat-stuffing forwards and centers who are undervalued because they don't score much. |
| **Trades** | I'll find and evaluate trades, but **I'll ask you before sending or accepting one.** That's the one decision I won't make alone. |

Data sources: Sleeper's public API (rosters, matchups, stats, per-game projections, injury tags) via `tools/report.py`, plus web news for injury timelines.

## 5. How moves get made (advisory mode)

You make every move yourself in the Sleeper app. I don't log in or change anything.

Every morning a scheduled task runs `tools/report.py` (Sleeper's public, read-only API), checks injury news, and sends you a short list of moves for the day:
- **Lineup:** who to swap into which slot so every unlocked slot has a player with a game today.
- **Locks:** which slot scores to lock now, using the rules in section 2. The public API shows each slot's current score but not whether it's already locked, so lock suggestions say "if not already locked".
- **Roster:** adds, drops, IR moves and FAAB bids, within the budget rules in section 4.
- **Trades:** ideas only. You decide.

Weekly review (Mondays) is folded into that morning's report.
