DROP TABLE IF EXISTS plants.flower_shop;

CREATE TABLE IF NOT EXISTS plants.flower_shop (
	plant_id INT NOT NULL,
  	species_name STRING NOT NULL,
  	variety_name STRING NOT NULL,
  	zone INT NOT NULL,
  	price INT NOT NULL
);