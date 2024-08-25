To run test on your computer you should have installed all requirements.
Current basic scalable API testing framework is designed for https://alexwohlbruck.github.io/cat-facts/ API.

The test by itself contain cases described in table below:

| Case # |                             Description                              |                 Validation                  |
|:------:|:--------------------------------------------------------------------:|:-------------------------------------------:|
|   1    |              Get random fact via /facts/random endpoint              | Status 200 and response passes json schema  |
|   2    | Get fact via parameters. I.e. /facts/random?animal_type=cat&amount=2 | Status 200 and response passes json schema  |
|   3    |      Get exact fact using its ID. I.e. 591f98803b90f7150a19c229      | Status 200 and response passes json schema  |
|   4    |                   Get all facts through / endpoint                   | Status 200 and responses passes json schema |
|   5    |        Get fact that is not exist using not existed endpoint         | Status 400 and response passes json schema  |
