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
        Schema::create('med_tests_values', function (Blueprint $table) {
            $table->id();
            $table->biginteger('user_id');
            $table->string('value');
            $table->string('normal');
            $table->string('specialist')->nullable();
            $table->string('equipment')->nullable();
            $table->foreignId('med_test_id')->constrained('med_tests')->onDelete('cascade');
            $table->foreignId('clinic_id')->constrained('clinics');
            $table->date('date');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::drop('med_tests_values');
    }
};
