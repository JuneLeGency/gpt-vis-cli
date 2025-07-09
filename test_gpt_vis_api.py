import pytest
import os
from gpt_vis_api import render

def assert_image_equal(buffer: bytes, name: str):
    snapshot_dir = 'charts/__tests__/snapshot'
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)

    expected_path = os.path.join(snapshot_dir, f'{name}.png')
    
    if not os.path.exists(expected_path):
        if os.environ.get('CI') == 'true':
            pytest.fail(f"Snapshot file not found: {expected_path}. Please generate it locally.")
        
        with open(expected_path, 'wb') as f:
            f.write(buffer)
        print(f"Generated new snapshot: {expected_path}")
        return

    with open(expected_path, 'rb') as f:
        expected_buffer = f.read()

    if buffer != expected_buffer:
        actual_path = os.path.join(snapshot_dir, f'{name}-actual.png')
        with open(actual_path, 'wb') as f:
            f.write(buffer)
        pytest.fail(f"Image does not match snapshot. Actual image saved at {actual_path}")

    # Clean up actual file if test passes
    actual_path = os.path.join(snapshot_dir, f'{name}-actual.png')
    if os.path.exists(actual_path):
        os.remove(actual_path)

class TestSSRRendering:
    def test_area(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'area',
            'data': [
                {'time': '1991', 'value': 3},
                {'time': '1992', 'value': 4},
                {'time': '1993', 'value': 3.5},
                {'time': '1994', 'value': 5},
                {'time': '1995', 'value': 4.9},
                {'time': '1996', 'value': 6},
                {'time': '1997', 'value': 7},
                {'time': '1998', 'value': 9},
                {'time': '1999', 'value': 13},
            ],
            'axisXTitle': 'Time',
            'axisYTitle': 'Value',
            'title': 'Area Chart',
        })
        assert_image_equal(vis_bytes, 'area')

    def test_area_required(self):
        vis_bytes = render({
            'type': 'area',
            'data': [
                {'time': '1991', 'value': 3},
                {'time': '1992', 'value': 4},
                {'time': '1993', 'value': 3.5},
                {'time': '1994', 'value': 5},
                {'time': '1995', 'value': 4.9},
                {'time': '1996', 'value': 6},
                {'time': '1997', 'value': 7},
                {'time': '1998', 'value': 9},
                {'time': '1999', 'value': 13},
            ],
        })
        assert_image_equal(vis_bytes, 'area-required')

    def test_area_rough(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'area',
            'texture': 'rough',
            'data': [
                {'time': '1991', 'value': 3},
                {'time': '1992', 'value': 4},
                {'time': '1993', 'value': 3.5},
                {'time': '1994', 'value': 5},
                {'time': '1995', 'value': 4.9},
                {'time': '1996', 'value': 6},
                {'time': '1997', 'value': 7},
                {'time': '1998', 'value': 9},
                {'time': '1999', 'value': 13},
            ],
            'axisXTitle': 'Time',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'area-rough')

    def test_area_academy(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'area',
            'theme': 'academy',
            'data': [
                {'time': '1991', 'value': 3},
                {'time': '1992', 'value': 4},
                {'time': '1993', 'value': 3.5},
                {'time': '1994', 'value': 5},
                {'time': '1995', 'value': 4.9},
                {'time': '1996', 'value': 6},
                {'time': '1997', 'value': 7},
                {'time': '1998', 'value': 9},
                {'time': '1999', 'value': 13},
            ],
            'axisXTitle': 'Time',
            'axisYTitle': 'Value',
            'title': 'Area Chart',
        })
        assert_image_equal(vis_bytes, 'area-academy')

    def test_area_grouped(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'area',
            'data': [
                {'time': 'Jan', 'group': 'Tokyo', 'value': 7},
                {'time': 'Jan', 'group': 'London', 'value': 3.9},
                {'time': 'Feb', 'group': 'Tokyo', 'value': 6.9},
                {'time': 'Feb', 'group': 'London', 'value': 4.2},
                {'time': 'Mar', 'group': 'Tokyo', 'value': 9.5},
                {'time': 'Mar', 'group': 'London', 'value': 5.7},
                {'time': 'Apr', 'group': 'Tokyo', 'value': 14.5},
                {'time': 'Apr', 'group': 'London', 'value': 8.5},
                {'time': 'May', 'group': 'Tokyo', 'value': 18.4},
                {'time': 'May', 'group': 'London', 'value': 11.9},
                {'time': 'Jun', 'group': 'Tokyo', 'value': 21.5},
                {'time': 'Jun', 'group': 'London', 'value': 15.2},
                {'time': 'Jul', 'group': 'Tokyo', 'value': 25.2},
                {'time': 'Jul', 'group': 'London', 'value': 17},
                {'time': 'Aug', 'group': 'Tokyo', 'value': 26.5},
                {'time': 'Aug', 'group': 'London', 'value': 16.6},
                {'time': 'Sep', 'group': 'Tokyo', 'value': 23.3},
                {'time': 'Sep', 'group': 'London', 'value': 14.2},
                {'time': 'Oct', 'group': 'Tokyo', 'value': 18.3},
                {'time': 'Oct', 'group': 'London', 'value': 10.3},
                {'time': 'Nov', 'group': 'Tokyo', 'value': 13.9},
                {'time': 'Nov', 'group': 'London', 'value': 6.6},
                {'time': 'Dec', 'group': 'Tokyo', 'value': 9.6},
                {'time': 'Dec', 'group': 'London', 'value': 4.8},
            ],
            'stack': True,
            'axisXTitle': 'Month',
            'axisYTitle': 'Temperature',
            'title': 'Area Chart',
        })
        assert_image_equal(vis_bytes, 'area-grouped')

    def test_area_stacked_academy(self):
        vis_bytes = render({
            'theme': 'academy',
            'width': 600,
            'height': 400,
            'type': 'area',
            'data': [
                {'time': 'Jan', 'group': 'Tokyo', 'value': 7},
                {'time': 'Jan', 'group': 'London', 'value': 3.9},
                {'time': 'Feb', 'group': 'Tokyo', 'value': 6.9},
                {'time': 'Feb', 'group': 'London', 'value': 4.2},
                {'time': 'Mar', 'group': 'Tokyo', 'value': 9.5},
                {'time': 'Mar', 'group': 'London', 'value': 5.7},
                {'time': 'Apr', 'group': 'Tokyo', 'value': 14.5},
                {'time': 'Apr', 'group': 'London', 'value': 8.5},
                {'time': 'May', 'group': 'Tokyo', 'value': 18.4},
                {'time': 'May', 'group': 'London', 'value': 11.9},
                {'time': 'Jun', 'group': 'Tokyo', 'value': 21.5},
                {'time': 'Jun', 'group': 'London', 'value': 15.2},
                {'time': 'Jul', 'group': 'Tokyo', 'value': 25.2},
                {'time': 'Jul', 'group': 'London', 'value': 17},
                {'time': 'Aug', 'group': 'Tokyo', 'value': 26.5},
                {'time': 'Aug', 'group': 'London', 'value': 16.6},
                {'time': 'Sep', 'group': 'Tokyo', 'value': 23.3},
                {'time': 'Sep', 'group': 'London', 'value': 14.2},
                {'time': 'Oct', 'group': 'Tokyo', 'value': 18.3},
                {'time': 'Oct', 'group': 'London', 'value': 10.3},
                {'time': 'Nov', 'group': 'Tokyo', 'value': 13.9},
                {'time': 'Nov', 'group': 'London', 'value': 6.6},
                {'time': 'Dec', 'group': 'Tokyo', 'value': 9.6},
                {'time': 'Dec', 'group': 'London', 'value': 4.8},
            ],
            'stack': True,
            'axisXTitle': 'Month',
            'axisYTitle': 'Temperature',
            'title': 'Area Chart',
        })
        assert_image_equal(vis_bytes, 'area-stacked-academy')

    def test_area_grouped_academy(self):
        vis_bytes = render({
            'theme': 'academy',
            'width': 600,
            'height': 400,
            'type': 'area',
            'data': [
                {'time': 'Jan', 'group': 'Tokyo', 'value': 7},
                {'time': 'Jan', 'group': 'London', 'value': 3.9},
                {'time': 'Feb', 'group': 'Tokyo', 'value': 6.9},
                {'time': 'Feb', 'group': 'London', 'value': 4.2},
                {'time': 'Mar', 'group': 'Tokyo', 'value': 9.5},
                {'time': 'Mar', 'group': 'London', 'value': 5.7},
                {'time': 'Apr', 'group': 'Tokyo', 'value': 14.5},
                {'time': 'Apr', 'group': 'London', 'value': 8.5},
                {'time': 'May', 'group': 'Tokyo', 'value': 18.4},
                {'time': 'May', 'group': 'London', 'value': 11.9},
                {'time': 'Jun', 'group': 'Tokyo', 'value': 21.5},
                {'time': 'Jun', 'group': 'London', 'value': 15.2},
                {'time': 'Jul', 'group': 'Tokyo', 'value': 25.2},
                {'time': 'Jul', 'group': 'London', 'value': 17},
                {'time': 'Aug', 'group': 'Tokyo', 'value': 26.5},
                {'time': 'Aug', 'group': 'London', 'value': 16.6},
                {'time': 'Sep', 'group': 'Tokyo', 'value': 23.3},
                {'time': 'Sep', 'group': 'London', 'value': 14.2},
                {'time': 'Oct', 'group': 'Tokyo', 'value': 18.3},
                {'time': 'Oct', 'group': 'London', 'value': 10.3},
                {'time': 'Nov', 'group': 'Tokyo', 'value': 13.9},
                {'time': 'Nov', 'group': 'London', 'value': 6.6},
                {'time': 'Dec', 'group': 'Tokyo', 'value': 9.6},
                {'time': 'Dec', 'group': 'London', 'value': 4.8},
            ],
            'stack': True,
            'axisXTitle': 'Month',
            'axisYTitle': 'Temperature',
            'title': 'Area Chart',
        })
        assert_image_equal(vis_bytes, 'area-grouped-academy')
