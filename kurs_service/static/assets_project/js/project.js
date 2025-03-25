(function (a) {
    'use string';
    a.pseudoElements = {length: 0};
    var b = function (c) {
        if ('object' == typeof c.argument || c.argument !== void 0 && c.property !== void 0) {
            for (var d of c.elements.get()) {
                d.pseudoElements || (d.pseudoElements = {
                    styleSheet: null,
                    before: {index: null, properties: null},
                    after: {index: null, properties: null},
                    id: null
                });
                var e = function () {
                    if (null !== d.pseudoElements.id) return +d.getAttribute('data-pe--id') !== d.pseudoElements.id && d.setAttribute('data-pe--id', d.pseudoElements.id), '[data-pe--id="' + d.pseudoElements.id + '"]::' + c.pseudoElement;
                    var k = a.pseudoElements.length;
                    return a.pseudoElements.length++, d.pseudoElements.id = k, d.setAttribute('data-pe--id', k), '[data-pe--id="' + k + '"]::' + c.pseudoElement
                }();
                if (!d.pseudoElements.styleSheet) if (document.styleSheets[0]) d.pseudoElements.styleSheet = document.styleSheets[0]; else {
                    var f = document.createElement('style');
                    document.head.appendChild(f), d.pseudoElements.styleSheet = f.sheet
                }
                if (d.pseudoElements[c.pseudoElement].properties && d.pseudoElements[c.pseudoElement].index && d.pseudoElements.styleSheet.deleteRule(d.pseudoElements[c.pseudoElement].index), 'object' == typeof c.argument) {
                    if (c.argument = a.extend({}, c.argument), !d.pseudoElements[c.pseudoElement].properties && !d.pseudoElements[c.pseudoElement].index) {
                        var g = d.pseudoElements.styleSheet.rules.length || d.pseudoElements.styleSheet.cssRules.length || d.pseudoElements.styleSheet.length;
                        d.pseudoElements[c.pseudoElement].index = g, d.pseudoElements[c.pseudoElement].properties = c.argument
                    }
                    var h = '';
                    for (var i in c.argument) d.pseudoElements[c.pseudoElement].properties[i] = 'function' == typeof c.argument[i] ? c.argument[i]() : c.argument[i];
                    for (var i in d.pseudoElements[c.pseudoElement].properties) h += i + ': ' + d.pseudoElements[c.pseudoElement].properties[i] + ' !important; ';
                    d.pseudoElements.styleSheet.addRule(e, h, d.pseudoElements[c.pseudoElement].index)
                } else if (void 0 !== c.argument && void 0 !== c.property) {
                    if (!d.pseudoElements[c.pseudoElement].properties && !d.pseudoElements[c.pseudoElement].index) {
                        var g = d.pseudoElements.styleSheet.rules.length || d.pseudoElements.styleSheet.cssRules.length || d.pseudoElements.styleSheet.length;
                        d.pseudoElements[c.pseudoElement].index = g, d.pseudoElements[c.pseudoElement].properties = {}
                    }
                    d.pseudoElements[c.pseudoElement].properties[c.argument] = 'function' == typeof c.property ? c.property() : c.property;
                    var h = '';
                    for (var i in d.pseudoElements[c.pseudoElement].properties) h += i + ': ' + d.pseudoElements[c.pseudoElement].properties[i] + ' !important; ';
                    d.pseudoElements.styleSheet.addRule(e, h, d.pseudoElements[c.pseudoElement].index)
                }
            }
            return a(c.elements)
        }
        if (void 0 !== c.argument && void 0 === c.property) {
            var d = a(c.elements).get(0),
                j = window.getComputedStyle(d, '::' + c.pseudoElement).getPropertyValue(c.argument);
            return d.pseudoElements ? a(c.elements).get(0).pseudoElements[c.pseudoElement].properties[c.argument] || j : j || null
        }
        return console.error('Invalid values!'), !1
    };
    a.fn.cssBefore = function (c, d) {
        return b({elements: this, pseudoElement: 'before', argument: c, property: d})
    }, a.fn.cssAfter = function (c, d) {
        return b({elements: this, pseudoElement: 'after', argument: c, property: d})
    }
})(jQuery);



