DROP TABLE "comments", "posts", "users";

CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL UNIQUE,
	email VARCHAR(60) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	token VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS posts (
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	description TEXT,
	video_url VARCHAR(255) NOT NULL,
	author_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS comments (
	id SERIAL PRIMARY KEY,
	content TEXT NOT NULL,
	author_id INTEGER NOT NULL REFERENCES users(id),
	post_id INTEGER NOT NULL REFERENCES posts(id)
);



INSERT INTO "users" VALUES (DEFAULT, 'test1', 'test1@example.com', 'test1', 'token1');
INSERT INTO "users" VALUES (DEFAULT, 'test2', 'test2@example.com', 'test2', 'token2');
INSERT INTO "users" VALUES (DEFAULT, 'test3', 'test3@example.com', 'test3', 'token3');
INSERT INTO "users" VALUES (DEFAULT, 'test4', 'test4@example.com', 'test4', 'token4');
INSERT INTO "users" VALUES (DEFAULT, 'test5', 'test5@example.com', 'test5', 'token5');

INSERT INTO "posts" VALUES (DEFAULT, 'Crab Rave', 'bla bla', 'https://www.youtube.com/watch?v=LDU_Txk06tM', 1);
INSERT INTO "posts" VALUES (DEFAULT, 'Yeeeeee', NULL, 'https://www.youtube.com/watch?v=q6EoRBvdVPQ', 1);
INSERT INTO "posts" VALUES (DEFAULT, 'Gamecube', 'azertyuiop', 'https://www.youtube.com/watch?v=GKSoXiBlnZY', 1);
INSERT INTO "posts" VALUES (DEFAULT, 'Fuller auto', 'mandalore', 'https://www.youtube.com/watch?v=bmmqx5O10Ic', 1); ------
INSERT INTO "posts" VALUES (DEFAULT, 'I love dogs.', 'qzdhqziduqzudhq', 'https://www.youtube.com/watch?v=AK26bXWrOvo', 2);
INSERT INTO "posts" VALUES (DEFAULT, 'Tom Scott', NULL, 'https://www.youtube.com/watch?v=9SCeK6BxAI4', 2);
INSERT INTO "posts" VALUES (DEFAULT, 'Farewell.', '6333zdq4zd', 'https://www.youtube.com/watch?v=N6hVmn9FM7o', 2);
INSERT INTO "posts" VALUES (DEFAULT, 'Have you heard of the high elves?', 'elves', 'https://www.youtube.com/watch?v=gmdP11zBX44', 3);
INSERT INTO "posts" VALUES (DEFAULT, 'Pikachu', 'Fuuuuuuuu', 'https://www.youtube.com/watch?v=WSGV_n6H1n0', 4); -----
INSERT INTO "posts" VALUES (DEFAULT, 'Whats your source ?', 'MGS:R', 'https://www.youtube.com/watch?v=r7l0Rq9E8MY', 5); -----

INSERT INTO "comments" VALUES (DEFAULT, 'Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.', 1, 1);
INSERT INTO "comments" VALUES (DEFAULT, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt efficitur vehicula. Quisque congue molestie lectus, ac ornare est mollis nec. Donec et nisi consectetur, suscipit tortor et, tristique velit', 2, 1);
INSERT INTO "comments" VALUES (DEFAULT, 'test_commentary_please_ignore', 3, 1);
INSERT INTO "comments" VALUES (DEFAULT, 'Azerty', 4, 1);
INSERT INTO "comments" VALUES (DEFAULT, 'Bla bla', 5, 1);
INSERT INTO "comments" VALUES (DEFAULT, 'Super vidéo, je mabonne !', 1, 2);
INSERT INTO "comments" VALUES (DEFAULT, 'Test comment', 1, 3);
INSERT INTO "comments" VALUES (DEFAULT, 'poiuytrez', 1, 3);
INSERT INTO "comments" VALUES (DEFAULT, '123456', 1, 3);
INSERT INTO "comments" VALUES (DEFAULT, 'JOQECDKXKISYQYJIZVUTBCORVZUCGFZNHMZGAVLDTLAIFTYNBLNXCUFQHXFNIJJCRDHWYJVGFIUEJHBU', 1, 6);
INSERT INTO "comments" VALUES (DEFAULT, 'THCAFYPBTPOSYGJMBIFSNKWSLJLBSYVKTOENNOJHEGLDISPAQLFKBCVZIVSOXCUERDRSYSFXXBOVKQXX', 1, 7);
INSERT INTO "comments" VALUES (DEFAULT, 'NADSDKEOWITEAIDQYOEGZTYDQCKTWTNPTBKEIFLMUIBRWBHWKXBEIHPTDBNWJIXQHILTFBVGKHQERART', 1, 8);
INSERT INTO "comments" VALUES (DEFAULT, 'LPKTOTYVXAMJUDKXFAQOMKWTODJXXXXZWGCPPMFCJWBEAVXPFZKTLSKAZWDNHCWGXSMCLXLVKOLLXHYP', 1, 9);
INSERT INTO "comments" VALUES (DEFAULT, 'ALCTTZAMVJTXUCQOYIAYVXFKOTGSLBCQIGPHCZQHCHAAIHUBAFHWKABVGGABRZQFHCJMASJECUTXVOMZ', 1, 10);
