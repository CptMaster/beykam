$(document).ready(function () {
    $("#personnel-data").DataTable({
        dom: 'Blfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3]
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3]
                }
            },
            {
                extend: 'print',
                text : 'YAZDIR',
                exportOptions: {
                    columns: [0, 1, 2, 3]
                }
            }
        ],
        columnDefs: [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"bSortable": false, "aTargets": [4]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#category-data").DataTable({
        columnDefs: [
            {"width": "7%", "targets": 0},
            {"width": "70%", "targets": 1},
            {"bSortable": false, "aTargets": [2]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#product-data").DataTable({
        columnDefs: [
            {"width": "10%", "targets": 0},
            {"width": "10%", "targets": 6},
            {"bSortable": false, "aTargets": [6]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#purchase-data").DataTable({
        dom: 'Blfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: 'print',
                text : 'YAZDIR',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            }
        ],
        columnDefs: [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"bSortable": false, "aTargets": [6]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#sales-data").DataTable({
        dom: 'Blfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
                }
            },
            {
                extend: 'print',
                text : 'YAZDIR',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
                }
            }
        ],
        columnDefs: [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"width": "10%", "targets": 9},
            {"bSortable": false, "aTargets": [9]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#supplier-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"bSortable": false, "aTargets": [4]}
        ],
        "language": {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#inventory-data").DataTable({
        dom: 'Blfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: 'print',
                text : 'YAZDIR',
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            }
        ],
        columnDefs: [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "7%", "targets": 2},
            {"bSortable": false, "aTargets": [6]}
        ],
        language: {
            "url": "/static/json/Turkish.json"
        }
    });

});

function clicked(e) {
    if (!confirm('Silmek istediğinize emin misiniz?'))e.preventDefault();
}