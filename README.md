## Тестовое задание Domconnect


<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/vPwqFFf/71191b852-domconnect-ru.png" alt="71191b852-domconnect-ru" border="0"></a>
</p>

<p align="left">
   <img src="https://img.shields.io/badge/selenium-4.9.1-blueviolet" alt="selenium" >
   <img src="https://img.shields.io/badge/webdriver-3.8.6-blue" alt="webdriver">
   <img src="https://img.shields.io/badge/PyAudio-0.2.13-orange" alt="PyAudio">
</p>

## Description

Ваша задача - не используя API сайта написать парсер остатков времени жизни прокси в ЛК магазина. 

1 Открыть страницу https://proxy6.net/
Нажать на кнопку “Войти”, ввести логин и пароль, войти в ЛК
* Пункт с  reCAPTCHA можно пропустить  (установить паузу и ввести картинки самостоятельно пользователю) или нажмите на галочку и капча пропустит без картинок. 

<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/jWwQWt4/S4qrFaGW.jpg" alt="S4qrFaGW" border="0"></a>
</p>

2 Вы вошли в ЛК. Со страницы “Прокси” (https://proxy6.net/user/proxy) получить таблицу прокси и дату окончания

<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/RhxKwKp/g6IryAKf.jpg" alt="g6IryAKf" border="0"></a>
</p>

4 Вывести в консоль результат. Результатом будут 2 строки:

217.29.53.108:12593 - 25.05.23, 15:57
217.29.53.108:12592 - 25.05.23, 15:56


Требования:
Используйте библиотеку Selenium для взаимодействия с браузером.
Используйте любой веб-драйвер на ваш выбор (например, ChromeDriver или GeckoDriver).
Код должен быть написан на языке Python.
Допускается вмешательство пользователя для ввода капчи.

Результат:

<pre>
<span class="key">217.29.53.108:12593 - 25.05.23, 15:57</span>
<span class="key">217.29.53.108:12592 - 25.05.23, 15:56</span>
</pre>


<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/rkybMjt/images-1.jpg" alt="images-1" border="0"></a>  
</p>
<pre>
<span class="key">"Творчество в работе - это средство самовыражения и проявления своей уникальности."</span>

</pre>

## Result
1 При вводе капчи было риализованно диалоговое окно которое дает
возможность неспеша ввести капчу и нажать "ок" для продолжения или "Отмена" для завершения работы скрипта

<p align="left">
     <a href="https://ibb.co/J7Djfmd"><img src="https://i.ibb.co/vP047VB/IbU28TIl.jpg" alt="IbU28TIl" border="0"></a>
</p>


2 Добавлено музыкальное сопровождение которое работает параллельно в отдельном потоке для хорошего настроения😀

<p align="left">
     <a href="https://ibb.co/cbjLJf2"><img src="https://i.ibb.co/cbjLJf2/pngwing-com.png" alt="pngwing-com" border="0"></a>
</p>

#Вывод в консоль:

<pre>
<span class="key">217.29.53.108:12593 - 25.05.23, 15:57</span>
<span class="key">217.29.53.108:12592 - 25.05.23, 15:56</span>
</pre>
