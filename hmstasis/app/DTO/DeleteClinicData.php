<?php

namespace App\DTO;

final readonly class DeleteClinicData
{
    public function __construct(
        public int $clinic_id,
        public int $user_id,
    ) {}
    public static function fromArray(array $data): self
    {
        return new self(
            user_id: $data['user_id'],
            clinic_id: $data['clinic_id'],
        );
    }
}