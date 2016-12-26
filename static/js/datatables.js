$(function () {
    $("#personnel-data").dataTable({
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
    $("#category-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "70%", "targets": 1},
            {"bSortable": false, "aTargets": [2]}
        ],
        "language": {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#product-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "70%", "targets": 1},
            {"bSortable": false, "aTargets": [3]}
        ],
        "language": {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#purchase-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"bSortable": false, "aTargets": [5]}
        ],
        "language": {
            "url": "/static/json/Turkish.json"
        }
    });
    $("#sales-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "25%", "targets": 2},
            {"bSortable": false, "aTargets": [7]}
        ],
        "language": {
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
    $("#inventory-data").dataTable({
        "columnDefs": [
            {"width": "7%", "targets": 0},
            {"width": "25%", "targets": 1},
            {"width": "7%", "targets": 2},
            {"bSortable": false, "aTargets": [6]}
        ],
        "language": {
            "url": "/static/json/Turkish.json"
        }
    });

});