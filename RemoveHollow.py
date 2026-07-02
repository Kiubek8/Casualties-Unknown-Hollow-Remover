import json
import zlib

with open("save.sv", "rb") as f:
    data = json.loads(zlib.decompress(f.read(), wbits=47))

data["bodyComponents"] = {}

compressor = zlib.compressobj(level=9, wbits=31)
payload = json.dumps(data).encode()
result = compressor.compress(payload)
result += compressor.flush()

with open("save_EDITED.sv", "wb") as f:
    f.write(result)