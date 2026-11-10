<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Attributes\Table;
use Illuminate\Database\Eloquent\Attributes\Fillable;

#[Table('clinics_addresses')]
#[Fillable(['options->enabled'])]
class ClinicAddress extends Model
{
    protected $fillable = [
        'title', 'description', 'user_id',
        'address', 'is_main', 'clinic_id'
    ];
}
