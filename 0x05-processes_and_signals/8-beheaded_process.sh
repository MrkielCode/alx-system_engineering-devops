#!/usr/bin/env bash
# To kill a process

PID=$(pgrep -f "7-highlander")

kill -s SIGKILL "$PID"
