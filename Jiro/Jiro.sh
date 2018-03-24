SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
if [ "`stat $SCRIPTPATH/source/Jiro.py | grep -o x`" == "" ]; then
  chmod +x $SCRIPTPATH/source/Jiro.py
fi

$SCRIPTPATH/source/Jiro.py "$@"
