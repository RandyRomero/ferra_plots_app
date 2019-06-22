FROM python:3.7-alpine

RUN adduser -D ferra_plots

WORKDIR /home/ferra_pots

COPY ferraplots1-4c84ccdfd4cd.json ferraplots1-4c84ccdfd4cd.json
COPY app_config.py app_config.py
COPY .env .env
COPY main.py main.py
COPY make_chart.py make_chart.py
COPY plot_settings.json plot_settings.json
COPY prepare_data.py prepare_data.py
COPY requirements.txt requirements.txt
COPY orca/ orca/
COPY sources_for_charts/ sources_for_charts/
COPY boot.sh boot.sh

RUN apk add --no-cache libzmq build-base libffi-dev openssl-dev python-dev curl krb5-dev linux-headers zeromq-dev
RUN python -m venv venv
RUN python -m pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN chmod +x orca/orca-1.2.1-x86_64.AppImage
RUN chmod +x boot.sh

RUN chown -R ferra_plots:ferra_plots ./
USER ferra_plots

ENTRYPOINT ["./boot.sh"]