const loadAjax = function (setting) {
    return $.ajax(setting);
}

const loadCart = function (container) {
    $(container).load('/check-list/index');
}

/* CheckList */
function getCountChecList() {
    if (!$.get('/check-list/count', function (r) {
        $('#check-list').html(r.count);
        $('#check-list-big').html(r.count);

    })) {
        $('#check-list').html(r.count);
        $('#check-list-big').html(r.count);
    }
}

getCountChecList();

//nityfication plagin
function funcSuccessNoty(data) {
    if (typeof data.code !== "undefined" && data.code === 200) {
        var noty = new Noty({
            text: data.html,
            layout: 'center',
            textAlign: 'center',
            type: 'success',
            theme: 'bootstrap-v4',
            speed: 500,
            timeout: 5000,
            closable: false,
            closeOnSelfClick: false,
        }).show();
        return;
    } else if (typeof data.code !== "undefined" && data.code === 400) {
        var noty = new Noty({
            text: data.html,
            layout: 'center',
            type: 'error',
            theme: 'bootstrap-v4',
            speed: 500,
            timeout: 5000,
            closable: true,
            closeOnSelfClick: true,
        }).show();
        return;
    }
}

function getTitleModal(title) {
    $('#addToOrderServices .modal-title').html(title);
    $('#addToOrderEvacuation .modal-title').html(title);
    $('#addToOrderDiscount .modal-title').html(title);
    $('#addToOrderSpecialPrice .modal-title').html(title);
    $('#addToOrderPriceMaintenance .modal-title').html(title);
    $('#addToOrderPower .modal-title').html(title);
}

// Service
function showModalService(data) {
    $('#addToOrderServices .modal-body').html(data);
    $('#addToOrderServices').modal('show');
}

