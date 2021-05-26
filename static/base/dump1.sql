-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 25 2021 г., 23:38
-- Версия сервера: 10.4.18-MariaDB
-- Версия PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `dump_project`
--

-- --------------------------------------------------------

--
-- Структура таблицы `charitable_foundation`
--

CREATE TABLE `charitable_foundation` (
  `ID_Charitable_Found` int(11) NOT NULL,
  `Adress` text NOT NULL,
  `Name_CF` text NOT NULL,
  `Email_CF` text DEFAULT NULL,
  `Telephone_CF` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `charitable_foundation`
--

INSERT INTO `charitable_foundation` (`ID_Charitable_Found`, `Adress`, `Name_CF`, `Email_CF`, `Telephone_CF`) VALUES
(1, 'TestAdress', 'TestName', 'TestEmail', 'TestPhone');

-- --------------------------------------------------------

--
-- Структура таблицы `cleaning`
--

CREATE TABLE `cleaning` (
  `ID_Dump` int(11) NOT NULL,
  `ID_Charitable_Found` int(11) NOT NULL,
  `Progress` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `cleaning`
--

INSERT INTO `cleaning` (`ID_Dump`, `ID_Charitable_Found`, `Progress`) VALUES
(1, 1, 'Started'),
(2, 1, 'Finished');

-- --------------------------------------------------------

--
-- Структура таблицы `dump`
--

CREATE TABLE `dump` (
  `ID_Dump` int(11) NOT NULL,
  `Coordinate` varchar(50) NOT NULL,
  `Operting_Mode` varchar(50) NOT NULL,
  `Responsible_Org` varchar(255) DEFAULT NULL,
  `Telephone` varchar(20) NOT NULL,
  `Legality` int(1) NOT NULL,
  `Area` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `dump`
--

INSERT INTO `dump` (`ID_Dump`, `Coordinate`, `Operting_Mode`, `Responsible_Org`, `Telephone`, `Legality`, `Area`) VALUES
(1, '56.207537, 37.413779', 'Круглосуточно', 'ГУП «Экотехпром»', '8-499-238-49-34', 1, 150000),
(2, '55.935828, 43.089714', 'Пн-Сб:8:00-16:00', 'МУП «Истринский полигон ТБО»', '8-495-994-42-92', 1, 146500);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `charitable_foundation`
--
ALTER TABLE `charitable_foundation`
  ADD PRIMARY KEY (`ID_Charitable_Found`);

--
-- Индексы таблицы `dump`
--
ALTER TABLE `dump`
  ADD PRIMARY KEY (`ID_Dump`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `charitable_foundation`
--
ALTER TABLE `charitable_foundation`
  MODIFY `ID_Charitable_Found` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `dump`
--
ALTER TABLE `dump`
  MODIFY `ID_Dump` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
