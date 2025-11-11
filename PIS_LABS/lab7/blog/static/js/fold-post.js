// Проверяем, что DOM полностью загружен
document.addEventListener('DOMContentLoaded', function () {
  // Получаем все кнопки с классом 'fold-button'
  var foldBtns = document.getElementsByClassName('fold-button')

  // Перебираем все кнопки и добавляем им обработчик события клика
  for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener('click', function (e) {
      // Находим предыдущий элемент (это и есть блок .one-post)
      var postElement = e.target.parentElement.previousElementSibling
      // Проверяем, есть ли у родительского элемента класс 'folded'
      if (postElement.classList.contains('folded')) {
        // Если есть, значит пост свернут. Разворачиваем его.
        e.target.innerHTML = 'свернуть' // Меняем текст кнопки
        postElement.classList.remove('folded') // Убираем класс 'folded' у .one-post
      } else {
        // Если нет, значит пост развернут. Сворачиваем его.
        e.target.innerHTML = 'развернуть' // Меняем текст кнопки
        postElement.classList.add('folded') // Добавляем класс 'folded' к .one-post
      }
    })
  }
})
