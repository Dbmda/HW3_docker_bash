# Описание

Генерация K-pop групп на основе сузествующих названий, компаний владельцев, лидеров групп и количества участников в них.

Проект состоит из двух приложений:  
Generator - генерирует CSV-файл со случайными данными о K-pop группах.  
Reporter - анализирует CSV-файл и формирует HTML-отчёт.  

# Структура проекта   

├── data/   
├── generator/   
│ ├── Dockerfile   
│ └── generator.py   
├── reporter/   
│ ├── Dockerfile   
│ ├── package.json  
│ └── report.js   
├── run.sh   
└── README.md  

# Команды 

./run.sh build_generator  
./run.sh run_generator  
./run.sh create_local_data  
./run.sh build_reporter  
./run.sh run_reporter  
./run.sh structure  
./run.sh clear_data  
./run.sh inside_generator  
./run.sh inside_reporter  

# Порядок запуска  

./run.sh build_generator  
./run.sh run_generator  
./run.sh build_reporter  
./run.sh run_reporter  


# Автор

Штейнберг Алиса Евгеньевна  
ББИ2508