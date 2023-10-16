from distutils.version import StrictVersion
import subprocess
import pytest
import testinfra
from testinfra.host import Host

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
# adapted from https://testinfra.readthedocs.io/en/latest/examples.html#test-docker-images
@pytest.fixture(scope='session')
def host(request):
    subprocess.check_call(['docker', 'build', '-t', 'test-image', '.'])
    docker_id = subprocess.check_output(
        ['docker', 'run', '-td', '--entrypoint', '/bin/cat', 'test-image']).decode().strip()
    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

# adapted from https://testinfra.readthedocs.io/en/latest/examples.html#test-docker-images
@pytest.fixture(scope='session')
def host(request):
    subprocess.check_call(['docker', 'build', '-t', 'test-image', '.'])
    docker_id = subprocess.check_output(
        ['docker', 'run', '-td', '--entrypoint', '/bin/cat', 'test-image']).decode().strip()

    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])


def test_python(host: Host):
    assert host.run("python --version")

def test_python_version(host: Host):
    print(host.run("python --version | awk '{print $2}'").stdout)
    version = StrictVersion(host.run("python --version | awk '{print $2}'").stdout.strip())
    desired_version = StrictVersion('3.11.4')
    assert version == desired_version