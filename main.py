import uvicorn
import settings
from time import time

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="localhost",
                port=settings.port, reload=True)
