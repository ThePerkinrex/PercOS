if [ "`stat source/PercScript.py | grep -o x`" == "" ]; then
  chmod +x source/PercScript.py
fi

./source/PercScript.py "$@"
