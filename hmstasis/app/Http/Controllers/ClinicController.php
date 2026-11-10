<?php

namespace App\Http\Controllers;

use App\DTO\AddClinicData;
use App\Services\ClinicService;
use Illuminate\Http\Request;
use App\Http\Requests\AddClinicRequest;


class ClinicController extends Controller
{
    public function add(AddClinicRequest $request) 
    {
        $data = $request->validated();
        $dto = AddClinicData::fromArray($data);

        $service = new ClinicService();
        $id = $service->createClinic($dto);

        return ["data" => ['clinic_id' => $id]];
    }

    public function edit(Request $request) 
    {
        $data = $request->all();
        return ["data" => $data];
    }

    public function delete(Request $request) 
    {
        $data = $request->all();
        return ["data" => $data];
    }
}
