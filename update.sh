echo "Downloading PercScript"
curl https://codeload.github.com/ThePerkinrex/PercScript/zip/master --output tmp.zip
echo "Installing Percscript"
unzip -u tmp.zip
rm tmp.zip
mv PercScript-master/ PercScript/
echo "PercScript done"
