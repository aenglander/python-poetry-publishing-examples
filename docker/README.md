Docker Hosting of Libraries
===========================

These examples all user Docker images and, more specifically, docker-compose
to provide a simple was to spin up and test hosting of python packages.

It is assumed that you have already built the library using `poetry build`

Standard Web Server
--------------------
The `nginx-server` directory contains the `docker-compose.yml` file for
hosting libraries in a web server. Just use `docker-compose up` to start
a container based on the image. It will host at `http://localhost:8080`.

Add the following ot your `project.toml` to us the repo:

```toml
[[tool.poetry.source]]
name = "foo"
url = "http://localhost:8080/"
```

or use the URL as the Index URL for PIP

```bash
pip install --index-url=http://localhost:8080 foo
```

To publish packages, add the build files to the `data` directory in a subdirectory named after the library.

For the `foo` library version `0.1.0`, you would add the directory `foo` to the `data` directory and the 
`foo-0.1.0.tar.gz` and `foo-0.1.0-py3-non-any.whl` files to the `foo` directory. The result would be:
```
data/foo/foo-0.1.0.tar.gz
data/foo/foo-0.1.0-py3-non-any.whl
``` 

PyPI Server
-----------
The `pypi-server` directory contains the `docker-compose.yml` file for
hosting libraries in a PyPI server. Just use `docker-compose up` to start
a container based on the image. It will host at `http://localhost:8080`.

Add the following ot your `project.toml` to us the repo:

```toml
[[tool.poetry.source]]
name = "foo"
url = "http://localhost:8080/simple"
```

or use the URL as the Index URL for PIP

```bash
pip install --index-url=http://localhost:8080/simple foo
```

To publish libraries to the repository, you need to add the repository to the poetry config:

```bash
poetry config repositories.local http://localhost:8080/
```

Then you would publish the current version using the command:

```bash
poetry publish --repository local --username test --password test
```

This will create the package directory and upload the sdist and wheel to the repository.