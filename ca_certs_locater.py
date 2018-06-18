#!/usr/bin/env python
# Copyright (c) 2013 New Dream Network, LLC (DreamHost)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

LINUX_PATHS = (
    '/etc/ssl/certs/ca-certificates.crt',                # Debian/Ubuntu/Gentoo etc.
    '/etc/pki/tls/certs/ca-bundle.crt',                  # Fedora/RHEL 6
    '/etc/ssl/ca-bundle.pem',                            # OpenSUSE
    '/etc/pki/tls/cacert.pem',                           # OpenELEC
    '/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem'  # CentOS/RHEL 7
)


def get():
    """Return a path to a certificate authority file.
    """
    # FIXME(dhellmann): Assume Linux for now, add more OSes and
    # platforms later.
    for path in LINUX_PATHS:
        if os.path.exists(path):
            return path
    # Fall back to the httplib2 default behavior by raising an
    # ImportError if we have not found the file.
    raise ImportError()
