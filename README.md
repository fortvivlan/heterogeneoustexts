# heterogeneoustexts

(Mallet LDA, конечно, не мой. http://mallet.cs.umass.edu/ )

annotation - скрипт для обучения LDA-модели с заданными параметрами. Импортирует process - там содержатся варианты обработки датасета. 

topictiling - скрипт для сегментации текста на основе обученной LDA-модели (вероятно, устаревший вариант)

automatedTT - автоматизированная сегментация текста для всех обученных LDA-моделей с окном от 2 до 10 предложений (более актуальный)

morphoparsing - скрипт для обработки датасета с помощью сентенайзера razdel, кастомного токенизатора и RNNMorph (есть разбор ча текстов в парсере Анастасьева + по моей просьбе запустили разбор основного датасета на морфопарсере гикря (Анастасьев с модификациями)

morphoclass - вспомогательный файл с классом, который возвращает морфопарсер (там хранятся четыре атрибута каждого токена: форма, лемма, PoS и категория)

Скрипты статистического анализа датасетов:

  SentLengths - анализ "в лоб" по средним длинам предложений (для каждого документа в сегменте вычисляется размах вариационного ряда, медиана, межквартильное расстояние и т.п., для сегмента вычисляется среднее арифметическое этих значений)
  
  LexDiv - попытка оценить лексическое разнообразие сегментов (не очень удачная)
  
  PosDiv - процентный состав сегментов по частям речи. 
  
  tfisforiginal - немного странная идея посчитать косинусное расстояние между сегментами. Результаты лежат в табличке cosines
