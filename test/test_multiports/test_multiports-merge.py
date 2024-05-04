import backoff
import pytest


def test_multiports_and_legacy_configs_should_be_merged(docker_compose, nginxproxy):
    @backoff.on_predicate(backoff.constant, lambda r: r == False, interval=.3, max_tries=30, jitter=None)
    def expect_answer(answer, url):
        return answer in nginxproxy.get(url).text

    assert expect_answer("answer from port 80", "http://merged.nginx-proxy.tld/port") == True
    assert expect_answer("answer from port 81", "http://merged.nginx-proxy.tld/port") == True
