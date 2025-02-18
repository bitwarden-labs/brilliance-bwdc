#!/bin/bash

# Set variables
PASSWORD=$(bws secret get 'a44294c3-a73e-4761-ac12-b286011e62d2' | jq -r '.value')
LDAP_PASSWORD=$(bws secret get 'e8d8b83f-06ee-4e11-926f-b286011f5a21' | jq -r '.value')
LOG_DIR="/home/bwdc/logs"
LOG_FILE="${LOG_DIR}/bwdc_test_$(date +%Y-%m-%d).log"

# Ensure the log directory exists
mkdir -p "$LOG_DIR"
chmod 755 "$LOG_DIR"

# Start dbus and gnome-keyring-daemon
export $(dbus-launch)
gnome-keyring-daemon --start --daemonize --components=secrets
echo "$PASSWORD" | gnome-keyring-daemon -r -d --unlock

# Configure LDAP password and run test
bwdc config ldap.password "$LDAP_PASSWORD"
bwdc test --pretty | tee "$LOG_FILE"

# Cleanup
exit 0
