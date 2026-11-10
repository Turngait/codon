<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Table;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Model;

#[Table('clinics')]
#[Fillable(['options->enabled'])]
class Clinic extends Model
{
    protected $fillable = [
        'title', 'description', 'user_id',
        'main_site', 'law_info'
    ];
}
