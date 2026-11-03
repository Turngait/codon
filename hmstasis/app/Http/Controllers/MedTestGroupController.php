<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MedTestGroupController extends Controller
{
    public function add(Request $request) 
    {
        $data = $request->all();
        return ["data" => $data];
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
