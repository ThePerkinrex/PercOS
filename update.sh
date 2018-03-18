echo "Downloading PercScript"
curl https://codeload.github.com/ThePerkinrex/PercScript/zip/master --output tmp.zip
echo "Installing Percscript"
unzip -u tmp.zip -x '*.md' '*.png' '*/LICENSE' '*/.gitignore' '*/Example.plang'
rm tmp.zip
rm -r PercScript/
mkdir PercScript
cp -R PercScript-master/* PercScript/
rm -r PercScript-master
echo "PercScript done"



echo "Pushing the updates"
echo "Adding ."
git add .
echo "Commiting as \"Get update packages\""
git commit -m "Get update packages"
echo "Pushing"
git push
