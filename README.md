# Receipt Processor
Tried to make a clean solution with a blend of simplicity and structure. Happy Reviewing!

I would recommend creating a Python virtual environment and installing the requirements to have a good IDE experience.

#### Techstack:
- FastAPI: Lightweight Python-based backend framework.
- Pydantic: Data validation library that makes Python typed.
- Pytest: Test library
- Black: VSCode Python formatter.
  
## Running Instruction
- Have Docker running in your system.
- Build and test
    - In the directory of the `Dockerfile`, run: `docker build -t fastapi-receipt-processor .`
    - This will build the service image as well as run a minimal test suite.
- Run the service
    - Run: `docker run -p 80:80 fastapi-receipt-processor`
    - The service will be running in port 80 of localhost.
    - Head over to `localhost:80/docs` to use the out-of-box swagger documentation page of FastAPI.
