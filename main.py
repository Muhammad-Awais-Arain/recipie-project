# main.py
from fastapi import FastAPI, HTTPException
import subprocess, re, os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

class URLPayload(BaseModel):
    url: str

# # Mount the "static" folder as a root directory for static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Define the default route to serve the index.html file
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",  {"request":request})

# Define the mapping between test types and script files
test_type_to_script = {
    "test-event": "Pytest_Scripts/Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_event.py",
    "test-legislative": "Pytest_Scripts/Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_Legislative.py",
    "test-memberdiscount": "Pytest_Scripts/Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_MemberDiscount.py",
    "test-multiplenews": "Pytest_Scripts/Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_MultipleNews.py"
}


@app.post("/run-test/{test_type}", response_model=dict)
def run_test(test_type: str, payload: URLPayload):
    url = payload.url
    os.environ["URL"] = url
    test_script = ""

    # Check if the provided test_type is valid
    test_script = test_type_to_script.get(test_type)
    if test_script is None:
        return JSONResponse(content={"result": "Invalid test type."}, status_code=400)

    try:
        result = subprocess.run(
            ["pytest", test_script],
            env=os.environ,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            test_result = re.search(r"test_addevent returned '(.+?)'", result.stdout)
            if test_result:
                return JSONResponse(content={"result": test_result.group(1)})
            else:
                return JSONResponse(content={"result": "Test result not found."})
        else:
            return JSONResponse(content={"result": f"Test execution failed:\n{result.stderr}"})
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="pytest executable not found. Make sure pytest is installed and available in the system's PATH.")


# Define the route to run the Cypress test
@app.get("/run-cypress-test")
def run_cypress_test():
    try:
        # Use the 'cypress run' command to execute the Cypress test
        result = subprocess.run(["cypress", "run", "--spec", "cypress/e2e/Add_Navigations_and_Data/Album.cy.js"], capture_output=True, text=True)
        return f"Cypress test execution output:\n{result.stdout}"
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Cypress executable not found. Make sure Cypress is installed and available in the system's PATH.")

@app.post("/v4")
def mainscript():
    result = subprocess.run(["python", "Pytest_Scripts/Stress_Testing_Scripts/V4_APIs/main_script.py"], capture_output=True, text=True)
    return result
