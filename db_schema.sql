CREATE TABLE meta (name TEXT PRIMARY KEY, value TEXT);
CREATE TABLE subscriptions (id BLOB PRIMARY KEY, query TEXT, type INTEGER, finished INTEGER, private INTEGER, date_added TEXT, instagram_id TEXT, overflow_behavior INTEGER, from_date_time INTEGER, to_date_time INTEGER, only_videos INTEGER, content_type INTEGER, attributes TEXT) WITHOUT ROWID;
CREATE TABLE intervals (id INTEGER PRIMARY KEY AUTOINCREMENT, subscriptionId BLOB, query TEXT, lastId TEXT, ts INTEGER, FOREIGN KEY(subscriptionId) REFERENCES subscriptions(id));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE photos ( id INTEGER PRIMARY KEY AUTOINCREMENT, subscriptionId BLOB, query TEXT, instagram_id TEXT, web_url TEXT, thumbnail_url TEXT, media_url TEXT, title TEXT, is_video INTEGER, created_time INTEGER, thumbnail_file TEXT, file TEXT, state INTEGER, locationId TEXT, ownerName TEXT, locationName TEXT, FOREIGN KEY(subscriptionId) REFERENCES subscriptions(id));
CREATE INDEX subscriptionId_index ON photos(subscriptionId);
CREATE INDEX intervals_index ON intervals(lastId);
