mkdir pronto/data
echo "Here is the README file for data file of the data year one" > README.txt
cd pronto/data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head *.csv

