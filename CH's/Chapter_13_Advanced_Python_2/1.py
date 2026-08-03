'''
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ python -m venv env1 env2
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ ls
env1  env2
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ source env1/bin/activate
(env1) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ deactivate
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ source env2/bin/activate
(env2) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ pip install pyjokes pandas
Collecting pyjokes
  Downloading pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
Collecting pandas
  Using cached pandas-2.3.3-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)
Collecting numpy>=1.26.0 (from pandas)
  Using cached numpy-2.3.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pyjokes-0.8.3-py3-none-any.whl (47 kB)
Using cached pandas-2.3.3-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.3 MB)
Using cached numpy-2.3.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyjokes, numpy, python-dateutil, pandas
Successfully installed numpy-2.3.4 pandas-2.3.3 pyjokes-0.8.3 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
(env2) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ pip freeze > req.txt
(env2) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ deactivate
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ source env1/bin/activate
(env1) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ pip install -r req.txt
Collecting numpy==2.3.4 (from -r req.txt (line 1))
  Using cached numpy-2.3.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting pandas==2.3.3 (from -r req.txt (line 2))
  Using cached pandas-2.3.3-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)
Collecting pyjokes==0.8.3 (from -r req.txt (line 3))
  Using cached pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
Collecting python-dateutil==2.9.0.post0 (from -r req.txt (line 4))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz==2025.2 (from -r req.txt (line 5))
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting six==1.17.0 (from -r req.txt (line 6))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tzdata==2025.2 (from -r req.txt (line 7))
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached numpy-2.3.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
Using cached pandas-2.3.3-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.3 MB)
Using cached pyjokes-0.8.3-py3-none-any.whl (47 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: pytz, tzdata, six, pyjokes, numpy, python-dateutil, pandas
Successfully installed numpy-2.3.4 pandas-2.3.3 pyjokes-0.8.3 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
(env1) smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$ deactivate
smilo@smilo-LOQ-15AHP9:~/Desktop/Venv$
'''