import importlib
import os
import sys

TEST_DATA = {
    'nitrogen': '90',
    'phosphorus': '42',
    'potassium': '43',
    'temperature': '20.8',
    'humidity': '82.0',
    'ph': '6.5',
    'rainfall': '202.9',
}


def import_app_with_env(env=None):
    """Import the `app` module applying temporary env vars (import-time uses these)."""
    old = {}
    if env:
        for k, v in env.items():
            old[k] = os.environ.get(k)
            os.environ[k] = v

    # Ensure fresh import
    if 'app' in sys.modules:
        del sys.modules['app']

    mod = importlib.import_module('app')

    # Restore environment variables (module has already read them)
    if env:
        for k, v in old.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v

    return mod


def test_model_loaded():
    mod = import_app_with_env()
    assert hasattr(mod, 'model')
    assert mod.model is not None, "Expected model to be loaded for tests"


def test_predict_endpoint_with_model():
    mod = import_app_with_env()
    client = mod.app.test_client()
    resp = client.post('/predict', data=TEST_DATA)
    assert resp.status_code == 200
    data = resp.data.lower()
    assert b'recommended crop' in data or b'<span>' in data
    assert b'rice' in data, "Expected 'rice' in prediction output"


def test_predict_endpoint_model_unavailable():
    mod = import_app_with_env({'MODEL_PATH': 'nonexistent_model_12345.pkl'})
    assert getattr(mod, 'model', None) is None
    client = mod.app.test_client()
    resp = client.post('/predict', data=TEST_DATA)
    assert resp.status_code == 200
    assert b'model not available' in resp.data.lower()


def test_predict_invalid_input():
    mod = import_app_with_env()
    client = mod.app.test_client()
    bad = TEST_DATA.copy()
    bad['nitrogen'] = 'not-a-number'
    resp = client.post('/predict', data=bad)
    assert resp.status_code == 200
    assert b'invalid input values' in resp.data.lower()