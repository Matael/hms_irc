
SERVICE:=hms_irc.service
SYSTEMD_DIR:=/lib/systemd/system/
SERVICE_PATH:=$(SYSTEMD_DIR)/$(SERVICE)

all:
	@echo make deb

deb:
	dpkg-buildpackage -us -uc -b
