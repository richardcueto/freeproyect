# Mi Notas

## Virtualenv 
`siempre es bueno crear un entornovirtual`

```
virtualenv env
.\env\Scripts\activate
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

## PyQt5
```
pip show PyQt5
qt5-tools.exe designer 
pip install pyqt5 pyqt5-tools

# compilar archivos
pyuic6 input.ui -o output.py
pyrcc6 input.qrc -o logo_rc.py

pyinstaller --onefile tu_script.py
```
