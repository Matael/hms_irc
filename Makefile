
SERVICE:=hms_irc.service
SYSTEMD_DIR:=/lib/systemd/system/
SERVICE_PATH:=$(SYSTEMD_DIR)/$(SERVICE)

all:
	@echo make install
	@echo make uninstall
	@echo make deb

deb:
	dpkg-buildpackage -us -uc -b

install:
	cp systemd/$(SERVICE) $(SERVICE_PATH)

uninstall:
	-systemctl disable $(SERVICE)
	rm $(SERVICE_PATH)