$(document).on('click', '.add-to-order-service', function (e) {
    e.preventDefault();
    var id = $(this).data('services');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-service/add-modal',
        async: true,
        data: {id: id, title: title},
        type: 'POST',
        success: function (services) {
            if (services) {
                getTitleModal(title);
                showModalService(services);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('click', '.add-to-call-back', function (e) {
    e.preventDefault();
    var id = $(this).data('services');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-call-back/add-modal-call-back',
        async: true,
        data: {id: id, title: title},
        type: 'POST',
        success: function (services) {
            if (services) {
                getTitleModal(title);
                showModalService(services);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

// Evacuation
function showModalEvacuation(data) {
    $('#addToOrderEvacuation .modal-body').html(data);
    $('#addToOrderEvacuation').modal('show');
}

$(document).on('click', '.add-to-order-evacuation', function (e) {
    e.preventDefault();
    var id = $(this).data('evacuation');
    var title = $(this).data('title');
    loadAjax({
        url: '/evacuation/add-modal',
        async: true,
        data: {id: id, title: title},
        type: 'POST',
        success: function (evacuation) {
            if (evacuation) {
                getTitleModal(title);
                showModalEvacuation(evacuation);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#form-services-modal', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-service/add-services",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

$(document).on('submit', '#order-call-back-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-call-back/add-order-call-back",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

$(document).on('submit', '#order-call-back-short-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-call-back/add-order-call-back-short",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

$(document).on('submit', '.online-appointment-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/online-appointment/add-services",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

$(document).on('submit', '.order-insurance-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/insurance/add-insurance",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

$(document).on('submit', '#order-evacuation-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/evacuation/add-evacuation",
        type: "POST",
        async: true,
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});

/* order sale-discount */
function showModalDiscount(data) {
    $('#addToOrderDiscount .modal-body').html(data);
    $('#addToOrderDiscount').modal('show');
}

$(document).on('click', '.add-to-sale', function (e) {
    e.preventDefault();
    var id = $(this).data('sale');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-discount/add-modal',
        async: true,
        data: {id: id, title: title},
        type: 'POST',
        success: function (sale) {
            if (sale) {
                getTitleModal(title);
                showModalDiscount(sale);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#form-sale-discounts', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-discount/add-sale-discounts",
        async: true,
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        beforeSend: function () {

        },
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order sale-discount end */

/* order special price */
function showModalSpecPrice(data) {
    $('#addToOrderSpecialPrice .modal-body').html(data);
    $('#addToOrderSpecialPrice').modal('show');
}

$(document).on('click', '.add-to-special-price', function (e) {
    e.preventDefault();
    var id = $(this).data('sale');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-special-price/add-modal',
        data: {id: id, title: title},
        async: true,
        type: "POST",
        success: function (sale) {
            if (sale) {
                getTitleModal(title);
                showModalSpecPrice(sale);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#form-special-price', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-special-price/add-order-special-price",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        beforeSend: function () {

        },
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order special price end */

/* order price maintanance  */
function showModalPriceMaintenance(data) {
    $('#addToOrderPriceMaintenance .modal-body').html(data);
    $('#addToOrderPriceMaintenance').modal('show');
}

$(document).on('click', '.add-to-price', function (e) {
    e.preventDefault();
    var id = $(this).data('price');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-price-maintenance/add-modal',
        data: {id: id, title: title},
        async: true,
        type: "POST",
        success: function (price) {
            if (price) {
                getTitleModal(title);
                showModalPriceMaintenance(price);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#order-price-maintenance-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-price-maintenance/add-order",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        beforeSend: function () {

        },
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order price maintanance end */

/* order price tire fitting */
function showModalPriceTireFitting(data) {
    $('#addToOrderPriceTireFitting .modal-body').html(data);
    $('#addToOrderPriceTireFitting').modal('show');
}

$(document).on('click', '.add-to-price-tire-fitting', function (e) {
    e.preventDefault();
    var id = $(this).data('price');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-price-tire-fitting/add-modal',
        data: {id: id, title: title},
        async: true,
        type: "POST",
        success: function (price) {
            if (price) {
                getTitleModal(title);
                showModalPriceMaintenance(price);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#order-price-tire-fitting-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-price-tire-fitting/add-order",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order price tire fitting end */

/* order price shod-razval */
function showModalPriceShodRazval(data) {
    $('#addToOrderPriceShodRazval .modal-body').html(data);
    $('#addToOrderPriceShodRazval').modal('show');
}

$(document).on('click', '.add-to-price-shod-razval', function (e) {
    e.preventDefault();
    var id = $(this).data('price');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-price-shod-razval/add-modal',
        data: {id: id, title: title},
        async: true,
        type: "POST",
        success: function (price) {
            if (price) {
                getTitleModal(title);
                showModalPriceMaintenance(price);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#order-price-shod-razval-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-price-shod-razval/add-order",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order price shod-razval end */
function showModalCheckList(data) {
    $('#addToCheckList .modal-body').html(data);
    $('#addToCheckList').modal('show');
}


$(document).on('click', '.add-to-check-list', function (e) {
    e.preventDefault();
    var id = $(this).data('services');
    loadAjax({
        url: '/check-list/add',
        data: {id: id},
        type: 'POST',
        success: function (services) {
            if (services) {
                getCountChecList();
                showModalCheckList(services);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('click', '.cart_quantity_up', function (e) {
    e.preventDefault();
    var id = $(this).data('services');
    loadAjax({
        url: '/check-list/increment',
        data: {id: id},
        async: true,
        type: 'POST',
        success: function () {
            loadCart('#content-check-list');
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
})

$(document).on('click', '.cart_quantity_down', function (e) {
    e.preventDefault();
    var id = $(this).data('services');
    loadAjax({
        url: '/check-list/decrement',
        async: true,
        data: {id: id},
        type: 'POST',
        success: function () {
            loadCart('#content-check-list');
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('click', '.del-item', function () {
    var id = $(this).data('services');
    loadAjax({
        url: '/check-list/del-item',
        data: {id: id},
        type: 'POST',
        success: function () {
            loadCart('#content-check-list');
            getCountChecList();
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#form-order-check-list', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-check-list/add-order",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* CheckList end */

/* load input car, model, modification */
function loadInput(data, selector) {
    $(selector).html(data)
    $(selector).removeAttr('disabled')
}

$(document).ready(function () {
    var inputItemsModel = document.getElementById('form-order-check-list-car_mark');
    if (inputItemsModel) {
        inputItemsModel.onchange = function () {
            var targetValue = inputItemsModel.value;
            $('#form-order-check-list-max-car_model').attr('disabled', true)
            loadAjax({
                url: '/auto-select/get-car-model',
                data: {id: targetValue},
                type: 'POST',
                before: function () {
                    $('#form-order-check-list-max-car_model').addClass('loader')
                },
                success: function (data) {
                    loadInput(data, '#form-order-check-list-car_model');
                },
                error: function (q, w, r) {
                    console.log(q, w, r);
                },
                complete: function (id, sss) {
                    console.log(id, sss);
                }
            });
        };
    }

    var inputItemsModification = document.getElementById('form-order-check-list-car_model');
    if (inputItemsModification) {
        inputItemsModification.onchange = function () {
            var targetValue = inputItemsModification.value;
            loadAjax({
                url: '/auto-select/get-car-modifications',
                data: {id: targetValue},
                type: 'POST',
                success: function (data) {
                    loadInput(data, '#form-order-check-list-car_modification');
                },
                error: function (q, w, r) {
                    console.log(q, w, r);
                },
                complete: function (id, sss) {
                    console.log(id, sss);
                }
            });
        };
    }

    var inputItemsCarModel = document.getElementById('online-appointment-form-car_mark');
    if (inputItemsCarModel) {
        inputItemsCarModel.onchange = function () {
            var targetValue = inputItemsCarModel.value;
            $('#online-appointment-form-car_model').attr('disabled', true)
            loadAjax({
                url: '/auto-select/get-car-model',
                data: {id: targetValue},
                type: 'POST',
                before: function () {
                    $('#online-appointment-form-car_model').addClass('loader')
                },
                success: function (data) {
                    loadInput(data, '#online-appointment-form-car_model');
                },
                error: function (q, w, r) {
                    console.log(q, w, r);
                },
                complete: function (id, sss) {
                    console.log(id, sss);
                }
            });
        };
    }

    var inputItemsCarModification = document.getElementById('online-appointment-form-car_model');
    if (inputItemsCarModification) {
        inputItemsCarModification.onchange = function () {
            var targetValue = inputItemsCarModification.value;
            loadAjax({
                url: '/auto-select/get-car-modifications',
                data: {id: targetValue},
                type: 'POST',
                success: function (data) {
                    loadInput(data, '#online-appointment-form-car_modification');
                },
                error: function (q, w, r) {
                    console.log(q, w, r);
                },
                complete: function (id, sss) {
                    console.log(id, sss);
                }
            });
        };
    }
});
/*load input car, model, modification end*/

/* order check list */
$(document).on('submit', '.order-price-shod-razval-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-price-shod-razval/add-order",
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        async: true,
        dataType: "json",
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});
/* order check list end */
/*order power*/
function showModalPower(data) {
    $('#addToOrderPower .modal-body').html(data);
    $('#addToOrderPower').modal('show');
}

$(document).on('click', '.add-to-order-power', function (e) {
    e.preventDefault();
    var id = $(this).data('power');
    var title = $(this).data('title');
    loadAjax({
        url: '/order-power-equipment/add-modal',
        async: true,
        data: {id: id, title: title},
        type: 'POST',
        success: function (power) {
            if (power) {
                getTitleModal(title);
                showModalPower(power);
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (id, sss) {
            console.log(id, sss);
        }
    });
});

$(document).on('submit', '#order-power-equipment-modal-form', function (e) {
    e.preventDefault();
    loadAjax({
        url: "/order-power-equipment/add-order",
        async: true,
        type: "POST",
        data: $(e.currentTarget).serializeArray(),
        dataType: "json",
        beforeSend: function () {

        },
        success: function (data) {
            funcSuccessNoty(data);
            if (parseInt(data.code) !== 400) {
                setTimeout(function () {
                    location.reload();
                }, 4500)
            }
        },
        error: function (q, w, r) {
            console.log(q, w, r);
        },
        complete: function (data, sss) {
            console.log(data, sss);
        }
    });

    return false;
});