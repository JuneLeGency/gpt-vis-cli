import pytest
import os
from gpt_vis.api import render

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
    def test_bar(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'bar',
            'data': [
                {'category': 'Sports', 'value': 275},
                {'category': 'Strategy', 'value': 115},
                {'category': 'Action', 'value': 120},
                {'category': 'Shooter', 'value': 350},
                {'category': 'Other', 'value': 150},
            ],
            'axisXTitle': 'Type',
            'axisYTitle': 'Sold',
        })
        assert_image_equal(vis_bytes, 'bar')

    def test_bar_required(self):
        vis_bytes = render({
            'type': 'bar',
            'data': [
                {'category': 'Sports', 'value': 275},
                {'category': 'Strategy', 'value': 115},
                {'category': 'Action', 'value': 120},
                {'category': 'Shooter', 'value': 350},
                {'category': 'Other', 'value': 150},
            ],
        })
        assert_image_equal(vis_bytes, 'bar-required')

    def test_bar_rough(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'bar',
            'texture': 'rough',
            'data': [
                {'category': 'Sports', 'value': 275},
                {'category': 'Strategy', 'value': 115},
                {'category': 'Action', 'value': 120},
                {'category': 'Shooter', 'value': 350},
                {'category': 'Other', 'value': 150},
            ],
            'axisXTitle': 'Type',
            'axisYTitle': 'Sold',
        })
        assert_image_equal(vis_bytes, 'bar-rough')

    def test_bar_academy(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'bar',
            'theme': 'academy',
            'data': [
                {'category': 'Sports', 'value': 275},
                {'category': 'Strategy', 'value': 115},
                {'category': 'Action', 'value': 120},
                {'category': 'Shooter', 'value': 350},
                {'category': 'Other', 'value': 150},
            ],
            'axisXTitle': 'Type',
            'axisYTitle': 'Sold',
        })
        assert_image_equal(vis_bytes, 'bar-academy')

    def test_bar_grouped(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'bar',
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'group': True,
            'stack': False,
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Grouped)',
        })
        assert_image_equal(vis_bytes, 'bar-grouped')

    def test_bar_stacked(self):
        vis_bytes = render({
            'width': 600,
            'height': 400,
            'type': 'bar',
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'bar-stacked')

    def test_bar_stacked_academy(self):
        vis_bytes = render({
            'theme': 'academy',
            'width': 600,
            'height': 400,
            'type': 'bar',
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'bar-stacked-academy')

    def test_column(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'width': 600,
            'height': 400,
            'type': 'column',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'column')

    def test_column_required(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'type': 'column',
        })
        assert_image_equal(vis_bytes, 'column-required')

    def test_column_rough(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'width': 600,
            'height': 400,
            'type': 'column',
            'texture': 'rough',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'column-rough')

    def test_column_academy(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'width': 600,
            'height': 400,
            'type': 'column',
            'theme': 'academy',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'column-academy')

    def test_column_grouped(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': False,
            'group': True,
            'width': 600,
            'height': 400,
            'type': 'column',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Grouped)',
        })
        assert_image_equal(vis_bytes, 'column-grouped')

    def test_column_stacked(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'width': 600,
            'height': 400,
            'type': 'column',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'column-stacked')

    def test_column_stacked_academy(self):
        vis_bytes = render({
            'data': [
                {'category': 'Jan', 'group': 'Email', 'value': 62},
                {'category': 'Jan', 'group': 'Affiliate', 'value': 38},
                {'category': 'Feb', 'group': 'Email', 'value': 45},
                {'category': 'Feb', 'group': 'Affiliate', 'value': 28},
                {'category': 'Mar', 'group': 'Email', 'value': 78},
                {'category': 'Mar', 'group': 'Affiliate', 'value': 48},
                {'category': 'Apr', 'group': 'Email', 'value': 68},
                {'category': 'Apr', 'group': 'Affiliate', 'value': 38},
                {'category': 'May', 'group': 'Email', 'value': 48},
                {'category': 'May', 'group': 'Affiliate', 'value': 28},
                {'category': 'Jun', 'group': 'Email', 'value': 38},
                {'category': 'Jun', 'group': 'Affiliate', 'value': 18},
            ],
            'stack': True,
            'group': False,
            'width': 600,
            'height': 400,
            'type': 'column',
            'theme': 'academy',
            'axisXTitle': 'Month',
            'axisYTitle': 'Value',
            'title': 'Monthly Sales Data (Stacked)',
        })
        assert_image_equal(vis_bytes, 'column-stacked-academy')

    def test_dual_axes(self):
        vis_bytes = render({
            'categories': ['2015', '2016', '2017', '2018', '2019'],
            'series': [
                {'type': 'column', 'data': [91.9, 99.1, 101.6, 114.4, 121], 'axisYTitle': 'Sales'},
                {'type': 'line', 'data': [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': 'Profit Margin'},
            ],
            'width': 600,
            'height': 400,
            'type': 'dual-axes',
            'title': 'Sales and Profit Margin Over Years',
            'axisXTitle': 'Year',
        })
        assert_image_equal(vis_bytes, 'dual-axes')

    def test_dual_axes_required(self):
        vis_bytes = render({
            'categories': ['2015', '2016', '2017', '2018', '2019'],
            'series': [
                {'type': 'column', 'data': [91.9, 99.1, 101.6, 114.4, 121]},
                {'type': 'line', 'data': [0.055, 0.06, 0.062, 0.07, 0.075]},
            ],
            'type': 'dual-axes',
        })
        assert_image_equal(vis_bytes, 'dual-axes-required')

    def test_dual_axes_rough(self):
        vis_bytes = render({
            'categories': ['2015', '2016', '2017', '2018', '2019'],
            'series': [
                {'type': 'column', 'data': [91.9, 99.1, 101.6, 114.4, 121], 'axisYTitle': 'Sales'},
                {'type': 'line', 'data': [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': 'Profit Margin'},
            ],
            'width': 600,
            'height': 400,
            'type': 'dual-axes',
            'texture': 'rough',
            'title': 'Sales and Profit Margin Over Years',
            'axisXTitle': 'Year',
        })
        assert_image_equal(vis_bytes, 'dual-axes-rough')

    def test_dual_axes_academy(self):
        vis_bytes = render({
            'categories': ['2015', '2016', '2017', '2018', '2019'],
            'series': [
                {'type': 'column', 'data': [91.9, 99.1, 101.6, 114.4, 121], 'axisYTitle': 'Sales'},
                {'type': 'line', 'data': [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': 'Profit Margin'},
            ],
            'width': 600,
            'height': 400,
            'type': 'dual-axes',
            'theme': 'academy',
            'title': 'Sales and Profit Margin Over Years',
            'axisXTitle': 'Year',
        })
        assert_image_equal(vis_bytes, 'dual-axes-academy')

    def test_fishbone_diagram(self):
        vis_bytes = render({
            'data': {
                'name': 'Quality Issues',
                'children': [
                    {'name': 'Man', 'children': [{'name': 'Lack of Training'}, {'name': 'Fatigue'}]},
                    {'name': 'Machine', 'children': [{'name': 'Aging Equipment'}, {'name': 'Improper Setup'}]},
                    {'name': 'Material', 'children': [{'name': 'Substandard Raw Materials'}, {'name': 'Incorrect Specifications'}]},
                    {'name': 'Method', 'children': [{'name': 'Inconsistent Processes'}, {'name': 'Lack of Clear Instructions'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'fishbone-diagram',
        })
        assert_image_equal(vis_bytes, 'fishbone-diagram')

    def test_fishbone_diagram_required(self):
        vis_bytes = render({
            'data': {
                'name': 'Quality Issues',
                'children': [
                    {'name': 'Man', 'children': [{'name': 'Lack of Training'}, {'name': 'Fatigue'}]},
                    {'name': 'Machine', 'children': [{'name': 'Aging Equipment'}, {'name': 'Improper Setup'}]},
                    {'name': 'Material', 'children': [{'name': 'Substandard Raw Materials'}, {'name': 'Incorrect Specifications'}]},
                    {'name': 'Method', 'children': [{'name': 'Inconsistent Processes'}, {'name': 'Lack of Clear Instructions'}]},
                ],
            },
            'type': 'fishbone-diagram',
        })
        assert_image_equal(vis_bytes, 'fishbone-diagram-required')

    def test_fishbone_diagram_rough(self):
        vis_bytes = render({
            'data': {
                'name': 'Quality Issues',
                'children': [
                    {'name': 'Man', 'children': [{'name': 'Lack of Training'}, {'name': 'Fatigue'}]},
                    {'name': 'Machine', 'children': [{'name': 'Aging Equipment'}, {'name': 'Improper Setup'}]},
                    {'name': 'Material', 'children': [{'name': 'Substandard Raw Materials'}, {'name': 'Incorrect Specifications'}]},
                    {'name': 'Method', 'children': [{'name': 'Inconsistent Processes'}, {'name': 'Lack of Clear Instructions'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'fishbone-diagram',
            'texture': 'rough',
        })
        assert_image_equal(vis_bytes, 'fishbone-diagram-rough')

    def test_fishbone_diagram_academy(self):
        vis_bytes = render({
            'data': {
                'name': 'Quality Issues',
                'children': [
                    {'name': 'Man', 'children': [{'name': 'Lack of Training'}, {'name': 'Fatigue'}]},
                    {'name': 'Machine', 'children': [{'name': 'Aging Equipment'}, {'name': 'Improper Setup'}]},
                    {'name': 'Material', 'children': [{'name': 'Substandard Raw Materials'}, {'name': 'Incorrect Specifications'}]},
                    {'name': 'Method', 'children': [{'name': 'Inconsistent Processes'}, {'name': 'Lack of Clear Instructions'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'fishbone-diagram',
            'theme': 'academy',
        })
        assert_image_equal(vis_bytes, 'fishbone-diagram-academy')

    def test_flow_diagram(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'Start'}, {'name': 'Process 1'}, {'name': 'Process 2'}, {'name': 'End'}],
                'edges': [
                    {'source': 'Start', 'target': 'Process 1', 'name': 'to p1'},
                    {'source': 'Process 1', 'target': 'Process 2', 'name': 'to p2'},
                    {'source': 'Process 2', 'target': 'End', 'name': 'to end'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'flow-diagram',
        })
        assert_image_equal(vis_bytes, 'flow-diagram')

    def test_flow_diagram_required(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'Start'}, {'name': 'Process 1'}, {'name': 'Process 2'}, {'name': 'End'}],
                'edges': [
                    {'source': 'Start', 'target': 'Process 1', 'name': 'to p1'},
                    {'source': 'Process 1', 'target': 'Process 2', 'name': 'to p2'},
                    {'source': 'Process 2', 'target': 'End', 'name': 'to end'},
                ],
            },
            'type': 'flow-diagram',
        })
        assert_image_equal(vis_bytes, 'flow-diagram-required')

    def test_flow_diagram_rough(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'Start'}, {'name': 'Process 1'}, {'name': 'Process 2'}, {'name': 'End'}],
                'edges': [
                    {'source': 'Start', 'target': 'Process 1', 'name': 'to p1'},
                    {'source': 'Process 1', 'target': 'Process 2', 'name': 'to p2'},
                    {'source': 'Process 2', 'target': 'End', 'name': 'to end'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'flow-diagram',
            'texture': 'rough',
        })
        assert_image_equal(vis_bytes, 'flow-diagram-rough')

    def test_flow_diagram_academy(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'Start'}, {'name': 'Process 1'}, {'name': 'Process 2'}, {'name': 'End'}],
                'edges': [
                    {'source': 'Start', 'target': 'Process 1', 'name': 'to p1'},
                    {'source': 'Process 1', 'target': 'Process 2', 'name': 'to p2'},
                    {'source': 'Process 2', 'target': 'End', 'name': 'to end'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'flow-diagram',
            'theme': 'academy',
        })
        assert_image_equal(vis_bytes, 'flow-diagram-academy')

    def test_funnel(self):
        vis_bytes = render({
            'data': [
                {'category': 'Website Visits', 'value': 50000},
                {'category': 'Added to Cart', 'value': 35000},
                {'category': 'Placed Order', 'value': 25000},
                {'category': 'Paid', 'value': 15000},
                {'category': 'Completed Transaction', 'value': 8000},
            ],
            'width': 600,
            'height': 400,
            'type': 'funnel',
            'title': 'Sales Funnel',
        })
        assert_image_equal(vis_bytes, 'funnel')

    def test_funnel_required(self):
        vis_bytes = render({
            'data': [
                {'category': 'Website Visits', 'value': 50000},
                {'category': 'Added to Cart', 'value': 35000},
                {'category': 'Placed Order', 'value': 25000},
                {'category': 'Paid', 'value': 15000},
                {'category': 'Completed Transaction', 'value': 8000},
            ],
            'type': 'funnel',
        })
        assert_image_equal(vis_bytes, 'funnel-required')

    def test_funnel_rough(self):
        vis_bytes = render({
            'data': [
                {'category': 'Website Visits', 'value': 50000},
                {'category': 'Added to Cart', 'value': 35000},
                {'category': 'Placed Order', 'value': 25000},
                {'category': 'Paid', 'value': 15000},
                {'category': 'Completed Transaction', 'value': 8000},
            ],
            'width': 600,
            'height': 400,
            'type': 'funnel',
            'texture': 'rough',
            'title': 'Sales Funnel',
        })
        assert_image_equal(vis_bytes, 'funnel-rough')

    def test_funnel_academy(self):
        vis_bytes = render({
            'data': [
                {'category': 'Website Visits', 'value': 50000},
                {'category': 'Added to Cart', 'value': 35000},
                {'category': 'Placed Order', 'value': 25000},
                {'category': 'Paid', 'value': 15000},
                {'category': 'Completed Transaction', 'value': 8000},
            ],
            'width': 600,
            'height': 400,
            'type': 'funnel',
            'theme': 'academy',
            'title': 'Sales Funnel',
        })
        assert_image_equal(vis_bytes, 'funnel-academy')

    def test_histogram(self):
        vis_bytes = render({
            'data': [78, 88, 60, 100, 95, 85, 75, 65, 90, 80, 70, 60, 100],
            'binNumber': 5,
            'width': 600,
            'height': 400,
            'type': 'histogram',
            'title': 'Distribution of Scores',
            'axisXTitle': 'Score',
            'axisYTitle': 'Frequency',
        })
        assert_image_equal(vis_bytes, 'histogram')

    def test_histogram_required(self):
        vis_bytes = render({
            'data': [78, 88, 60, 100, 95, 85, 75, 65, 90, 80, 70, 60, 100],
            'type': 'histogram',
        })
        assert_image_equal(vis_bytes, 'histogram-required')

    def test_histogram_rough(self):
        vis_bytes = render({
            'data': [78, 88, 60, 100, 95, 85, 75, 65, 90, 80, 70, 60, 100],
            'binNumber': 5,
            'width': 600,
            'height': 400,
            'type': 'histogram',
            'texture': 'rough',
            'title': 'Distribution of Scores',
            'axisXTitle': 'Score',
            'axisYTitle': 'Frequency',
        })
        assert_image_equal(vis_bytes, 'histogram-rough')

    def test_histogram_academy(self):
        vis_bytes = render({
            'data': [78, 88, 60, 100, 95, 85, 75, 65, 90, 80, 70, 60, 100],
            'binNumber': 5,
            'width': 600,
            'height': 400,
            'type': 'histogram',
            'theme': 'academy',
            'title': 'Distribution of Scores',
            'axisXTitle': 'Score',
            'axisYTitle': 'Frequency',
        })
        assert_image_equal(vis_bytes, 'histogram-academy')

    def test_line(self):
        vis_bytes = render({
            'data': [
                {'time': '2015', 'value': 23},
                {'time': '2016', 'value': 35},
                {'time': '2017', 'value': 45},
                {'time': '2018', 'value': 58},
                {'time': '2019', 'value': 72},
            ],
            'width': 600,
            'height': 400,
            'type': 'line',
            'title': 'Growth Over Years',
            'axisXTitle': 'Year',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'line')

    def test_line_required(self):
        vis_bytes = render({
            'data': [
                {'time': '2015', 'value': 23},
                {'time': '2016', 'value': 35},
                {'time': '2017', 'value': 45},
                {'time': '2018', 'value': 58},
                {'time': '2019', 'value': 72},
            ],
            'type': 'line',
        })
        assert_image_equal(vis_bytes, 'line-required')

    def test_line_rough(self):
        vis_bytes = render({
            'data': [
                {'time': '2015', 'value': 23},
                {'time': '2016', 'value': 35},
                {'time': '2017', 'value': 45},
                {'time': '2018', 'value': 58},
                {'time': '2019', 'value': 72},
            ],
            'width': 600,
            'height': 400,
            'type': 'line',
            'texture': 'rough',
            'title': 'Growth Over Years',
            'axisXTitle': 'Year',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'line-rough')

    def test_line_academy(self):
        vis_bytes = render({
            'data': [
                {'time': '2015', 'value': 23},
                {'time': '2016', 'value': 35},
                {'time': '2017', 'value': 45},
                {'time': '2018', 'value': 58},
                {'time': '2019', 'value': 72},
            ],
            'width': 600,
            'height': 400,
            'type': 'line',
            'theme': 'academy',
            'title': 'Growth Over Years',
            'axisXTitle': 'Year',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'line-academy')

    def test_liquid(self):
        vis_bytes = render({
            'percent': 0.75,
            'shape': 'circle',
            'width': 400,
            'height': 400,
            'type': 'liquid',
            'title': 'Progress Completion',
        })
        assert_image_equal(vis_bytes, 'liquid')

    def test_liquid_required(self):
        vis_bytes = render({
            'percent': 0.75,
            'type': 'liquid',
        })
        assert_image_equal(vis_bytes, 'liquid-required')

    def test_liquid_rough(self):
        vis_bytes = render({
            'percent': 0.75,
            'shape': 'circle',
            'width': 400,
            'height': 400,
            'type': 'liquid',
            'texture': 'rough',
            'title': 'Progress Completion',
        })
        assert_image_equal(vis_bytes, 'liquid-rough')

    def test_liquid_academy(self):
        vis_bytes = render({
            'percent': 0.75,
            'shape': 'circle',
            'width': 400,
            'height': 400,
            'type': 'liquid',
            'theme': 'academy',
            'title': 'Progress Completion',
        })
        assert_image_equal(vis_bytes, 'liquid-academy')

    def test_mind_map(self):
        vis_bytes = render({
            'data': {
                'name': 'Central Topic',
                'children': [
                    {'name': 'Main Topic 1'},
                    {'name': 'Main Topic 2'},
                    {'name': 'Main Topic 3'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'mind-map',
        })
        assert_image_equal(vis_bytes, 'mind-map')

    def test_mind_map_required(self):
        vis_bytes = render({
            'data': {
                'name': 'Central Topic',
                'children': [
                    {'name': 'Main Topic 1'},
                    {'name': 'Main Topic 2'},
                    {'name': 'Main Topic 3'},
                ],
            },
            'type': 'mind-map',
        })
        assert_image_equal(vis_bytes, 'mind-map-required')

    def test_mind_map_rough(self):
        vis_bytes = render({
            'data': {
                'name': 'Central Topic',
                'children': [
                    {'name': 'Main Topic 1'},
                    {'name': 'Main Topic 2'},
                    {'name': 'Main Topic 3'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'mind-map',
            'texture': 'rough',
        })
        assert_image_equal(vis_bytes, 'mind-map-rough')

    def test_mind_map_academy(self):
        vis_bytes = render({
            'data': {
                'name': 'Central Topic',
                'children': [
                    {'name': 'Main Topic 1'},
                    {'name': 'Main Topic 2'},
                    {'name': 'Main Topic 3'},
                ],
            },
            'width': 600,
            'height': 400,
            'type': 'mind-map',
            'theme': 'academy',
        })
        assert_image_equal(vis_bytes, 'mind-map-academy')

    def test_network_graph(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}],
                'edges': [{'source': 'A', 'target': 'B'}, {'source': 'A', 'target': 'C'}, {'source': 'B', 'target': 'D'}],
            },
            'width': 600,
            'height': 400,
            'type': 'network-graph',
        })
        assert_image_equal(vis_bytes, 'network-graph')

    def test_network_graph_required(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}],
                'edges': [{'source': 'A', 'target': 'B'}, {'source': 'A', 'target': 'C'}, {'source': 'B', 'target': 'D'}],
            },
            'type': 'network-graph',
        })
        assert_image_equal(vis_bytes, 'network-graph-required')

    def test_network_graph_rough(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}],
                'edges': [{'source': 'A', 'target': 'B'}, {'source': 'A', 'target': 'C'}, {'source': 'B', 'target': 'D'}],
            },
            'width': 600,
            'height': 400,
            'type': 'network-graph',
            'texture': 'rough',
        })
        assert_image_equal(vis_bytes, 'network-graph-rough')

    def test_network_graph_academy(self):
        vis_bytes = render({
            'data': {
                'nodes': [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}],
                'edges': [{'source': 'A', 'target': 'B'}, {'source': 'A', 'target': 'C'}, {'source': 'B', 'target': 'D'}],
            },
            'width': 600,
            'height': 400,
            'type': 'network-graph',
            'theme': 'academy',
        })
        assert_image_equal(vis_bytes, 'network-graph-academy')

    def test_organization_chart(self):
        vis_bytes = render({
            'data': {
                'name': 'CEO',
                'children': [
                    {'name': 'VP of Engineering', 'children': [{'name': 'Team Lead 1'}, {'name': 'Team Lead 2'}]},
                    {'name': 'VP of Sales', 'children': [{'name': 'Sales Manager 1'}, {'name': 'Sales Manager 2'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'organization-chart',
        })
        assert_image_equal(vis_bytes, 'organization-chart')

    def test_organization_chart_required(self):
        vis_bytes = render({
            'data': {
                'name': 'CEO',
                'children': [
                    {'name': 'VP of Engineering', 'children': [{'name': 'Team Lead 1'}, {'name': 'Team Lead 2'}]},
                    {'name': 'VP of Sales', 'children': [{'name': 'Sales Manager 1'}, {'name': 'Sales Manager 2'}]},
                ],
            },
            'type': 'organization-chart',
        })
        assert_image_equal(vis_bytes, 'organization-chart-required')

    def test_organization_chart_rough(self):
        vis_bytes = render({
            'data': {
                'name': 'CEO',
                'children': [
                    {'name': 'VP of Engineering', 'children': [{'name': 'Team Lead 1'}, {'name': 'Team Lead 2'}]},
                    {'name': 'VP of Sales', 'children': [{'name': 'Sales Manager 1'}, {'name': 'Sales Manager 2'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'organization-chart',
            'texture': 'rough',
        })
        assert_image_equal(vis_bytes, 'organization-chart-rough')

    def test_organization_chart_academy(self):
        vis_bytes = render({
            'data': {
                'name': 'CEO',
                'children': [
                    {'name': 'VP of Engineering', 'children': [{'name': 'Team Lead 1'}, {'name': 'Team Lead 2'}]},
                    {'name': 'VP of Sales', 'children': [{'name': 'Sales Manager 1'}, {'name': 'Sales Manager 2'}]},
                ],
            },
            'width': 800,
            'height': 600,
            'type': 'organization-chart',
            'theme': 'academy',
        })
        assert_image_equal(vis_bytes, 'organization-chart-academy')

    def test_pie(self):
        vis_bytes = render({
            'data': [
                {'category': 'Category A', 'value': 27},
                {'category': 'Category B', 'value': 25},
                {'category': 'Category C', 'value': 18},
                {'category': 'Category D', 'value': 15},
                {'category': 'Category E', 'value': 10},
                {'category': 'Other', 'value': 5},
            ],
            'innerRadius': 0.6,
            'width': 600,
            'height': 400,
            'type': 'pie',
            'title': 'Donut Chart',
        })
        assert_image_equal(vis_bytes, 'pie')

    def test_pie_required(self):
        vis_bytes = render({
            'data': [
                {'category': 'Category A', 'value': 27},
                {'category': 'Category B', 'value': 25},
                {'category': 'Category C', 'value': 18},
                {'category': 'Category D', 'value': 15},
                {'category': 'Category E', 'value': 10},
                {'category': 'Other', 'value': 5},
            ],
            'type': 'pie',
        })
        assert_image_equal(vis_bytes, 'pie-required')

    def test_pie_rough(self):
        vis_bytes = render({
            'data': [
                {'category': 'Category A', 'value': 27},
                {'category': 'Category B', 'value': 25},
                {'category': 'Category C', 'value': 18},
                {'category': 'Category D', 'value': 15},
                {'category': 'Category E', 'value': 10},
                {'category': 'Other', 'value': 5},
            ],
            'innerRadius': 0.6,
            'width': 600,
            'height': 400,
            'type': 'pie',
            'texture': 'rough',
            'title': 'Donut Chart',
        })
        assert_image_equal(vis_bytes, 'pie-rough')

    def test_pie_academy(self):
        vis_bytes = render({
            'data': [
                {'category': 'Category A', 'value': 27},
                {'category': 'Category B', 'value': 25},
                {'category': 'Category C', 'value': 18},
                {'category': 'Category D', 'value': 15},
                {'category': 'Category E', 'value': 10},
                {'category': 'Other', 'value': 5},
            ],
            'innerRadius': 0.6,
            'width': 600,
            'height': 400,
            'type': 'pie',
            'theme': 'academy',
            'title': 'Donut Chart',
        })
        assert_image_equal(vis_bytes, 'pie-academy')

    def test_radar(self):
        vis_bytes = render({
            'data': [
                {'name': 'Sales', 'value': 70},
                {'name': 'Marketing', 'value': 60},
                {'name': 'Development', 'value': 80},
                {'name': 'Support', 'value': 40},
                {'name': 'Administration', 'value': 50},
            ],
            'width': 600,
            'height': 400,
            'type': 'radar',
            'title': 'Performance Metrics',
        })
        assert_image_equal(vis_bytes, 'radar')

    def test_radar_required(self):
        vis_bytes = render({
            'data': [
                {'name': 'Sales', 'value': 70},
                {'name': 'Marketing', 'value': 60},
                {'name': 'Development', 'value': 80},
                {'name': 'Support', 'value': 40},
                {'name': 'Administration', 'value': 50},
            ],
            'type': 'radar',
        })
        assert_image_equal(vis_bytes, 'radar-required')

    def test_radar_rough(self):
        vis_bytes = render({
            'data': [
                {'name': 'Sales', 'value': 70},
                {'name': 'Marketing', 'value': 60},
                {'name': 'Development', 'value': 80},
                {'name': 'Support', 'value': 40},
                {'name': 'Administration', 'value': 50},
            ],
            'width': 600,
            'height': 400,
            'type': 'radar',
            'texture': 'rough',
            'title': 'Performance Metrics',
        })
        assert_image_equal(vis_bytes, 'radar-rough')

    def test_radar_academy(self):
        vis_bytes = render({
            'data': [
                {'name': 'Sales', 'value': 70},
                {'name': 'Marketing', 'value': 60},
                {'name': 'Development', 'value': 80},
                {'name': 'Support', 'value': 40},
                {'name': 'Administration', 'value': 50},
            ],
            'width': 600,
            'height': 400,
            'type': 'radar',
            'theme': 'academy',
            'title': 'Performance Metrics',
        })
        assert_image_equal(vis_bytes, 'radar-academy')

    def test_sankey(self):
        vis_bytes = render({
            'data': [
                {'source': 'Landing Page', 'target': 'Product Page', 'value': 50000},
                {'source': 'Product Page', 'target': 'Add to Cart', 'value': 35000},
                {'source': 'Add to Cart', 'target': 'Checkout', 'value': 25000},
                {'source': 'Checkout', 'target': 'Payment', 'value': 15000},
                {'source': 'Payment', 'target': 'Purchase Completed', 'value': 8000},
            ],
            'width': 800,
            'height': 600,
            'type': 'sankey',
            'title': 'User Flow',
        })
        assert_image_equal(vis_bytes, 'sankey')

    def test_sankey_required(self):
        vis_bytes = render({
            'data': [
                {'source': 'Landing Page', 'target': 'Product Page', 'value': 50000},
                {'source': 'Product Page', 'target': 'Add to Cart', 'value': 35000},
                {'source': 'Add to Cart', 'target': 'Checkout', 'value': 25000},
                {'source': 'Checkout', 'target': 'Payment', 'value': 15000},
                {'source': 'Payment', 'target': 'Purchase Completed', 'value': 8000},
            ],
            'type': 'sankey',
        })
        assert_image_equal(vis_bytes, 'sankey-required')

    def test_sankey_rough(self):
        vis_bytes = render({
            'data': [
                {'source': 'Landing Page', 'target': 'Product Page', 'value': 50000},
                {'source': 'Product Page', 'target': 'Add to Cart', 'value': 35000},
                {'source': 'Add to Cart', 'target': 'Checkout', 'value': 25000},
                {'source': 'Checkout', 'target': 'Payment', 'value': 15000},
                {'source': 'Payment', 'target': 'Purchase Completed', 'value': 8000},
            ],
            'width': 800,
            'height': 600,
            'type': 'sankey',
            'texture': 'rough',
            'title': 'User Flow',
        })
        assert_image_equal(vis_bytes, 'sankey-rough')

    def test_sankey_academy(self):
        vis_bytes = render({
            'data': [
                {'source': 'Landing Page', 'target': 'Product Page', 'value': 50000},
                {'source': 'Product Page', 'target': 'Add to Cart', 'value': 35000},
                {'source': 'Add to Cart', 'target': 'Checkout', 'value': 25000},
                {'source': 'Checkout', 'target': 'Payment', 'value': 15000},
                {'source': 'Payment', 'target': 'Purchase Completed', 'value': 8000},
            ],
            'width': 800,
            'height': 600,
            'type': 'sankey',
            'theme': 'academy',
            'title': 'User Flow',
        })
        assert_image_equal(vis_bytes, 'sankey-academy')

    def test_scatter(self):
        vis_bytes = render({
            'data': [
                {'x': 10, 'y': 15},
                {'x': 20, 'y': 25},
                {'x': 30, 'y': 35},
                {'x': 40, 'y': 45},
                {'x': 50, 'y': 55},
            ],
            'width': 600,
            'height': 400,
            'type': 'scatter',
            'title': 'Scatter Plot',
            'axisXTitle': 'X Value',
            'axisYTitle': 'Y Value',
        })
        assert_image_equal(vis_bytes, 'scatter')

    def test_scatter_required(self):
        vis_bytes = render({
            'data': [
                {'x': 10, 'y': 15},
                {'x': 20, 'y': 25},
                {'x': 30, 'y': 35},
                {'x': 40, 'y': 45},
                {'x': 50, 'y': 55},
            ],
            'type': 'scatter',
        })
        assert_image_equal(vis_bytes, 'scatter-required')

    def test_scatter_rough(self):
        vis_bytes = render({
            'data': [
                {'x': 10, 'y': 15},
                {'x': 20, 'y': 25},
                {'x': 30, 'y': 35},
                {'x': 40, 'y': 45},
                {'x': 50, 'y': 55},
            ],
            'width': 600,
            'height': 400,
            'type': 'scatter',
            'texture': 'rough',
            'title': 'Scatter Plot',
            'axisXTitle': 'X Value',
            'axisYTitle': 'Y Value',
        })
        assert_image_equal(vis_bytes, 'scatter-rough')

    def test_scatter_academy(self):
        vis_bytes = render({
            'data': [
                {'x': 10, 'y': 15},
                {'x': 20, 'y': 25},
                {'x': 30, 'y': 35},
                {'x': 40, 'y': 45},
                {'x': 50, 'y': 55},
            ],
            'width': 600,
            'height': 400,
            'type': 'scatter',
            'theme': 'academy',
            'title': 'Scatter Plot',
            'axisXTitle': 'X Value',
            'axisYTitle': 'Y Value',
        })
        assert_image_equal(vis_bytes, 'scatter-academy')

    def test_treemap(self):
        vis_bytes = render({
            'data': [
                {'name': 'Root', 'value': 100, 'children': [{'name': 'Category A', 'value': 50}, {'name': 'Category B', 'value': 30}, {'name': 'Category C', 'value': 20}]},
            ],
            'width': 600,
            'height': 400,
            'type': 'treemap',
            'title': 'Treemap',
        })
        assert_image_equal(vis_bytes, 'treemap')

    def test_treemap_required(self):
        vis_bytes = render({
            'data': [
                {'name': 'Root', 'value': 100, 'children': [{'name': 'Category A', 'value': 50}, {'name': 'Category B', 'value': 30}, {'name': 'Category C', 'value': 20}]},
            ],
            'type': 'treemap',
        })
        assert_image_equal(vis_bytes, 'treemap-required')

    def test_treemap_rough(self):
        vis_bytes = render({
            'data': [
                {'name': 'Root', 'value': 100, 'children': [{'name': 'Category A', 'value': 50}, {'name': 'Category B', 'value': 30}, {'name': 'Category C', 'value': 20}]},
            ],
            'width': 600,
            'height': 400,
            'type': 'treemap',
            'texture': 'rough',
            'title': 'Treemap',
        })
        assert_image_equal(vis_bytes, 'treemap-rough')

    def test_treemap_academy(self):
        vis_bytes = render({
            'data': [
                {'name': 'Root', 'value': 100, 'children': [{'name': 'Category A', 'value': 50}, {'name': 'Category B', 'value': 30}, {'name': 'Category C', 'value': 20}]},
            ],
            'width': 600,
            'height': 400,
            'type': 'treemap',
            'theme': 'academy',
            'title': 'Treemap',
        })
        assert_image_equal(vis_bytes, 'treemap-academy')

    def test_venn(self):
        vis_bytes = render({
            'data': [
                {'label': 'A', 'value': 10, 'sets': ['A']},
                {'label': 'B', 'value': 20, 'sets': ['B']},
                {'label': 'C', 'value': 30, 'sets': ['C']},
                {'label': 'AB', 'value': 5, 'sets': ['A', 'B']},
            ],
            'width': 600,
            'height': 400,
            'type': 'venn',
            'title': 'Venn Diagram',
        })
        assert_image_equal(vis_bytes, 'venn')

    def test_venn_required(self):
        vis_bytes = render({
            'data': [
                {'label': 'A', 'value': 10, 'sets': ['A']},
                {'label': 'B', 'value': 20, 'sets': ['B']},
                {'label': 'C', 'value': 30, 'sets': ['C']},
                {'label': 'AB', 'value': 5, 'sets': ['A', 'B']},
            ],
            'type': 'venn',
        })
        assert_image_equal(vis_bytes, 'venn-required')

    def test_venn_rough(self):
        vis_bytes = render({
            'data': [
                {'label': 'A', 'value': 10, 'sets': ['A']},
                {'label': 'B', 'value': 20, 'sets': ['B']},
                {'label': 'C', 'value': 30, 'sets': ['C']},
                {'label': 'AB', 'value': 5, 'sets': ['A', 'B']},
            ],
            'width': 600,
            'height': 400,
            'type': 'venn',
            'texture': 'rough',
            'title': 'Venn Diagram',
        })
        assert_image_equal(vis_bytes, 'venn-rough')

    def test_venn_academy(self):
        vis_bytes = render({
            'data': [
                {'label': 'A', 'value': 10, 'sets': ['A']},
                {'label': 'B', 'value': 20, 'sets': ['B']},
                {'label': 'C', 'value': 30, 'sets': ['C']},
                {'label': 'AB', 'value': 5, 'sets': ['A', 'B']},
            ],
            'width': 600,
            'height': 400,
            'type': 'venn',
            'theme': 'academy',
            'title': 'Venn Diagram',
        })
        assert_image_equal(vis_bytes, 'venn-academy')

    def test_violin(self):
        vis_bytes = render({
            'data': [
                {'category': 'Group A', 'value': 10},
                {'category': 'Group A', 'value': 20},
                {'category': 'Group A', 'value': 30},
                {'category': 'Group B', 'value': 25},
                {'category': 'Group B', 'value': 35},
                {'category': 'Group B', 'value': 45},
            ],
            'width': 600,
            'height': 400,
            'type': 'violin',
            'title': 'Violin Plot',
            'axisXTitle': 'Group',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'violin')

    def test_violin_required(self):
        vis_bytes = render({
            'data': [
                {'category': 'Group A', 'value': 10},
                {'category': 'Group A', 'value': 20},
                {'category': 'Group A', 'value': 30},
                {'category': 'Group B', 'value': 25},
                {'category': 'Group B', 'value': 35},
                {'category': 'Group B', 'value': 45},
            ],
            'type': 'violin',
        })
        assert_image_equal(vis_bytes, 'violin-required')

    def test_violin_rough(self):
        vis_bytes = render({
            'data': [
                {'category': 'Group A', 'value': 10},
                {'category': 'Group A', 'value': 20},
                {'category': 'Group A', 'value': 30},
                {'category': 'Group B', 'value': 25},
                {'category': 'Group B', 'value': 35},
                {'category': 'Group B', 'value': 45},
            ],
            'width': 600,
            'height': 400,
            'type': 'violin',
            'texture': 'rough',
            'title': 'Violin Plot',
            'axisXTitle': 'Group',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'violin-rough')

    def test_violin_academy(self):
        vis_bytes = render({
            'data': [
                {'category': 'Group A', 'value': 10},
                {'category': 'Group A', 'value': 20},
                {'category': 'Group A', 'value': 30},
                {'category': 'Group B', 'value': 25},
                {'category': 'Group B', 'value': 35},
                {'category': 'Group B', 'value': 45},
            ],
            'width': 600,
            'height': 400,
            'type': 'violin',
            'theme': 'academy',
            'title': 'Violin Plot',
            'axisXTitle': 'Group',
            'axisYTitle': 'Value',
        })
        assert_image_equal(vis_bytes, 'violin-academy')

    def test_word_cloud(self):
        vis_bytes = render({
            'data': [
                {'value': 4.272, 'text': 'G2Plot'},
                {'value': 3.5, 'text': 'AntV'},
                {'value': 2.5, 'text': 'F2'},
                {'value': 2.2, 'text': 'Chart'},
                {'value': 2.0, 'text': 'Graphics'},
                {'value': 1.8, 'text': 'Plot'},
                {'value': 1.5, 'text': 'Visualization'},
            ],
            'width': 600,
            'height': 400,
            'type': 'word-cloud',
            'title': 'Word Cloud',
        })
        assert_image_equal(vis_bytes, 'word-cloud')

    def test_word_cloud_required(self):
        vis_bytes = render({
            'data': [
                {'value': 4.272, 'text': 'G2Plot'},
                {'value': 3.5, 'text': 'AntV'},
                {'value': 2.5, 'text': 'F2'},
                {'value': 2.2, 'text': 'Chart'},
                {'value': 2.0, 'text': 'Graphics'},
                {'value': 1.8, 'text': 'Plot'},
                {'value': 1.5, 'text': 'Visualization'},
            ],
            'type': 'word-cloud',
        })
        assert_image_equal(vis_bytes, 'word-cloud-required')

    def test_word_cloud_rough(self):
        vis_bytes = render({
            'data': [
                {'value': 4.272, 'text': 'G2Plot'},
                {'value': 3.5, 'text': 'AntV'},
                {'value': 2.5, 'text': 'F2'},
                {'value': 2.2, 'text': 'Chart'},
                {'value': 2.0, 'text': 'Graphics'},
                {'value': 1.8, 'text': 'Plot'},
                {'value': 1.5, 'text': 'Visualization'},
            ],
            'width': 600,
            'height': 400,
            'type': 'word-cloud',
            'texture': 'rough',
            'title': 'Word Cloud',
        })
        assert_image_equal(vis_bytes, 'word-cloud-rough')

    def test_word_cloud_academy(self):
        vis_bytes = render({
            'data': [
                {'value': 4.272, 'text': 'G2Plot'},
                {'value': 3.5, 'text': 'AntV'},
                {'value': 2.5, 'text': 'F2'},
                {'value': 2.2, 'text': 'Chart'},
                {'value': 2.0, 'text': 'Graphics'},
                {'value': 1.8, 'text': 'Plot'},
                {'value': 1.5, 'text': 'Visualization'},
            ],
            'width': 600,
            'height': 400,
            'type': 'word-cloud',
            'theme': 'academy',
            'title': 'Word Cloud',
        })
        assert_image_equal(vis_bytes, 'word-cloud-academy')
