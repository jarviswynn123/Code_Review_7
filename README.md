Part 1
- Using Python, create a BigQuery client.

- In BigQuery (using the console or the command line), in the project that the client connects to, make a new dataset called 'plants'.

- Back in the Python file (or notebook), use the client to list the datasets in the BigQuery project. Confirm that the new 'plants' dataset is there.

- In a `.sql` file in the same repository as the Python code, write the SQL code that will create a table in the `plants` dataset called `flower_shop`. Give it a schema and insert values into it so it looks like this:

```
plant_id | species_name | variety_name    | zone | price
1        | "monstera"   | "swiss_cheese"  | 5    | 20.25
2        | "cactus"     | "star"          | 8    | 8.00
3        | "cactus"     | "bunny_ear"     | 9    | 8.00
4        | "fern"       | "birds_nest"    | 6    | 12.50
5        | "cactus"     | "saguaro"       | 8    | 8.00
6        | "fern"       | "giant"         | 7    | 11.00
7        | "monstera"   | "albo"          | 5    | 14.75
8        | "cactus"     | "blue_columnar" | 8    | 9.00
9        | "cactus"     | "barrel"        | 9    | 14.50
10       | "bromeliad"  | "guzmania"      | 9    | 15.50
```


- Run the code from the `.sql` file in BigQuery, so it adds the new table to the `plants` dataset.

- Using Python, use `.list_tables()`, list the tables in the `plants` dataset, and confirm your new `flower_shop` table is there.

Part 2

The second part of the code review is fairly open-ended:

- In BigQuery, select a public dataset that interests you, and copy it to your project.

- Using Looker Studio, connect to the dataset and use it to make a visual.

- Add the visual from Looker Studio to your README. In the README, include a short description of the dataset, and what the visual is showing.


For my visualization, I chose the google bigquery public dataset lightening strikes. This dataset counts the number of lightning strikes per each day and the geometric location of that lightning strike. I narrowed the data down to the month of August, 2018 to see the days with the most amount of lightning strikes in that month.