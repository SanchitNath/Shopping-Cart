# Frontend BDD Automation

# Installation Steps

This project requires :- pytest, selenium, behave to be installed

```
sudo apt-get update
pip install -U pytest
sudo apt-get install python3-selenium
sudo pip install pytest-bdd
sudo apt-get install python3-behave
behave --version
```

Install Gherkin Plugin :-
```
File > Settings > Plugins > Marketplace
Search "Gherkin"
Install it
```

Use pip to install Pipenv, if not installed :-
```
pip install --user pipenv
```

# End-to-end tests
To run any feature file:
```
1. Setup configuration by entering name, path of features folder
2. behave test/features/{filename}.feature
```

If tag is used, run ->
```
2. behave tests/features/{filename}.feature --tags {tagname}
```


To delete - screenshots, reports, testSuite file generated in one shot :-
```
rm -rf screenshot/ reports/ testSuite-*
```
