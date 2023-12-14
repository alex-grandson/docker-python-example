# python 3.11

Base: `python:3.11.4-alpine3.18`

Packages included:

| Package                   | Version   | Reason installed                                                                                                                                                    |
| :------------------------ | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `findutils`               | `4.9.0`   |                                                                                                                                                                     |
| `gcc`                     | `12.2.1`  |                                                                                                                                                                     |
| `git`                     | `2.40.1`  |                                                                                                                                                                     |
| `gnupg`                   | `2.4.3`   |                                                                                                                                                                     |
| `libc-dev`                | `0.7.2`   |                                                                                                                                                                     |
| `libcrypto3`              | `3.1.4`   | Fix vulnerability issue (Medium: [CVE-2023-5363](https://avd.aquasec.com/nvd/cve-2023-5363))                                                                        |
| `libcurl`                 | `8.5.0`   | Fix vulnerability issue (Critical: [CVE-2023-38545](https://avd.aquasec.com/nvd/cve-2023-38545), Low: [CVE-2023-38546](https://avd.aquasec.com/nvd/cve-2023-38546)) |
| `libssl3`                 | `3.1.4`   | Fix vulnerability issue (Medium: [CVE-2023-5363](https://avd.aquasec.com/nvd/cve-2023-5363))                                                                        |
| `make`                    | `4.4.1`   |                                                                                                                                                                     |
| `nghttp2`, `nghttp2-libs` | `1.57.0`  | Fix vulnerability issue (High: [CVE-2023-44487](https://avd.aquasec.com/nvd/cve-2023-44487))                                                                        |
| `openssh-client`          | `9.3_p2`  |                                                                                                                                                                     |
| `pip`                     | `23.3.1`  | Fix vulnerability issue (Medium: [CVE-2023-5752](https://avd.aquasec.com/nvd/cve-2023-5752))                                                                        |
| `tar`                     | `1.34`    |                                                                                                                                                                     |
| `virtualenv`              | `20.24.5` |                                                                                                                                                                     |
| `xz`                      | `5.4.3`   |                                                                                                                                                                     |


## Testing 

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r tests/requirements.txt
pytest
```
