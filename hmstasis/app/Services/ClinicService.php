<?php

namespace App\Services;

use App\Models\Clinic;
use App\Models\ClinicAddress;
use App\Models\ClinicPhones;
use App\DTO\AddClinicData;
use App\DTO\DeleteClinicData;
use App\DTO\UpdateClinicData;
use Illuminate\Support\Facades\DB;


class ClinicService
{
    public function createClinic(AddClinicData $data)
    {
        try 
        {
            $old_clinic = $this->getClinicByTitleForUser($data->title, $data->user_id);

            if(!is_null($old_clinic) || !empty($old_clinic)) return ['status' => 4003, "msg" => 'Clinic already exist', "data" => null];

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
            return ['status' => 200, "msg" => 'Clinic was added', "data" => ['clinic_id'=> $clinic->id,'clinic_address_id' => $clinic_address->id]];
            });
        }
        catch (\Exception $e)
        {
            return ['status' => 5000, "msg" => $e->getMessage(), "data" => null];
        }
    }

    public function updateClinic(UpdateClinicData $data)
    {
        try 
        {
            $old_clinic = $this->getClinicById($data->clinic_id);

            if(is_null($old_clinic) || empty($old_clinic)) return ['status' => 4004, "msg" => 'Clinic does not exist', "data" => null];
            
            $old_clinic->title = $data->title;
            $old_clinic->description = $data->description;
            $old_clinic->main_site = $data->mainSite;
            $old_clinic->law_info = $data->lawInfo;

            $old_clinic->save();

            return ['status' => 200, "msg" => 'Clinic was updated', "data" => null];
        }
        catch (\Exception $e) 
        {
            return ['status' => 5000, "msg" => $e->getMessage(), "data" => null];
        }
    }

    public function deleteClinic(DeleteClinicData $data)
    {
        try
        {
            $old_clinic = $this->getClinicById($data->clinic_id);
            if(is_null($old_clinic) || empty($old_clinic)) return ['status' => 4004, "msg" => 'Clinic does not exist', "data" => null];

            $old_clinic->delete();
            return ['status' => 200, "msg" => 'Clinic was deleted', "data" => null];
        }
        catch (\Exception $e) 
        {
            return ['status' => 5000, "msg" => $e->getMessage(), "data" => null];
        }
    }

    private function getClinicByTitleForUser(string $title, int $user_id)
    {
        return Clinic::where('title', $title)->where('user_id', $user_id)->first();
    }

    private function getClinicById(int $id)
    {
        return Clinic::where('id', $id)->first();
    }
}