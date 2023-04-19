# DatGen

## What is DatGen?
DatGen stands for Data Generator and is a Python package that uses generative approach to creating synthetic data.

## How DatGen differs from other similar packages like Faker?
* DatGen uses information on the available data and models synthetic data on the real life data, so the statistical characteristics of synthetic data correspond to those observed on the actual data. Let's assume that we are interested in creating a synthetic data sets that would provide access to `age` and `amount` features. We model our data on actual commercial data set reflecting on cash transactions. In our actual data sets we can see that majority of customers are of age from 20 to 70 and value of transactions never exceed 1,000 with majority of amounts being round 50-100. DatGen will creating synthetic data with distributions reflecting those assumptions.
* Many other popular solutions derive synthetic data in the course of analysis of available distributions, DatGen leverages generative ML approach in creating synthetic observation.

## What's the purpose of DatGen
DatGen can provide an immediate access to *realistic* and *synthetic* data enabling data scientists to start working on projects immediately, without the need to wait for the access and permissions. The usual workflow assumes development of EDA and modelling artefacts and then replacing those with the proper data later in the project. DatGen is also excellent for prototyping of various visuals and interactive reporting solutions.

