#!/usr/bin/env python3
"""Pull Sleeper league data and print our roster + best free agents under league scoring.

Usage: python3 tools/report.py [week]
Data is cached in data/ (git-ignored). Read-only: uses Sleeper's public API.
"""
import collections, json, os, subprocess, sys

LEAGUE = "1413931525723992064"
OUR_ROSTER_ID = 1  # Jayde69 / The Jackson 5 Centers
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def get(url, name):
    path = os.path.join(DATA, name)
    subprocess.run(["curl", "-sSf", "-o", path, url], check=True)
    with open(path) as f:
        return json.load(f)


def main():
    os.makedirs(DATA, exist_ok=True)
    state = get("https://api.sleeper.app/v1/state/nba", "state.json")
    week = int(sys.argv[1]) if len(sys.argv) > 1 else state["leg"]
    season = state["season"]
    league = get(f"https://api.sleeper.app/v1/league/{LEAGUE}", "league.json")
    rosters = get(f"https://api.sleeper.app/v1/league/{LEAGUE}/rosters", "rosters.json")
    players = get("https://api.sleeper.app/v1/players/nba", "players_nba.json")
    stats = get(f"https://api.sleeper.com/stats/nba/{season}?season_type=regular", "season_stats.json")
    proj = get(f"https://api.sleeper.com/projections/nba/{season}/{week}?season_type=regular", "week_proj.json")
    scoring = league["scoring_settings"]
    fp = lambda st: sum(st.get(k, 0) * v for k, v in scoring.items())

    avg = {}
    for r in stats:
        gp = r["stats"].get("gp", 0)
        if gp:
            avg[r["player_id"]] = (gp, fp(r["stats"]) / gp, r["stats"].get("min", 0) / gp)
    games = collections.defaultdict(list)
    for x in proj:
        games[x["player_id"]].append((x["date"][5:], x.get("opponent"), round(fp(x["stats"]), 1)))
    owned = {p for r in rosters for p in (r["players"] or [])}
    ours = next(r for r in rosters if r["roster_id"] == OUR_ROSTER_ID)

    def line(pid, tag=""):
        p = players.get(pid, {})
        gp, a, m = avg.get(pid, (0, 0, 0))
        return (f"{tag:3}{p.get('full_name', pid)[:22]:22} {str(p.get('team')):4} "
                f"{'/'.join(p.get('fantasy_positions') or []):9} {str(p.get('injury_status') or ''):4} "
                f"gp{gp:>3.0f} {a:5.1f} fp/g {m:4.1f} min  wk{week}: {games.get(pid, [])}")

    print(f"Week {week} - our roster")
    for pid in ours["players"]:
        tag = "S" if pid in ours["starters"] else ("IR" if pid in (ours.get("reserve") or []) else "")
        print(line(pid, tag))
    matchups = get(f"https://api.sleeper.app/v1/league/{LEAGUE}/matchups/{week}", "matchups.json")
    me = next((m for m in matchups if m["roster_id"] == OUR_ROSTER_ID), None)
    if me:
        opp = next((m for m in matchups if m["matchup_id"] == me["matchup_id"] and m is not me), None)
        pts = sorted(m["points"] or 0 for m in matchups)
        median = (pts[len(pts) // 2 - 1] + pts[len(pts) // 2]) / 2
        print(f"\nMatchup wk{week}: us {me['points']} vs roster {opp and opp['roster_id']} {opp and opp['points']}; league median {median}")
        print("Current slot scores (locked game, or latest game if unlocked):")
        for pid, p in zip(me["starters"], me.get("starters_points") or []):
            print(f"   {players.get(pid, {}).get('full_name', pid):22} {p}")

    print("\nTop free agents (>=3 games)")
    fa = [p for p in avg if p not in owned and players.get(p, {}).get("team") and avg[p][0] >= 3]
    for pid in sorted(fa, key=lambda p: -avg[p][1])[:25]:
        print(line(pid))


if __name__ == "__main__":
    main()
