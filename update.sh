echo "Downloading Jiro"
curl https://codeload.github.com/ThePerkinrex/Jiro/zip/master --output tmp.zip
echo "Installing Jiro"
unzip -u tmp.zip -x '*.md' '*.png' '*/LICENSE' '*/.gitignore' '*/[Ee]xample.jr'
rm tmp.zip
rm -r Jiro/
mkdir Jiro
cp -R Jiro-master/* Jiro/
rm -r Jiro-master
echo "Jiro done"



echo "Pushing the updates"
echo "Adding ."
git add .
echo "$@"
if [ "$1" != "" ]; then
  echo "Commiting as \"$@\""
  git commit -m "$1"
else
  echo "Commiting as \"Get update packages\""
  git commit -m "Get update packages"
fi
echo "Pushing"
git push
