XML file handling
step 1:In this program I am creating a function to import the web-3Dayforecast.xml XML data file. This function includes exceptionhandling clauses.
Using a loop structure, I am printing the values associated with each day for each station in the XML data.
  i. day_num
  ii. wind_speed
  iii. wind_dir
step 2: I am Calculating the average max_temp for across all days for stations where the id value is greater than 03956.
step 3: I am Extracting the following information from the XML weather forecast data and writing it to a CSV file:
  • Id
  • location
  • day_num
  • wind_speed
  • wind_dir

Numpy nd array:
step 1: here I am Creating a 2-dimensional NumPy ndarray filled with 500 random numbers. Ensuring that the array has 10 rows and 50 columns. I am Computing the sum total of all entries in the first five rows and also Computing the sum total of all entries in the fifth and tenth columns.
step 2: Spliting the array from step 1 into 5 separate arrays. The number of columns in each array are equal, and there
is 10 rows in each array and Adding together corresponding array entry values from each of the 5 arrays.


Regular expressions:
Given the following string:
GPT don't chat
To me or yourself
Unless it is noon
On the Moon.
a) Using a single regular expression, write a function to highlight all occurrences of words that consist of exactly
two letters. Your answer should look like this:
GPT don't chat
{To} {me} {or} yourself
Unless {it} {is} noon
On the Moon.
b) Using another single regular expression, write another function that highlights all the first three characters on
each line. Your answer should look like this:
{GPT} don't chat
{To }me or yourself
{Unl}ess it is noon
{On }the Moon.
