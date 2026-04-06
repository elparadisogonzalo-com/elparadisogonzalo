from datetime import datetime, UTC
import json

build_data = {
    "build_version": "1.0.0",
    "build_time": datetime.now(UTC).isoformat(),
    "environment": "production"
}

with open("config/build.json", "w") as f:
    json.dump(build_data, f, indent=2)

print("Build metadata updated!")
