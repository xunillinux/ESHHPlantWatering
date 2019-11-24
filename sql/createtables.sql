
DROP TABLE IF EXISTS humidity;
CREATE TABLE IF NOT EXISTS humidity(
	id INT NOT NULL AUTO_INCREMENT,
	humidity_value INT NOT NULL,
	measure_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( id )
);

DROP TABLE IF EXISTS brightness;
CREATE TABLE IF NOT EXISTS brightness(
	id INT NOT NULL AUTO_INCREMENT,
	brightness_value INT NOT NULL,
	measure_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( id )
);

DROP TABLE IF EXISTS temperature;
CREATE TABLE IF NOT EXISTS temperature(
	id INT NOT NULL AUTO_INCREMENT,
	temperature_value INT NOT NULL,
	measure_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( id )
);

DROP TABLE IF EXISTS foto;
CREATE TABLE IF NOT EXISTS foto(
	id INT NOT NULL AUTO_INCREMENT,
	foto_path INT NOT NULL,
	measure_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( id )
);

DROP TABLE IF EXISTS settings;
CREATE TABLE IF NOT EXISTS settings(
	id INT NOT NULL AUTO_INCREMENT,
	humidity_threshhold INT NOT NULL,
	pump_water_amount INT NOT NULL,
	PRIMARY KEY ( id )
);