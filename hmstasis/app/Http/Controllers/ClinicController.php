<?php

namespace App\Http\Controllers;

use App\DTO\AddClinicData;
use App\DTO\DeleteClinicData;
use App\DTO\UpdateClinicData;
use App\Services\ClinicService;
use Illuminate\Http\Request;
use App\Http\Requests\AddClinicRequest;
use App\Http\Requests\UpdateClinicRequest;
use App\Http\Requests\DeleteClinicRequest;


class ClinicController extends Controller
{
    public function add(AddClinicRequest $request) 
    {
        $data = $request->validated();
        $dto = AddClinicData::fromArray($data);

        $service = new ClinicService();
        return $service->createClinic($dto);
    }

    public function edit(UpdateClinicRequest $request) 
    {
        $data = $request->validated();
        $dto = UpdateClinicData::fromArray($data);
        $service = new ClinicService();
        return $service->updateClinic($dto);
    }

    public function delete(DeleteClinicRequest $request) 
    {
        $data = $request->validated();
        $dto = DeleteClinicData::fromArray($data);
        $service = new ClinicService();
        return $service->deleteClinic($dto);
    }
}
