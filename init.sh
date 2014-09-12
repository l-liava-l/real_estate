echo "Разворачиваем'с"

echo "Создаем новый проект cordova"
cordova create _public com.nedviga.eng nedviga 

echo "Добавляем android и ios"
cd ./_public 
cordova platform add android 
cordova platform add ios

echo "подключаем зависимости"
cd ../mobile_app
npm install && bower install
rm -R ../_public/www
brunch build


echo "Создаем симлинк для jaded-brunch" 
cd ../_public/www
ln -s scripts templates

echo "Готово!"
