<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/getAllInfo', function (Request $request) {
    return 'All info';
});

require __DIR__.'/clinic/api-clinics.php';
require __DIR__.'/med_tests/api-analyses.php';