[![Test](https://github.com/nginx-proxy/nginx-proxy/actions/workflows/test.yml/badge.svg)](https://github.com/nginx-proxy/nginx-proxy/actions/workflows/test.yml)
[![GitHub release](https://img.shields.io/github/v/release/nginx-proxy/nginx-proxy)](https://github.com/nginx-proxy/nginx-proxy/releases)
![nginx 1.25.3](https://img.shields.io/badge/nginx-1.25.3-brightgreen.svg)
[![Docker Image Size](https://img.shields.io/docker/image-size/nginxproxy/nginx-proxy?sort=semver)](https://hub.docker.com/r/nginxproxy/nginx-proxy "Click to view the image on Docker Hub")
[![Docker stars](https://img.shields.io/docker/stars/nginxproxy/nginx-proxy.svg)](https://hub.docker.com/r/nginxproxy/nginx-proxy 'DockerHub')
[![Docker pulls](https://img.shields.io/docker/pulls/nginxproxy/nginx-proxy.svg)](https://hub.docker.com/r/nginxproxy/nginx-proxy 'DockerHub')


nginx-proxy sets up a container running nginx and [docker-gen](https://github.com/nginx-proxy/docker-gen). docker-gen generates reverse proxy configs for nginx and reloads nginx when containers are started and stopped.

See [Automated Nginx Reverse Proxy for Docker](http://jasonwilder.com/blog/2014/03/25/automated-nginx-reverse-proxy-for-docker/) for why you might want to use this.

### Usage

To run it:

```console
docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro nginxproxy/nginx-proxy:1.4
```

Then start any containers you want proxied with an env var `VIRTUAL_HOST=subdomain.youdomain.com`

```console
docker run -e VIRTUAL_HOST=foo.bar.com  ...
```

The containers being proxied must :
- [expose](https://docs.docker.com/engine/reference/run/#expose-incoming-ports) the port to be proxied, either by using the `EXPOSE` directive in their `Dockerfile` or by using the `--expose` flag to `docker run` or `docker create`.
- share at least one Docker network with the nginx-proxy container: by default, if you don't pass the `--net` flag when your nginx-proxy container is created, it will only be attached to the default bridge network. This means that it will not be able to connect to containers on networks other than bridge.

Provided your DNS is setup to forward foo.bar.com to the host running nginx-proxy, the request will be routed to a container with the `VIRTUAL_HOST` env var set.

Note: providing a port number in `VIRTUAL_HOST` isn't suported, please see [virtual ports](https://github.com/nginx-proxy/nginx-proxy/docs#virtual-ports) or [custom external HTTP/HTTPS ports](https://github.com/nginx-proxy/nginx-proxy/docs#custom-external-httphttps-ports) depending on what you want to achieve.

### Image variants

The nginx-proxy images are available in two flavors.

#### nginxproxy/nginx-proxy:(version)

This image is based on the nginx:mainline image, itself based on the debian slim image.

```console
docker pull nginxproxy/nginx-proxy:1.4
```

#### nginxproxy/nginx-proxy:(version)-alpine

This image is based on the nginx:alpine image.

```console
docker pull nginxproxy/nginx-proxy:1.4-alpine
```

#### :warning: a note on `latest` and `alpine`:

Do not use the `latest` (`nginxproxy/nginx-proxy`, `nginxproxy/nginx-proxy:latest`) or `alpine` (`nginxproxy/nginx-proxy:alpine`) tag for production setups.

Those tags are not a way of automagically updating your container with the latest features, but rather points to the latest commit in the `main` branch. They do not carry any promise of stability, and using them will most certainly put you at risk of experiencing uncontrolled updates to non backward compatible versions (or versions with breaking changes). You should always specify the version you want to use explicitly to ensure your container doesn't break when the image is updated.

### Additional documentation

Please check the [docs section](https://github.com/nginx-proxy/nginx-proxy/tree/main/docs).
