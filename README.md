Горчаков Роман Владимирович. Вариант 2
# Лабораторная работа 4.4. Работа с исключениями в языке Python

Исключениями (exceptions) в языках программирования называют проблемы, возникающие в ходе выполнения программы, которые допускают возможность дальнейшей ее работы в рамках основного алгоритма. Типичным примером исключения является деление на ноль, невозможность считать данные из файла (устройства), отсутствие доступной памяти, доступ к закрытой области памяти и т.п. Для обработки таких ситуаций в языках программирования, как правило, предусматривается специальный механизм, который называется обработка исключений (exception handling).

Исключения разделяют на синхронные и асинхронные. Синхронные исключения могут возникнуть только в определенных местах программы. Например, если у вас есть код, который открывает файл и считывает из него данные, то исключение типа “ошибка чтения данных” может произойти только в указанном куске кода. Асинхронные исключения могут возникнуть в любой момент работы программы, они, как правило, связаны с какими-либо аппаратными проблемами, либо приходом данных. В качестве примера можно привести сигнал отключения питания.

В языках программирования чаще всего предусматривается специальный механизм обработки исключений. Обработка может быть с возвратом, когда после обработки исключения выполнение программы продолжается с того места, где оно возникло. И обработка без возврата, в этом случае, при возникновении исключения, осуществляется переход в специальный, заранее подготовленный, блок кода.

Различают структурную и неструктурную обработку исключений. Неструктурная обработка предполагает регистрацию функции обработчика для каждого исключения, соответственно данная функция будет вызвана при возникновении конкретного исключения. Для структурной обработки язык программирования должен поддерживать специальные синтаксические конструкции, которые позволяют выделить код, который необходимо контролировать и код, который нужно выполнить при возникновении исключительной ситуации.

В Python выделяют два различных вида ошибок: синтаксические ошибки и исключения. Синтаксические ошибки возникают в случае если программа написана с нарушениями требований Python к синтаксису. Определяются они в процессе парсинга программы. Исключения возникают в случае если синтаксически программа корректна, но в процессе выполнения возникает ошибка (деление на ноль и т.п.).

В Python исключения являются определенным типом данных, через который пользователь (программист) получает информацию об ошибке. Если в коде программы исключение не обрабатывается, то приложение останавливается и в консоли печатается подробное описание произошедшей ошибки с указанием места в программе, где она произошла и тип этой ошибки.

Обработка исключений нужна для того, чтобы приложение не завершалось аварийно каждый раз, когда возникает исключение. Для этого блок кода, в котором возможно появление исключительной ситуации необходимо поместить во внутрь синтаксической конструкции try… except. Для указания набора исключений, который должен обрабатывать данный блок except их необходимо перечислить в скобках (круглых) через запятую после оператора except.

Для выполнения определенного программного кода при выходе из блока try/except, используйте оператор finally. Не зависимо от того, возникнет или нет во время выполнения кода в блоке try исключение, код в блоке finally все равно будет выполнен. Если необходимо выполнить какой-то программный код, в случае если в процессе выполнения блока try не возникло исключений, то можно использовать оператор else.

Блоки try-except могут быть вложенными для более гибкого управления исключениями. В следующем примере демонстрируется попытка открыть текстовый файл и записать в него некую строку. Для каждой цели используется отдельный блок try. Для принудительной генерации исключения используется инструкция raise.

В Python можно создавать собственные исключения. Такая практика позволяет увеличить гибкость процесса обработки ошибок в рамках той предметной области, для которой написана ваша программа. Для реализации собственного типа исключения необходимо создать класс, являющийся наследником от одного из классов исключений.

Для вывода специальных сообщений, не влияющих на функционирование программы, в Python применяется библиотека логов. Чтобы воспользоваться ею, необходимо выполнить импорт в верхней части файла. В Python существует пять уровней логирования:

1) DEBUG - самый низкий уровень логирования, предназначенный для отладочных сообщений, для вывода диагностической информации о приложении;
2) INFO - этот уровень предназначен для вывода данных о фрагментах кода, работающих так, как ожидается;
3) WARNING - этот уровень логирования предусматривает вывод предупреждений, он применяется для записи сведений о событиях, на которые программист обычно обращает внимание. Такие события вполне могут привести к проблемам при работе приложения. По умолчанию используется именно warning;
4) ERROR - этот уровень логирования предусматривает вывод сведений об ошибках — о том, что часть приложения работает не так, как ожидается, о том, что программа не смогла правильно выполниться;
5) CRITICAL - этот уровень используется для вывода сведений об очень серьёзных ошибках, наличие которых угрожает нормальному функционированию всего приложения. Если не исправить такую ошибку — это может привести к тому, что приложение прекратит работу. 
