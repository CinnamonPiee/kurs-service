// Инициализация псевдоэлементов
console.log('JS loaded')
;(function (a) {
	'use string'
	a.pseudoElements = { length: 0 }
	var b = function (c) {
		// Логика работы с псевдоэлементами
		if (
			'object' == typeof c.argument ||
			(c.argument !== void 0 && c.property !== void 0)
		) {
			for (var d of c.elements.get()) {
				d.pseudoElements ||
					(d.pseudoElements = {
						styleSheet: null,
						before: { index: null, properties: null },
						after: { index: null, properties: null },
						id: null,
					})
				var e = (function () {
					if (null !== d.pseudoElements.id)
						return (
							+d.getAttribute('data-pe--id') !== d.pseudoElements.id &&
								d.setAttribute('data-pe--id', d.pseudoElements.id),
							'[data-pe--id="' + d.pseudoElements.id + '"]::' + c.pseudoElement
						)
					var k = a.pseudoElements.length
					return (
						a.pseudoElements.length++,
						(d.pseudoElements.id = k),
						d.setAttribute('data-pe--id', k),
						'[data-pe--id="' + k + '"]::' + c.pseudoElement
					)
				})()
				if (!d.pseudoElements.styleSheet)
					if (document.styleSheets[0])
						d.pseudoElements.styleSheet = document.styleSheets[0]
					else {
						var f = document.createElement('style')
						document.head.appendChild(f),
							(d.pseudoElements.styleSheet = f.sheet)
					}
				if (
					(d.pseudoElements[c.pseudoElement].properties &&
						d.pseudoElements[c.pseudoElement].index &&
						d.pseudoElements.styleSheet.deleteRule(
							d.pseudoElements[c.pseudoElement].index
						),
					'object' == typeof c.argument)
				) {
					if (
						((c.argument = a.extend({}, c.argument)),
						!d.pseudoElements[c.pseudoElement].properties &&
							!d.pseudoElements[c.pseudoElement].index)
					) {
						var g =
							d.pseudoElements.styleSheet.rules.length ||
							d.pseudoElements.styleSheet.cssRules.length ||
							d.pseudoElements.styleSheet.length
						;(d.pseudoElements[c.pseudoElement].index = g),
							(d.pseudoElements[c.pseudoElement].properties = c.argument)
					}
					var h = ''
					for (var i in c.argument)
						d.pseudoElements[c.pseudoElement].properties[i] =
							'function' == typeof c.argument[i]
								? c.argument[i]()
								: c.argument[i]
					for (var i in d.pseudoElements[c.pseudoElement].properties)
						h +=
							i +
							': ' +
							d.pseudoElements[c.pseudoElement].properties[i] +
							' !important; '
					d.pseudoElements.styleSheet.addRule(
						e,
						h,
						d.pseudoElements[c.pseudoElement].index
					)
				} else if (void 0 !== c.argument && void 0 !== c.property) {
					if (
						!d.pseudoElements[c.pseudoElement].properties &&
						!d.pseudoElements[c.pseudoElement].index
					) {
						var g =
							d.pseudoElements.styleSheet.rules.length ||
							d.pseudoElements.styleSheet.cssRules.length ||
							d.pseudoElements.styleSheet.length
						;(d.pseudoElements[c.pseudoElement].index = g),
							(d.pseudoElements[c.pseudoElement].properties = {})
					}
					d.pseudoElements[c.pseudoElement].properties[c.argument] =
						'function' == typeof c.property ? c.property() : c.property
					var h = ''
					for (var i in d.pseudoElements[c.pseudoElement].properties)
						h +=
							i +
							': ' +
							d.pseudoElements[c.pseudoElement].properties[i] +
							' !important; '
					d.pseudoElements.styleSheet.addRule(
						e,
						h,
						d.pseudoElements[c.pseudoElement].index
					)
				}
			}
			return a(c.elements)
		}
		if (void 0 !== c.argument && void 0 === c.property) {
			var d = a(c.elements).get(0),
				j = window
					.getComputedStyle(d, '::' + c.pseudoElement)
					.getPropertyValue(c.argument)
			return d.pseudoElements
				? a(c.elements).get(0).pseudoElements[c.pseudoElement].properties[
						c.argument
				  ] || j
				: j || null
		}
		return console.error('Invalid values!'), !1
	}
	;(a.fn.cssBefore = function (c, d) {
		return b({
			elements: this,
			pseudoElement: 'before',
			argument: c,
			property: d,
		})
	}),
		(a.fn.cssAfter = function (c, d) {
			return b({
				elements: this,
				pseudoElement: 'after',
				argument: c,
				property: d,
			})
		})
})(jQuery)

// Универсальная функция для AJAX-запросов
const loadAjax = function (setting) {
	return $.ajax(setting)
}

// Функция для загрузки содержимого корзины
const loadCart = function (container) {
	$(container).load('/check-list/index')
}

