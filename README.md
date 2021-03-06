<p align="center">
    <a href="https://antiphishme.info/">
        <img width="30%" src="Logo.png" alt="AntiPhishMe Logo"/>
    </a>
</p>

# Phishing add-on backend

[![Build Status](https://travis-ci.com/TheArqsz/AntiPhishMe-backend.svg?branch=master)](https://travis-ci.com/TheArqsz/AntiPhishMe-backend)
[![codecov](https://codecov.io/gh/TheArqsz/AntiPhishMe-backend/branch/develop/graph/badge.svg)](https://codecov.io/gh/TheArqsz/AntiPhishMe-backend)
[![Python](https://img.shields.io/pypi/pyversions/Django)](https://img.shields.io/pypi/pyversions/Django)
[![License](https://img.shields.io/github/license/TheArqsz/AntiPhishMe-backend)](https://img.shields.io/github/license/TheArqsz/AntiPhishMe-backend)



## Prerequisites

- python >3.6
- pip

## Installation

```python3
pip install -r requirements.txt
```

## Run

```python3
python src/app.py
```

## UI

At default, swaggerUI can be found at `localhost:5000/api/v1/ui`

## Environmental variables

| variable's name  | definition  | example  | default value |
|:-:|:-:|:-:|:-:|
| ENV     | Define environment for project  | `DEV`, `DOCKER_DEV`, `PROD`  | `DEV` |  
| DEBUG   | If set, logging level is set to DEBUG and flask's debugger is on  | `True`, `False`  | `False` |
| PORT    | Port on which app will listen   | `5000`  | `5000` |
| HOST    | IP in which app will listen     | `127.0.0.1`, `0.0.0.0`    | `127.0.0.1` |
| DOMAIN  | Domain's name for swagger. API requests use this as target  | `localhost:5000`. `example.com` | Same as `HOST:PORT` | Varamthir
| BASE_PATH | Base path for swagger | `/api/v1` | `/api/v1` |
| URLSCAN_API_KEY | API key for urlscan.io | `-` | `-` |
| SAFEBROWSING_API_KEY | API key for safebrowsing | `-` | `-` |
| AUTH_API_KEY | API key for server and db endpoints | `-` | `test_api_key_978675645342312` |

## License

### Code

MIT License (see the [LICENSE](LICENSE) file)

### Graphic design

Copyright 2020, [Varamthir](https://github.com/NeonDreamZ)

## Contributors

- [Arqsz](https://github.com/TheArqsz)
- [Tacola](https://github.com/Tacola320)

## New features or bugs

Follow templates from (here)[https://github.com/TheArqsz/AntiPhishMe-backend/issues/new/choose]