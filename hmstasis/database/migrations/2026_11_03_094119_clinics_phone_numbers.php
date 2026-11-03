<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('clinics_phone_numbers', function (Blueprint $table) {
            $table->id();
            $table->biginteger('user_id');
            $table->string('title');
            $table->string('description')->nullable();
            $table->string('phone_number');
            $table->string('is_main')->default(false);
            $table->foreignId('clinic_id')->constrained('clinics')->onDelete('cascade');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::drop('clinics_phone_numbers');
    }
};