// Функция для обновления количества элементов в корзине
function getCountCheckList() {
	$.get('/check-list/count', function (response) {
		$('#check-list').html(response.count)
		$('#check-list-big').html(response.count)
	})
}

// Инициализация количества элементов в корзине
getCountCheckList()

// Функция для отображения уведомлений
function funcSuccessNoty(data) {
	if (data.code === 200) {
		new Noty({
			text: data.html,
			layout: 'center',
			type: 'success',
			theme: 'bootstrap-v4',
			timeout: 5000,
		}).show()
	} else if (data.code === 400) {
		new Noty({
			text: data.html,
			layout: 'center',
			type: 'error',
			theme: 'bootstrap-v4',
			timeout: 5000,
		}).show()
	}
}

// Функция для установки заголовка модального окна
function getTitleModal(title) {
	$('.modal-title').html(title)
}

// Универсальная функция для отображения модального окна
function showModal(modalId, data) {
	$(`#${modalId} .modal-body`).html(data)
	$(`#${modalId}`).modal('show')
}

// Универсальный обработчик для модальных окон
function setupModalHandler(buttonClass, url, modalId) {
	$(document).on('click', buttonClass, function (e) {
		e.preventDefault()
		const id = $(this).data('id')
		const title = $(this).data('title')
		loadAjax({
			url,
			type: 'POST',
			data: { id, title },
			success: function (data) {
				if (data) {
					getTitleModal(title)
					showModal(modalId, data)
				}
			},
			error: function (xhr, status, error) {
				console.error('Ошибка:', error)
			},
		})
	})
}

// Настройка обработчиков для различных модальных окон
setupModalHandler(
	'.add-to-order-service',
	'/order-service/add-modal',
	'addToOrderServices'
)
setupModalHandler(
	'.add-to-order-evacuation',
	'/evacuation/add-modal',
	'addToOrderEvacuation'
)
setupModalHandler(
	'.add-to-sale',
	'/order-discount/add-modal',
	'addToOrderDiscount'
)
setupModalHandler(
	'.add-to-special-price',
	'/order-special-price/add-modal',
	'addToOrderSpecialPrice'
)
setupModalHandler(
	'.add-to-price',
	'/order-price-maintenance/add-modal',
	'addToOrderPriceMaintenance'
)
setupModalHandler(
	'.add-to-price-tire-fitting',
	'/order-price-tire-fitting/add-modal',
	'addToOrderPriceTireFitting'
)
setupModalHandler(
	'.add-to-price-shod-razval',
	'/order-price-shod-razval/add-modal',
	'addToOrderPriceShodRazval'
)
setupModalHandler(
	'.add-to-order-power',
	'/order-power-equipment/add-modal',
	'addToOrderPower'
)

// Обработчики для работы с корзиной
$(document).on('click', '.cart_quantity_up', function (e) {
	e.preventDefault()
	const id = $(this).data('services')
	loadAjax({
		url: '/check-list/increment',
		type: 'POST',
		data: { id },
		success: function () {
			loadCart('#content-check-list')
		},
	})
})

$(document).on('click', '.cart_quantity_down', function (e) {
	e.preventDefault()
	const id = $(this).data('services')
	loadAjax({
		url: '/check-list/decrement',
		type: 'POST',
		data: { id },
		success: function () {
			loadCart('#content-check-list')
		},
	})
})

$(document).on('click', '.del-item', function () {
	const id = $(this).data('services')
	loadAjax({
		url: '/check-list/del-item',
		type: 'POST',
		data: { id },
		success: function () {
			loadCart('#content-check-list')
			getCountCheckList()
		},
	})
})

$(document).on('click', '.add-to-check-list', function (e) {
	e.preventDefault()
	const id = $(this).data('services')
	const name = $(this).data('name') || ''
	const img_url = $(this).data('img') || ''
	loadAjax({
		url: '/check-list/add/',
		type: 'POST',
		data: { id, name, img_url },
		success: function (response) {
			if (response.code === 200) {
				getCountCheckList()
			}
		},
	})
})

// Обработчики для динамической загрузки данных
$(document).ready(function () {
	$('#form-order-check-list-car_mark').on('change', function () {
		const targetValue = $(this).val()
		loadAjax({
			url: '/online-appointment/get-car-models/',
			type: 'GET',
			data: { id: targetValue },
			success: function (data) {
				$('#form-order-check-list-car_model')
					.html(data)
					.removeAttr('disabled')
					.css('background', '')
				$('#form-order-check-list-car_modification')
					.html('<option value="">Сначала выберите модель</option>')
					.attr('disabled', 'disabled')
					.css('background', '#eee')
			},
		})
	})

	$('#form-order-check-list-car_model').on('change', function () {
		const targetValue = $(this).val()
		loadAjax({
			url: '/online-appointment/get-car-modifications/',
			type: 'GET',
			data: { id: targetValue },
			success: function (data) {
				$('#form-order-check-list-car_modification')
					.html(data)
					.removeAttr('disabled')
					.css('background', '')
			},
		})
	})
})
