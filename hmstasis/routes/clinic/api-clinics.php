<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ClinicController;
use App\Http\Controllers\ClinicAddressController;
use App\Http\Controllers\ClinicPhoneController;

Route::prefix('clinics')->group(function () {
    Route::post('/clinic', [ClinicController::class, 'add']);
    Route::put('/clinic', [ClinicController::class, 'edit']);
    Route::delete('/clinic', [ClinicController::class, 'delete']);

    // clnicaddress
    Route::post('/clnicaddress', [ClinicAddressController::class, 'add']);
    Route::put('/clnicaddress', [ClinicAddressController::class, 'edit']);
    Route::delete('/clnicaddress', [ClinicAddressController::class, 'delete']);

    // clnicphone
    Route::post('/clnicphone', [ClinicPhoneController::class, 'add']);
    Route::put('/clnicphone', [ClinicPhoneController::class, 'edit']);
    Route::delete('/clnicphone', [ClinicPhoneController::class, 'delete']);
});




