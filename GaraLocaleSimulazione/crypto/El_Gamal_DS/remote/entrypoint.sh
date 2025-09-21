#!/bin/bash
exec socat TCP-LISTEN:1338,reuseaddr,fork EXEC:"timeout 300 python3 chall.py"

