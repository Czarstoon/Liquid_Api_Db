
Create Table IF NOT EXISTS Users(
	id serial primary key,
	login VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,	
	date_joined TIMESTAMP NOT NULL,
	last_login TIMESTAMP,
	stripe_id varchar(255),
	is_superuser boolean,
    first_name character varying(150),
    last_name character varying(150),
    is_staff boolean,
    is_active boolean
	
	);

Create Table IF NOT EXISTS Games(
	id serial primary key,
	title VARCHAR(100) NOT NULL,
	genre VARCHAR(100) NOT NULL,
	developer VARCHAR(100) NOT NULL,	
	publisher VARCHAR(100) NOT NULL,
	cover_url VARCHAR(255) NOT NULL,
	stripe_id VARCHAR(255),
	price numeric(10,2),
    release_date date,
    description character varying(1500)
	);
CREATE TYPE status_ AS ENUM ('created','paid','expired','refunded');
Create Table IF NOT EXISTS Orders(
	id serial primary key,
	create_time TIMESTAMP NOT NULL,
	pay_time TIMESTAMP NOT NULL,
	payment_intent_id varchar(255),
	status status_,
	user_id int NOT NULL,
	total_price numeric(10,2),
    is_paid boolean,
    checkout_session_id character varying(255)
	
	);
	
Create Table IF NOT EXISTS Users_Orders_connection(
	user_id int NOT NULL,
	order_id int NOT Null,
	primary key (user_id,order_id),
	FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
	);	
Create Table IF NOT EXISTS Order_games_connection(
	id serial primary key,
	order_id int NOT NULL,
	game_id int NOT NULL,
	FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE,
	FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE
	);

CREATE TABLE IF NOT EXISTS Reviews (
  id serial primary key,
  review_text VARCHAR(1000),
  published_date timestamp DEFAULT CURRENT_TIMESTAMP,
  game_id int NOT NULL,
  user_id int NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
  );
  
 CREATE TABLE IF NOT EXISTS Ratings (
  id serial primary key,
  game_id int NOT NULL,
  user_id int NOT NULL,
  value integer,
  FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
  );
  
 CREATE TABLE IF NOT EXISTS Requirements (
  id serial primary key,
  os VARCHAR(100) NOT NULL,
  processor VARCHAR(100) NOT NULL,
  ram VARCHAR(100) NOT NULL,
  graphics_card VARCHAR(100) NOT NULL,
  directx VARCHAR(100) NOT NULL,
  drive_space VARCHAR(100) NOT NULL,
  additional_comments VARCHAR(100),
  game_id int NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Games(id) 
  );
  
 CREATE TABLE IF NOT EXISTS Screens (
  id serial primary key,
  screen_url VARCHAR(250),
  game_id int NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE
  );
  
CREATE TABLE IF NOT EXISTS User_library (
  id serial primary key,
  user_id int NOT NULL,
  game_id int NOT Null,	
  
  UNIQUE(user_id),
  FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE
  );
  
  CREATE TABLE IF NOT EXISTS cart
(
    id serial primary key,
    game_id integer NOT NULL,
    user_id integer NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
	FOREIGN KEY (game_id) REFERENCES Games(id) ON DELETE CASCADE
   
);