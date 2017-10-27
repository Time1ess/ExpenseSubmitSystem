FROM python:3.5
MAINTAINER youchen <youchen.du@gmail.com>
USER root

RUN apt-get update
RUN apt-get install -y gettext

RUN git clone https://github.com/Time1ess/ExpenseSubmitSystem
VOLUME ["/ExpenseSubmitSystem/static", "/ExpenseSubmitSystem/media"]

RUN chmod a+x /ExpenseSubmitSystem/web/entrypoint.sh

EXPOSE 8005

ENV ExpenseSubmitSystem_SETTINGS production
ENTRYPOINT ["/ExpenseSubmitSystem/web/entrypoint.sh"]
