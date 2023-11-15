DROP TABLE IF EXISTS Games;
DROP TABLE IF EXISTS Rounds;
DROP TABLE IF EXISTS Scores;

-- Gamesテーブルの作成
CREATE TABLE Games
(
    game_id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    date                      TIMESTAMP,
    initial_points            INTEGER,
    return_points             INTEGER,
    player_count              INTEGER,
    score_to_money_conversion REAL,
    chips_count               INTEGER,
    game_name                 TEXT,
    uma_last_to_first         INTEGER,
    uma_third_to_second       INTEGER,
    chip_to_money_conversion  INTEGER,
    tobi_penalty              INTEGER
);

-- Roundsテーブルの作成
CREATE TABLE Rounds
(
    round_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id      INTEGER,
    round_number INTEGER,
    FOREIGN KEY (game_id) REFERENCES Games (game_id)
);

-- Scoresテーブルの作成
CREATE TABLE Scores
(
    score_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    round_id    INTEGER,
    player_name TEXT,
    score       INTEGER,
    chips_count INTEGER,
    FOREIGN KEY (round_id) REFERENCES Rounds (round_id)
);