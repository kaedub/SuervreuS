DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS device_command;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  role INTEGER NOT NULL
);

CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_connection TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE device_command (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  device_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  parameters TEXT,
  FOREIGN KEY (device_id) REFERENCES device (id)
);

INSERT INTO device (name, created, last_connection)
VALUES ('Test Device', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO device_command (device_id, name, parameters)
VALUES (1, 'lights on', '{"intesity": "int", "duration": "bigint", "color": "int"}');

