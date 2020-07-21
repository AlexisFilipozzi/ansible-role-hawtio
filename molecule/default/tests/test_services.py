import os

from testinfra.utils.ansible_runner import AnsibleRunner

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hawtio_service_is_started(host):
    hawtio = host.service("hawtio")
    assert hawtio.is_running
