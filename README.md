# Scrape DOR Milwaukee Real Estate Transfer Data

A postprocess script in Github's Flat Data actions is used to fire a Python script that collects real estate transfer data

## Execution :

- the Flat Data action is scheduled daily.

- the `postprocess.ts` script is then run, triggers the install of python packages, and runs the main python script `postprocess.py`.

- `postprocess.py` prints out its received arguments, and then generates a CSV file `flat_retr.csv`. 

## Thanks

- Thanks to the Github Octo Team
- Thanks to [Pierre-Olivier Simonard](https://github.com/pierrotsmnrd/flat_data_py_example) for his repo on implementing Flat data as a Python postprocess file.

