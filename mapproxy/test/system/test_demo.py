# This file is part of the MapProxy project.
# Copyright (C) 2022 Even Rouault
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from mapproxy.test.system import SysTest


@pytest.fixture(scope="module")
def config_file():
    return "demo.yaml"


class TestDemo(SysTest):

    def test_basic(self, app):
        resp = app.get("/demo/", status=200)
        assert resp.content_type == "text/html"
        assert 'href="../service?REQUEST=GetCapabilities"' in resp
        assert 'href="../service?REQUEST=GetCapabilities&tiled=true"' in resp
        assert 'href="../demo/?wmts_layer=wms_cache&format=jpeg&srs=EPSG%3A900913"' in resp
        assert 'href="../demo/?tms_layer=wms_cache&format=jpeg&srs=EPSG%3A900913"' in resp

    def test_previewmap(self, app):
        resp = app.get("/demo/?srs=EPSG%3A3857&format=image%2Fpng&wms_layer=wms_cache", status=200)
        assert resp.content_type == "text/html"
        assert '<h2>Layer Preview - wms_cache</h2>' in resp
