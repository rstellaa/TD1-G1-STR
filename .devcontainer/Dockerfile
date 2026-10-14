FROM python:3.14-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        tree \
        less \
        nano \
        man-db \
        manpages \
        manpages-fr \
        manpages-fr-dev \
        lowdown \
        locales \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i '/fr_FR.UTF-8/s/^# //g' /etc/locale.gen \
    && locale-gen

ENV LANG=fr_FR.UTF-8
ENV LANGUAGE=fr_FR:fr
ENV LC_ALL=fr_FR.UTF-8

RUN python -m pip install --no-cache-dir \
    pytest \
    pycodestyle \
    numpy \
    matplotlib \
    ruff \
    pdoc \
    rich

RUN useradd -m -s /bin/bash aap

USER aap