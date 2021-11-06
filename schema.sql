DROP TABLE IF EXISTS phrases,groups,users;


CREATE TABLE phrases (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  private_phrase varChar(255) NOT NULL
);

CREATE TABLE groups (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  group_name varChar(255) NOT NULL,
  private_phrase_id integer,
  FOREIGN KEY (private_phrase_id) REFERENCES phrases (id)
);

CREATE TABLE users (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  username varChar(255) NOT NULL,
  email_address varChar(255),
  first_name varChar(255),
  last_name varChar(255),
  is_staff boolean NOT NULL,
  private_phrase_id integer,
  group_id integer,
  FOREIGN KEY (private_phrase_id) REFERENCES phrases (id),
  FOREIGN KEY (group_id) REFERENCES groups (id),
);