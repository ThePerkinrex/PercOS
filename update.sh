echo "Downloading Jiro"
curl https://codeload.github.com/ThePerkinrex/Jiro/zip/master --output tmp.zip
echo "Installing Jiro"
unzip -u tmp.zip -x '*.md' '*.png' '*/LICENSE' '*/.gitignore' '*/Example.jr'
rm tmp.zip
rm -r Jiro/
mkdir Jiro
cp -R Jiro-master/* Jiro/
rm -r Jiro-master
echo "Jiro done"



echo "Pushing the updates"
echo "Adding ."
git add .
echo "Commiting as \"Get update packages\""
git commit -m "Get update packages"
echo "Pushing"
git push
