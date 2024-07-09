```sh
sudo apt update
sudo apt install python3-venv

cd projects
python3 -m venv myenv

source myenv/bin/activate
pip install fastapi uvicorn
W

uvicorn main:app --reload --host 0.0.0.0 --port 8000  # run uvicorn

```