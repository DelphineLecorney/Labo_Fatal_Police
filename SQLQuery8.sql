USE Etoile
GO

CREATE TABLE dim_Date(
	ID_dim_Date INT NOT NULL,
    date_ DATE NOT NULL,
	year_ DATE NOT NULL,
	month_ DATE NOT NULL,
	day_ INT NOT NULL,
	PRIMARY KEY (ID_dim_Date)
);

CREATE TABLE dim_UsCities(
    ID_dim_USCities INT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state_id VARCHAR(50) NOT NULL,
    state_name varchar(50) NOT NULL,
    population VARCHAR(50) NOT NULL,
    density VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID_dim_UsCities)
);

CREATE TABLE dim_Victims(
    ID_dim_Victims INT IDENTITY(1,1) PRIMARY KEY,
    name_Victims VARCHAR(50) NOT NULL,
    age_Victims INT NOT NULL,
    gender_Victims VARCHAR(50) NOT NULL,
    race_Victims VARCHAR(50) NOT NULL,
);


CREATE TABLE dim_Circumstances_Murders(
    ID_dim_Circumstances_Murders INT IDENTITY(1,1)  PRIMARY KEY,
    manner_of_death VARCHAR(50) NOT NULL,
    armed VARCHAR(50) NOT NULL,
    signs_of_mental_illness VARCHAR (50) NOT NULL,
    threat_level VARCHAR(50) NOT NULL,
    flee VARCHAR(50) NOT NULL,
);

CREATE TABLE Murders(
    ID_Murders INT NOT NULL,
	FK_date INT,
	FK_victims INT,
	FK_Circumstances_Murders INT,
	FK_UsCities INT,
    PRIMARY KEY (id_Murders),
	CONSTRAINT FK_dim_Date FOREIGN KEY (FK_date) REFERENCES dim_Date (ID_dim_Date),
	CONSTRAINT FK_dim_Victims FOREIGN KEY (FK_victims) REFERENCES dim_Victims (ID_dim_Victims),
    CONSTRAINT FK_dim_Circumstances_Murders FOREIGN KEY (FK_Circumstances_Murders) REFERENCES dim_Circumstances_Murders (ID_dim_Circumstances_Murders),
    CONSTRAINT FK_ID_dim_UsCities FOREIGN KEY (FK_UsCities) REFERENCES dim_UsCities (ID_dim_UsCities)
);