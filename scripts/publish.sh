#!/usr/bin/env bash

set -euo pipefail

uv build
uv publish --trusted-publishing always
