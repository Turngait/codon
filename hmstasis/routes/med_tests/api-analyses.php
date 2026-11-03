<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MedTestController;
use App\Http\Controllers\MedTestGroupController;
use App\Http\Controllers\MedTestValueController;

Route::prefix('mtests')->group(function () {
    Route::post('/mtest', [MedTestController::class, 'add']);
    Route::put('/mtest', [MedTestController::class, 'edit']);
    Route::delete('/mtest', [MedTestController::class, 'delete']);

    // mtestgroup
    Route::post('/mtestgroup', [MedTestGroupController::class, 'add']);
    Route::put('/mtestgroup', [MedTestGroupController::class, 'edit']);
    Route::delete('/mtestgroup', [MedTestGroupController::class, 'delete']);

    // mtestvalue
    Route::post('/mtestvalue', [MedTestValueController::class, 'add']);
    Route::put('/mtestvalue', [MedTestValueController::class, 'edit']);
    Route::delete('/mtestvalue', [MedTestValueController::class, 'delete']);
});
