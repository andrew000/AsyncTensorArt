# AsyncTensorArt

#### Asynchronous wrapper for the TensorArt API

---

`async_tensorart` is a Python package for asynchronous access to
the [TensorArt](https://tensor.art/) API.

## Installation

```bash
pip install async-tensorart
```

---

## Usage

```python
import asyncio
from pathlib import Path

from aiohttp import ClientSession

from async_tensorart import TensorArt
from async_tensorart.signature import PrivateKey


async def main():
    # Create a TensorArt client
    tensor = TensorArt(
        app_id="APP_ID",
        endpoint="ENDPOINT",
        session=ClientSession(),
        private_key=PrivateKey(path=Path("private_key.pem")),
    )

    # Get model info
    model_info = await tensor.get_model(model_id=42)
    print(model_info)


asyncio.run(main())
```

---

## License

This project is licensed under the terms of the MIT license.
