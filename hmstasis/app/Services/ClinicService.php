<?php

namespace App\Services;

use App\Models\Clinic;
use App\Models\ClinicAddress;
use App\Models\ClinicPhones;
use App\DTO\AddClinicData;
use Illuminate\Support\Facades\DB;


class ClinicService
{
    public function createClinic(AddClinicData $data)
    {
        return DB::transaction(function () use ($data) {
            $clinic = Clinic::create([
                'title' => $data->title,
                'description' => $data->description,
                'user_id' => $data->user_id,
                'main_site' => $data->mainSite,
                'law_info' => $data->lawInfo
            ]);
            $clinic_address = ClinicAddress::create([
                'title' => $data->title,
                'description' => $data->description,
                'user_id' => $data->user_id,
                'address' => $data->mainAddress,
                'is_main' => true,
                'clinic_id' => $clinic->id,
            ]);
        return ['clinic_id'=> $clinic->id,'clinic_address_id' => $clinic_address->id];
    });
        
    }
}