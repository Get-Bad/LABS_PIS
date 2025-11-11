const groupmates = [
    {
      name: 'Александр',
      surname: 'Иванов',
      group: 'БВТ1702',
      marks: [4, 3, 5],
    },
    {
      name: 'Иван',
      surname: 'Петров',
      group: 'БСТ1702',
      marks: [3, 3, 2],
    },
    {
      name: 'Кирилл',
      surname: 'Смирнов',
      group: 'БАП1801',
      marks: [5, 5, 5],
    },
    {
      name: 'Ваня',
      surname: 'Иван',
      group: 'БВТ1702',
      marks: [1, 0, -15],
    },
  ]
  
  const rpad = function (str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString() // преобразование в строку
    while (str.length < length) {
      // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
      str = str + ' '
    }
  
    return str
  }
  
  var printStudents = function (students) {
    console.log(
      rpad('Имя', 15),
      rpad('Фамилия', 15),
      rpad('Группа', 8),
      rpad('Оценки', 20)
    )
    // был выведен заголовок таблицы
    for (let i = 0; i <= students.length - 1; i++) {
      // в цикле выводится каждый экземпляр студента
      console.log(
        rpad(students[i]['name'], 15),
        rpad(students[i]['surname'], 15),
        rpad(students[i]['group'], 8),
        rpad(students[i]['marks'], 20)
      )
    }
    console.log('\n') // добавляется пустая строка в конце вывода
  }
  printStudents(groupmates)
  
  console.log('Отфильтрованные по группе студенты')
  const group = prompt('Введите группу')
  printStudents(groupmates.filter((student) => student.group === group))
  
  console.log('Отфильтрованные по оценке студенты')
  
  const input_mark = prompt('Введите оценку')
  printStudents(
    groupmates.filter((student) => {
      const mark = student.marks.reduce(
        (accumulator, student_mark) => accumulator + student_mark,
        0
      )
      return mark / student.marks.length >= input_mark
    })
  )