echo "публикация пакета на PyPI..."
uv publish
if [ $? -eq 0 ]; then
    echo "Публикация завершена успешно."
else
    echo "Ошибка при публикации пакета."
fi  
