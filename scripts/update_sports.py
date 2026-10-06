import json
from datetime import datetime

def generate_updated_data():
    data = {
        "stats": {
            "accuracyPercentage": 69.2,
            "record": "148-66",
            "lastUpdated": datetime.utcnow().strftime("%B %d, %Y - %H:%M UTC")
        },
        "games": [
            {
                "id": 1,
                "league": "NFL",
                "teamA": "Kansas City Chiefs",
                "teamB": "Buffalo Bills",
                "oddsA": "-115",
                "oddsB": "-105",
                "time": "Tonight, 8:15 PM",
                "h2hSummary": "Chiefs lead 5-2 past 4 yrs",
                "historicalNote": "Chiefs are 3-1 ATS when playing on short rest against Buffalo."
            },
            {
                "id": 2,
                "league": "CFB",
                "teamA": "Ohio State",
                "teamB": "Michigan",
                "oddsA": "-210",
                "oddsB": "+175",
                "time": "Saturday, 12:00 PM",
                "h2hSummary": "Michigan won last 3",
                "historicalNote": "Michigan has covered the spread in the last 4 consecutive matchups."
            },
            {
                "id": 3,
                "league": "WNBA",
                "teamA": "Las Vegas Aces",
                "teamB": "New York Liberty",
                "oddsA": "-140",
                "oddsB": "+120",
                "time": "Tomorrow, 7:00 PM",
                "h2hSummary": "Tied 5-5 historically",
                "historicalNote": "Aces average +4.5 point margins at home vs Liberty."
            },
            {
                "id": 4,
                "league": "NCAA",
                "teamA": "Duke Blue Devils",
                "teamB": "North Carolina",
                "oddsA": "-110",
                "oddsB": "-110",
                "time": "Wednesday, 9:00 PM",
                "h2hSummary": "UNC leads split 6-4",
                "historicalNote": "Under has hit in 5 of the last 6 matchups."
            }
        ],
        "players": [
            {"name": "Patrick Mahomes", "team": "KC", "position": "QB", "status": "Active", "recentForm": "284 YDS, 2.3 TD avg", "vsOpponentRecord": "4-1 vs Bills"},
            {"name": "Caleb Williams", "team": "CHI", "position": "QB", "status": "Active", "recentForm": "240 YDS, 1.5 TD avg", "vsOpponentRecord": "1-0 vs Packers"},
            {"name": "A'ja Wilson", "team": "LVA", "position": "F", "status": "Active", "recentForm": "24.5 PTS, 10.2 REB", "vsOpponentRecord": "12-6 vs Liberty"}
        ],
        "newsFeed": [
            {"category": "NFL Injury", "title": "Starting Left Tackle cleared for Sunday showdown", "snippet": "Medical staff greenlights full practice workload ahead of weekend kickoff.", "source": "Rotowire / Beat Report", "timestamp": "2h ago"},
            {"category": "CFB Rumors", "title": "Quarterback rotation expected for upcoming rivalry game", "snippet": "Coach hints at packages for backup dual-threat freshman in red zone.", "source": "Inside Athletics", "timestamp": "5h ago"}
        ]
    }

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Successfully updated data.json")

if __name__ == "__main__":
    generate_updated_data()
